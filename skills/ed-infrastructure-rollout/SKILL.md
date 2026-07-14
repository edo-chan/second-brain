---
name: ed-infrastructure-rollout
description: Infrastructure, Terraform, secrets, environment scoping, AWS parameter/config, and rollout guardrails for Ed's repos. Use when touching Terraform, CI, branch protection, cloud resources, credentials, KMS/enclave flows, or deployed configuration.
---

# Ed Infrastructure Rollout

Inspect drift and scope before applying infrastructure changes.

## Secrets And Config

- Treat pasted credentials, API keys, private keys, and session tokens as sensitive unless explicitly marked throwaway.
- Do not persist private keys or secrets in source.
- Store public keys and non-secret service runtime configuration in SSM.
- Use AWS SSM Parameter Store as the sole source for service runtime configuration in every environment, including local development.
- Treat declared SSM parameters as required. Do not make them optional or add environment-variable, hardcoded, default-value, or local fallback paths when a parameter is missing.
- Configure local development to authenticate to AWS and read its environment-scoped configuration directly from SSM.

## Terraform And Environments

- Inspect plan and drift before applying Terraform unless the user explicitly asks for direct apply.
- Keep infrastructure changes scoped by environment.
- If a resource is per-environment, name and store it per-environment.
- Prefer deleting deprecated resources after traffic and dependencies are confirmed gone.
- Be especially willing to delete old EKS, ClickHouse, indexer, and unused Helm resources once confirmed unused.

## Signing And Enclaves

- For AWS signing and enclave work, keep private material owned by KMS/enclave flows where possible.
- Store only public keys or ciphertext blobs outside the signer boundary.

## Rollout Blockers

- When CI, branch protection, credentials, or cloud state blocks a rollout, state the exact blocker.
- Include the concrete next action rather than a vague status.
