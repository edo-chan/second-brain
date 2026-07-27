# Ed Service Boundaries

Treat service boundaries as the place where trust, authentication, and logging policy must be explicit.

## Vendor Clients

- Treat each vendor endpoint as a distinct contract.
- When a vendor-client boundary exists, expose an explicit endpoint-specific
  method that returns a clear concrete response struct.
- Review the request contract as strictly as the response contract. Identify
  caller-supplied, server-derived, and vendor-derived fields instead of showing
  or validating only the response shape.
- For signed payloads, distinguish who constructs instructions, who funds fees
  or tips, and who signs. Do not mutate an already signed message unless every
  affected signer can sign the resulting message.
- Use `Option` only for fields the vendor contract truly marks optional. Model required fields as required concrete fields; do not pass uncertainty through with `Option` or `serde(default)` merely to make malformed responses deserialize.
- For a required-but-nullable field, accept explicit `null` and reject omission.
  A plain `Option<T>` does not preserve that presence distinction.
- Distinguish missing data from unknown values. Keep extensible vendor identifiers as required strings when new codes are valid, and reject a missing identifier instead of collapsing it to `UNKNOWN` or `UNSPECIFIED`.
- Do not expose generic request/response wrappers or generic JSON methods such as `get_json<T>`.
- Do not let `serde_json::Value` or raw upstream response bodies cross the vendor-library boundary.
- Do not create a new vendor client, endpoint-method layer, trait, or other
  abstraction solely to eliminate generic JSON. When the current code does not
  otherwise warrant that layer, deserialize into concrete local structs at the
  existing ownership boundary.
- Keep HTTP, authentication, retries, response-body handling, and deserialization inside the vendor library.
- Allow a raw body only inside a private transport helper, and deserialize it before the public endpoint method returns.
- Never include an upstream response body in a public error or log message.
  Preserve a safe status, error class, and upstream request id instead.
- Keep response types beside the feature or endpoint implementation that exposes them; do not create a giant shared vendor types file.
- Model only the upstream fields that consumers use or the boundary must
  validate. Do not import a large optional vendor response dump or dependency
  when a focused endpoint type is sufficient.
- Let consuming services perform only the explicit mapping from typed vendor structs into domain or proto types.
- Reject responses that omit required upstream data with a structured boundary error instead of returning partial output. Use `FAILED_PRECONDITION` at a gRPC boundary when the missing field makes the requested result unusable.
- Return authoritative vendor identifiers and let downstream presentation own display labels. Do not synthesize provider or product names from codes unless a distinct typed vendor metadata endpoint supplies the canonical name.
- Validate response cardinality and correlate returned identifiers to the
  requested identifiers before accepting a response. Do not assume the first
  entry belongs to the request.
- Test each endpoint's concrete response deserialization inside the vendor library, including documented success responses, missing required fields, and the resulting typed error.
- For Rust consuming-service tests, use `mockall` at a focused typed vendor
  boundary. A production trait is justified when the consumer needs a
  replaceable dependency such as `Arc<dyn VendorClient>`; do not reject that
  interface merely because its main alternate implementation is a test mock.
- Mockall mocks of inherent methods are separate concrete types. Substituting
  them for a field typed as the real client requires `mockall_double`,
  test-only import rewriting, or generic code, so prefer trait injection when
  it matches the service's normal dependency shape.
- Keep the trait limited to the endpoint methods its consumers use. A thin
  implementation that delegates those methods to the concrete client is
  legitimate boundary wiring, not an unnecessary forwarding abstraction.
- When the trait belongs to another crate, a consuming crate's `mock!`
  declaration may repeat the method signatures. Prefer a shared,
  feature-gated generated mock only when reuse across consumers justifies the
  added test-support API.
- Return typed successes or errors from the mock and assert downstream status
  and domain mapping.
- Do not use an HTTP mock server to claim consuming-service logic coverage. It primarily proves that the configured fixture returns what was configured rather than isolating application behavior.
- Treat any new or extended violation of these rules as blocking for approval. Request changes even when functional behavior and tests otherwise pass.
- Keep HTTP client types and raw RPC messages private. Public errors should
  expose stable error classes and safe context such as status or request ids,
  not transport implementation types or response bodies.
- Keep provider-specific protocol differences in provider-specific operations.
  Do not thread `is_provider_x` flags through generic authorization, token, or
  verification code when the provider has a materially different contract.
- Use established libraries or platform caches for protocol metadata such as
  JWKS. Do not build a process-global cache, refresh-lock registry, generation
  counter, or stale-data policy inside an endpoint module.
- A provider token decoder is a trust boundary, not a generic convenience
  helper. Verify the exact signature algorithm, key, issuer, audience, expiry,
  nonce, and any required front-channel binding for the concrete flow.

