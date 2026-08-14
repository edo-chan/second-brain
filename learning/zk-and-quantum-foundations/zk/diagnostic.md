# ZK Track Diagnostic

## Confidence map

Rate each item from 0 to 4 using the scale in the
[two-track diagnostic](../diagnostic.md).

- **Z1.** Modular arithmetic, finite fields, and extension fields
- **Z2.** Cyclic groups, group order, and scalar encodings
- **Z3.** Elliptic curves and the discrete-logarithm assumption
- **Z4.** Polynomial interpolation, root bounds, and vanishing polynomials
- **Z5.** Relations, statements, witnesses, and arithmetic circuits
- **Z6.** Rank-1 constraint systems
- **Z7.** Quadratic arithmetic programs
- **Z8.** Proofs, arguments, soundness, knowledge soundness, and zero knowledge
- **Z9.** Interactive proofs, Fiat-Shamir, and polynomial commitments
- **Z10.** Bilinear pairings and pairing-friendly curves
- **Z11.** Groth16 setup, prover, and verifier
- **Z12.** Python, SageMath, or Rust for ZK experiments

Submit the ratings before answering the probes.

## Adaptive probe bank

Answer only the probes selected after the confidence map is reviewed.

### ZP1: Scalar encodings

Let \(\mathbb G=\langle G\rangle\) have prime order \(r\), with
\([x]=xG\). State what linear combinations can be computed from \([x]\) and
\([y]\), and distinguish group inversion from recovering \(x\).

### ZP2: Field boundaries

Explain why the scalar field, elliptic-curve base field, and pairing target
extension field are distinct algebraic objects.

### ZP3: Polynomial checking

State the root bound for a nonzero degree-\(d\) polynomial and explain how it
supports randomized polynomial-identity testing. Include the small-field
caveat.

### ZP4: R1CS

Using a witness vector you define, encode

\[
z=xy,\qquad t=z+x
\]

as rank-1 constraints.

### ZP5: QAP

Explain at a high level how a family of rank-1 constraints becomes a single
polynomial-divisibility condition.

### ZP6: Security properties

Distinguish soundness, knowledge soundness, and zero knowledge. State whether
any one automatically implies another.

### ZP7: Pairings

State bilinearity for
\(e:\mathbb G_1\times\mathbb G_2\to\mathbb G_T\). Explain what a pairing
comparison reveals and what remains hidden under the discrete-log assumption.

### ZP8: Groth16

Describe the roles of the QAP, the structured reference string, and the three
proof elements \(A,B,C\). If any role is unfamiliar, identify it precisely.
