---
name: ed-service-boundaries
description: API boundary, proto/gRPC service organization, webhook verification, and sensitive logging rules for Ed's repos. Use when changing public APIs, gRPC services, webhooks, proto files, auth interceptors, or logging around vendor/user payloads.
---

# Ed Service Boundaries

Treat service boundaries as the place where trust, authentication, and logging policy must be explicit.

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
