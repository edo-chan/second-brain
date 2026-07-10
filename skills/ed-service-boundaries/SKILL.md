---
name: ed-service-boundaries
description: API and vendor-client boundaries, proto/gRPC service organization, webhook verification, and sensitive logging rules for Ed's repos. Use when changing public APIs, vendor integrations, HTTP clients, response parsing, gRPC services, webhooks, proto files, auth interceptors, or logging around vendor/user payloads.
---

# Ed Service Boundaries

Treat service boundaries as the place where trust, authentication, and logging policy must be explicit.

## Vendor Clients

- Treat each vendor endpoint as a distinct contract.
- Expose an explicit endpoint-specific method that returns a clear concrete response struct.
- Do not expose generic request/response wrappers or generic JSON methods such as `get_json<T>`.
- Do not let `serde_json::Value` or raw upstream response bodies cross the vendor-library boundary.
- Keep HTTP, authentication, retries, response-body handling, and deserialization inside the vendor library.
- Allow a raw body only inside a private transport helper, and deserialize it before the public endpoint method returns.
- Keep response types beside the feature or endpoint implementation that exposes them; do not create a giant shared vendor types file.
- Let consuming services perform only the explicit mapping from typed vendor structs into domain or proto types.
- Test documented response deserialization at the vendor endpoint boundary, then test the small vendor-to-domain mapping separately.
- Treat any new or extended violation of these rules as blocking for approval. Request changes even when functional behavior and tests otherwise pass.

## Proto And gRPC

- Keep proto files to one service each.
- If a new independently routed service is needed, create a separate proto file.
- Wire descriptor generation, Rust codegen, gateway routing, and client type generation for new proto files.
- Services named with the `Api` prefix are public API-key authenticated services.
- Register `Api` services with the repo's API-key auth interceptor at the tonic service boundary, or use the existing centralized API-key auth pattern before handler logic runs.

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
- Avoid moving concrete vendor request/response types into giant shared files before there is a real reuse boundary.
- Keep vendor property and lookup types with the feature that consumes or exposes them.
