# Quantum-Cryptography Track Diagnostic

## Confidence map

Rate each item from 0 to 4 using the scale in the
[two-track diagnostic](../diagnostic.md).

- **Q1.** Complex vector spaces, inner products, eigenvectors, and spectral
  decomposition
- **Q2.** Qubits, global phase, unitary evolution, and measurement
- **Q3.** Tensor products, composite systems, entanglement, and reduced states
- **Q4.** Quantum gates, circuits, and computational-basis reasoning
- **Q5.** Reversible computation and quantum oracles
- **Q6.** Quantum Fourier transform
- **Q7.** Phase estimation
- **Q8.** Period finding
- **Q9.** Abelian hidden-subgroup problem
- **Q10.** Shor's factoring and discrete-logarithm algorithms
- **Q11.** Grover search and quantum attacks on hashes
- **Q12.** Quantum resource estimation, QROM, and post-quantum security models

Submit the ratings before answering the probes.

## Adaptive probe bank

Answer only the probes selected after the confidence map is reviewed.

### QP1: State and measurement

For

\[
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle,
\]

state the normalization condition and the computational-basis measurement
probabilities. Explain why global phase is unobservable.

### QP2: Tensor products

Distinguish a separable two-qubit state from an entangled state. Determine
whether

\[
(|00\rangle+|11\rangle)/\sqrt2
\]

is separable and justify the answer.

### QP3: Reversibility

Explain why a quantum oracle for a classical function is normally represented
as

\[
|x,y\rangle\mapsto|x,y\oplus f(x)\rangle
\]

rather than \(|x\rangle\mapsto|f(x)\rangle\).

### QP4: QFT

Write the action of the QFT over \(\mathbb Z_N\) on \(|x\rangle\). Explain
why periodic structure becomes concentrated in related frequency outcomes.

### QP5: Phase estimation

Given an eigenstate \(|u\rangle\) of a unitary \(U\) with eigenvalue
\(e^{2\pi i\theta}\), state what phase estimation returns and what resources
determine its precision.

### QP6: Hidden subgroup

Let \(Q=xG\) and define

\[
f(a,b)=aG+bQ.
\]

Find the subgroup of \(\mathbb Z_r^2\) on whose cosets \(f\) is constant.

### QP7: Shor versus Grover

Contrast the kind of speedup Shor gives for discrete logarithms with the
speedup Grover gives for unstructured preimage search. State the cryptographic
consequence of each.

### QP8: Physical meaning

Distinguish logical qubits, physical qubits, logical gate count, and wall-clock
runtime in a fault-tolerant attack estimate.
