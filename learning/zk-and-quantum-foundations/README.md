# ZK and Quantum Foundations

## Project state

- **Phase:** Foundations
- **Current activity:** Abstract-algebra diagnostic
- **Research direction:** Intentionally deferred
- **Started:** 2026-08-13

## Goal

Build first-principles command through a traditional algebra spine and two
later subject tracks:

1. study abstract algebra through groups, rings, fields, polynomials,
   elliptic curves, and pairings;
2. derive Groth16 from arithmetic computation and reconstruct the design of
   Poseidon-style algebraic hashes;
3. derive Shor's discrete-logarithm algorithm from quantum computation,
   Fourier sampling, and the abelian hidden-subgroup problem.

Connect the subjects only through explicit bridge modules. The main bridge is
a precise explanation of why a quantum discrete-logarithm algorithm destroys
Groth16 soundness without implying that hashes become reversible or that old
proofs reveal their witnesses.

## Materials

- [Curriculum map](curriculum.md)
- [Project diagnostic](diagnostic.md)
- [Progress and question log](progress.md)
- [Abstract-algebra spine](algebra/curriculum.md) and
  [diagnostic](algebra/diagnostic.md)
- [ZK track](zk/curriculum.md)
- [Quantum-cryptography track](quantum-cryptography/curriculum.md)
- [Teacher agent](../ed-teacher/SKILL.md)

## Learning rules

- Advance one main concept at a time.
- Use the traditional abstract-algebra sequence as the active spine; do not
  compress it into only the facts immediately needed by cryptography.
- Keep separate diagnostics, lessons, and progress for the algebra, ZK, and
  quantum tracks.
- End each lesson with an operational checkpoint.
- Record derivations and questions rather than relying on slogans.
- Use small explanatory experiments when they clarify the mathematics.
- Unlock a bridge only after both of its prerequisites are understood.
- Improve lesson size, sequencing, examples, and checkpoints when recorded
  learner evidence exposes a curriculum problem.
- Choose a paper, implementation, or other research direction after the
  foundation phase reveals a worthwhile question.

## Foundation checkpoint

The current foundation destination is reached when:

- the algebra checkpoints required by the downstream branches can be proved
  and computed independently;
- the Groth16 verifier equation from an R1CS/QAP;
- a Poseidon-style permutation can be reconstructed from its sponge, power
  map, linear layer, round structure, and stated security goals;
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
