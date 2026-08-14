# Two-Track Curriculum

ZK proof systems and quantum cryptography progress independently. Each has its
own diagnostic, lesson sequence, checkpoints, and progress state.

## Track Z: Zero-knowledge proof systems

- [Curriculum](zk/curriculum.md)
- [Diagnostic](zk/diagnostic.md)

```text
fields + groups + polynomials
        |
        v
arithmetic circuits -> R1CS -> QAP
        |
        v
pairings + structured reference strings
        |
        v
Groth16 prover, verifier, and security properties
        |
        v
broader ZK proof-system landscape
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

- Complete both diagnostics first.
- Choose one starting lesson independently for each track.
- Alternate tracks unless one develops a missing shared prerequisite.
- Keep each lesson to one main concept.
- Unlock a bridge after both prerequisite checkpoints are complete.
- Keep research direction deferred until the foundation phase ends.
