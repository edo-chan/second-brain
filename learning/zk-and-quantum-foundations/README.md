# ZK and Quantum Foundations

## Project state

- **Phase:** Foundations
- **Current activity:** Two-track diagnostic
- **Research direction:** Intentionally deferred
- **Started:** 2026-08-13

## Goal

Build first-principles command of two independent subjects:

1. derive Groth16 from finite fields, polynomials, arithmetization, and
   pairings;
2. derive Shor's discrete-logarithm algorithm from quantum computation,
   Fourier sampling, and the abelian hidden-subgroup problem.

Connect the subjects only through explicit bridge modules. The main bridge is
a precise explanation of why a quantum discrete-logarithm algorithm destroys
Groth16 soundness without implying that hashes become reversible or that old
proofs reveal their witnesses.

## Materials

- [Two-track curriculum](curriculum.md)
- [Two-track diagnostic](diagnostic.md)
- [Progress and question log](progress.md)
- [ZK track](zk/curriculum.md)
- [Quantum-cryptography track](quantum-cryptography/curriculum.md)
- [Teacher agent](../ed-teacher/SKILL.md)

## Learning rules

- Advance one main concept at a time.
- Keep separate diagnostics, lessons, and progress for the two tracks.
- End each lesson with an operational checkpoint.
- Record derivations and questions rather than relying on slogans.
- Use small explanatory experiments when they clarify the mathematics.
- Unlock a bridge only after both of its prerequisites are understood.
- Improve lesson size, sequencing, examples, and checkpoints when recorded
  learner evidence exposes a curriculum problem.
- Choose a paper, implementation, or other research direction after the
  foundation phase reveals a worthwhile question.

## Foundation checkpoint

The foundation phase is complete when both of these derivations can be
reconstructed without references:

- the Groth16 verifier equation from an R1CS/QAP;
- Shor's discrete-logarithm algorithm from Fourier sampling of a hidden
  subgroup.

The final checkpoint connects those derivations and identifies exactly which
classical hardness assumption fails.

## Initial reading map

- [Jens Groth, *On the Size of Pairing-Based Non-interactive Arguments*](https://discovery.ucl.ac.uk/id/eprint/1501201/)
- [Peter Shor, *Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer*](https://epubs.siam.org/doi/10.1137/S0097539795293172)
- [Roetteler et al., *Quantum Resource Estimates for Computing Elliptic Curve Discrete Logarithms*](https://arxiv.org/abs/1706.06752)
- [Justin Thaler, *Proofs, Arguments, and Zero-Knowledge*](https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.html)
- [Binius64 Blueprint](https://www.binius.xyz/blueprint/)
- [Flock: Fast Proving for Batch Boolean Computations](https://arxiv.org/abs/2607.27491)
- [leanVM](https://github.com/leanEthereum/leanVM)

Add sources as each concept is studied. This is a starting map, not a claim
that a research direction has been selected.
