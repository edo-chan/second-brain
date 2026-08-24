# Algebra Spine with ZK and Quantum Tracks

Abstract algebra is the active traditional spine. ZK proof systems and quantum
cryptography retain independent diagnostics, lesson sequences, checkpoints,
and progress states. The applications do not determine the pace of the
algebra course.

## Track A: Abstract algebra spine

- [Curriculum](algebra/curriculum.md)
- [Diagnostic](algebra/diagnostic.md)

```text
proof language -> groups -> rings -> fields
                              |
                              v
linear structure + polynomials
              |
              v
elliptic curves + pairings
```

## Track Z: Zero-knowledge proof systems

- [Curriculum](zk/curriculum.md)
- [Diagnostic](zk/diagnostic.md)

```text
algebra spine + polynomials
        |
        +-> arithmetic circuits -> R1CS -> QAP
        |               |
        |               v
        |      pairings + structured reference strings
        |               |
        |               v
        |      Groth16 prover, verifier, and security properties
        |
        +-> sponge + power maps + linear layers
                        |
                        v
              Poseidon-style algebraic hashes
```

## Track Q: Quantum cryptography

- [Curriculum](quantum-cryptography/curriculum.md)
- [Diagnostic](quantum-cryptography/diagnostic.md)

```text
quantum states + measurement
        |
        v
reversible computation + quantum oracles
        |
        v
QFT -> phase estimation -> hidden subgroups
        |
        v
Shor DLP + Grover search
        |
        v
cryptanalytic and post-quantum consequences
```

## Bridge modules

### Bridge 1: Discrete-logarithm boundary

- **ZK supplies:** Cyclic-group encodings, elliptic-curve groups, and the
  classical discrete-log assumption.
- **Quantum supplies:** The hidden-subgroup formulation and Shor's
  discrete-logarithm algorithm.
- **Result:** Explain why a public elliptic-curve point no longer hides its
  scalar from a quantum attacker.

### Bridge 2: Groth16 soundness

- **ZK supplies:** The Groth16 verification equation and the roles of its
  encoded setup scalars.
- **Quantum supplies:** Efficient discrete-log extraction in
  \(\mathbb G_1\) and \(\mathbb G_2\).
- **Result:** Reduce verification to a scalar equation and construct an
  accepted proof for a false statement.

### Bridge 3: Post-quantum ZK survey

- **ZK supplies:** Proof-system architecture, commitments, Fiat-Shamir, and
  verifier requirements.
- **Quantum supplies:** Shor, Grover, the QROM, and post-quantum assumption
  analysis.
- **Result:** Evaluate why hash- and code-based proof systems are candidates
  instead of merely labeling systems "PQ-safe."

## Operating rule

- Complete the algebra placement first, one item and one probe at a time.
- Let the algebra spine lead until a downstream lesson's prerequisites are
  demonstrated.
- Complete the ZK and quantum diagnostics before advancing those tracks.
- Choose one starting lesson independently for each track.
- Do not alternate mechanically. Use a side track when it is restorative or
  when the required foundation has already been demonstrated.
- Keep each lesson to one main concept.
- Unlock a bridge after both prerequisite checkpoints are complete.
- Keep research direction deferred until the foundation phase ends.
