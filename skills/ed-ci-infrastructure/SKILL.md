---
name: ed-ci-infrastructure
description: CI, Git publication, infrastructure, deployment, and rollout standards for Ed's repositories. Use when working with branches, commits, pull requests, merges, releases, GitHub Actions, CI failures, branch protection, Terraform, cloud resources, secrets, credentials, AWS parameter/config, KMS/enclave flows, deployed configuration, or production rollouts.
---

# Ed CI And Infrastructure

For branch, commit, pull-request, merge, and release actions, read
[git-workflow.md](references/git-workflow.md).

Keep multi-part repository work in a linear stack of focused pull requests.
Never merge without explicit merge authorization from the user in the current
session, except in the canonical second-brain repository. Second-brain PRs may
be merged without separate user approval once validation and repository gates
pass.

Inspect drift and scope before applying infrastructure changes.

## Secrets And Config

- Treat pasted credentials, API keys, private keys, and session tokens as sensitive unless explicitly marked throwaway.
- Do not persist private keys or secrets in source.
- Give each deployed caller only the secret for its own authenticated service
  surface. Admin, Developer, Api, Public, and Internal callers must not share
  credentials or impersonate one another by constructing another surface's
  headers.
- Removing a Vercel environment variable changes future deployments, not the
  immutable environment snapshot of an existing deployment. Remove the code
  dependency and replace the deployment; rotate the credential when immediate
  revocation from prior deployments is required.
- Classify each value as a credential, environment-specific configuration,
  customer-specific configuration, or stable public protocol constant.
- Store public keys and environment- or customer-specific service runtime
  configuration in SSM.
- Stable canonical public endpoints and paths may live in code when they are not
  credential-bearing, region-selected, customer-specific, or environment-
  varying.
- Before adding a new endpoint parameter, check whether an existing
  credentialed provider endpoint supports the required capability and verify it
  against the live provider contract.
- Use AWS SSM Parameter Store as the sole source for environment- and
  customer-specific service runtime configuration, including local development.
- Treat declared SSM parameters as required. Do not make them optional or add environment-variable, hardcoded, default-value, or local fallback paths when a parameter is missing.
- Configure local development to authenticate to AWS and read its environment-scoped configuration directly from SSM.

## Terraform And Environments

- Inspect plan and drift before applying Terraform unless the user explicitly asks for direct apply.
- Confirm each repository's environment semantics before changing infrastructure
  or SSM values. In `swig-dev-portal`, `dev` means the local
  Docker/Surfpool environment, not a shared cloud staging environment; its
  service URLs must resolve from local containers and must not point at
  cloud-only resources such as ElastiCache.
- Keep infrastructure changes scoped by environment.
- If a resource is per-environment, name and store it per-environment.
- Provision every new environment-scoped SSM parameter with Terraform before attempting to persist its real value.
- After Terraform creates the parameter, persist the real value in SSM and verify that every target environment can resolve it before deploying code that requires it.
- Treat missing, placeholder, sentinel, or unreadable SSM values as rollout blockers. Never deploy consuming code before the required value is persisted and verified.
- Prefer deleting deprecated resources after traffic and dependencies are confirmed gone.
- Be especially willing to delete old EKS, ClickHouse, indexer, and unused Helm resources once confirmed unused.

## Jobs And Service Shape

- Run durable background jobs as Temporal workflows/workers instead of
  long-running web handlers.
- Keep service code, proto, migrations, Terraform, and worker changes visible
  in the same repository and PR when they form one behavior.
- Use boring defaults: Postgres for durable state, Redis for cache, and SSM for
  deployed configuration. Add deployed parameters through Terraform so config
  cannot drift from infrastructure.
- Choose the smallest durable job shape: a one-off workflow for historical
  backfills, a Temporal schedule for periodic reconciliation, or a heartbeat
  loop for frequent polling.
- Do not start workflows and activities every few seconds when one
  long-running, heartbeating activity owns the loop more clearly and cheaply.

## Signing And Enclaves

- For AWS signing and enclave work, keep private material owned by KMS/enclave flows where possible.
- Store only public keys or ciphertext blobs outside the signer boundary.

## Rollout Blockers

- When CI, branch protection, credentials, or cloud state blocks a rollout, state the exact blocker.
- Include the concrete next action rather than a vague status.