## Authentication Flows

- Derive authorization context from a trusted boundary. Do not compare a
  caller-supplied `origin`, tenant, organization, issuer, or other claimed
  context with an allowlist and call the result authenticated.
- For browser redirects, derive a web origin from an exact registered redirect
  URI or establish it through a platform-authenticated channel. A query
  parameter copied through an isolated host does not prove the developer
  frontend's origin.
- Bind a multi-step authentication attempt to the exact provider
  configuration and credential identity selected at initiation. Callback and
  completion code must not silently reselect whichever configuration or
  credential is current after rotation.
- Derive stable user identity from authoritative verified issuer and subject
  values. Never substitute a mutable provider key, display label, route
  segment, or logging name for a signed identity namespace.
- When a component privately derives an identifier, another component cannot
  assert that identifier without a verifiable binding. Fail closed instead of
  relabeling an unbound canonical or default identifier.
- Prefer the smallest provider flow that supplies the required identity. Do not
  opt into hybrid or multi-token variants when a code exchange provides the
  required verified token.
- Complete browser-mediated authentication through its correlated return
  channel on both success and failure. Do not strand a popup or expose a raw
  transport response for provider denial.
- Treat browser-console logging as external disclosure. Never log launch URLs,
  authorization state, PKCE verifier or challenge material, token claims,
  proof inputs, signatures, or raw authentication errors.

## External Effects And Retry Ownership

- Decide whether the caller, vendor client, workflow, or platform owns retries.
  Do not add implicit retries at a layer that cannot reason about idempotency.
- Mark irreversible vendor acceptance explicitly and persist its identifier or
  accepted state before later confirmation, accounting, or response work.
- Never release idempotency after acceptance in a way that lets a retry repeat
  the external effect.
- Record exactly one API-request event per invocation, including errors and
  replays. Emit domain or billing events only for newly completed work so API
  telemetry cannot double bill a failed or repeated request.

## Proto And gRPC

- Model variant payloads with `oneof` instead of an enum plus unrelated
  variant-specific optional fields.
- Use unsigned proto integers for values that cannot be negative, including
  amounts and observed slots.
- Add `google.api.http` annotations to public endpoints.
- Keep proto files to one service each.
- If a new independently routed service is needed, create a separate proto file.
- Wire descriptor generation, Rust codegen, gateway routing, and client type generation for new proto files.
- Treat the service prefix as an authentication contract:
  - `Admin` means Swig operations/admin access. It does not mean an
    organization administrator in a developer application.
  - `Developer` means the developer portal UI backend acting with developer
    service authentication and an organization context.
  - `Api` means a developer-facing product API authenticated with that
    developer's API key.
  - `Public` means no authentication.
  - `Internal` means authenticated service-to-service traffic.
- Register every `Api` service with the repo's API-key auth interceptor at the
  tonic service boundary, or use the existing centralized API-key auth pattern
  before handler logic runs.
- Align route prefixes with the same contract: `/admin` belongs only to Swig
  operations, `/developer` to the developer portal backend, `/api` to
  developer API-key traffic, and `/public` to unauthenticated traffic.
- Do not infer an authentication boundary from an end-user role label such as
  "tenant admin." Name the actual caller and credential boundary.
- Do not mix differently authenticated endpoints behind an ambiguously named
  service or route prefix.
- Put closed public values such as network, flow kind, credential kind, provider
  variant, and lifecycle status in proto enums or `oneof` payloads. Validate and
  convert them once at the boundary; do not pass raw integers or strings through
  the service.

## Webhooks

- Put an explicit verification boundary before trusted webhook handler logic.
- Prefer a webhook signature interceptor or gateway verifier.
- Do not trust webhook payloads inside handlers until the verification boundary has run.

## Sensitive Logging

- Do not log sensitive vendor payloads, launch URLs, KYC/PII fields, upstream response bodies, API keys, signatures, or tokens.
- Prefer stable non-sensitive fields: status code, error class, request id, organization id, internal ids, and upstream request ids.
- Do not rely on broad redaction helpers as the primary safety mechanism.

## Handler Shape

- Keep request validation, auth boundary, domain logic, and response mapping easy to audit.
- Destructure transport requests in the handler and convert them into concrete
  typed domain inputs. Do not pass proto request messages into domain modules.
- Authenticate once at the service boundary or handler entry. Do not repeatedly
  extract claims only to bind them to an unused variable.
- Do not add wrapper helpers that only forward a call or rename, clone, trim, borrow, or convert a value. Keep trivial transformations inline, or fix the source type so the conversion disappears.
- Avoid moving concrete vendor request/response types into giant shared files before there is a real reuse boundary.
- Keep vendor property and lookup types with the feature that consumes or exposes them.
