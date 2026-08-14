# Quantum-Cryptography Track Curriculum

## Goal

Develop quantum computation and cryptographic reasoning from first principles
through Shor, Grover, and the security models needed to evaluate classical and
post-quantum primitives.

This track initially emphasizes quantum algorithms and cryptanalysis. Quantum
communication protocols such as QKD form an optional later branch rather than
a prerequisite for understanding Shor.

## Q0: Diagnostic

- Complete the [quantum-cryptography diagnostic](diagnostic.md).
- Choose the earliest non-operational dependency as the first lesson.

## Q1: Quantum information language

1. Pure states, amplitudes, and global phase
2. Unitary evolution and measurement
3. Composite systems and tensor products
4. Entanglement, reduced states, and density matrices
5. No-cloning and distinguishability

## Q2: Quantum computation

6. Single- and multi-qubit gates
7. Reversible classical computation
8. Quantum circuits and complexity
9. Quantum oracles and phase kickback
10. Controlled group arithmetic

## Q3: Fourier methods

11. Fourier transform over finite cyclic groups
12. Quantum Fourier transform
13. Quantum phase estimation
14. Period finding
15. The abelian hidden-subgroup problem

## Q4: Quantum cryptanalysis

16. Shor's factoring algorithm
17. Shor's discrete-logarithm algorithm
18. Applying Shor to finite-field and elliptic-curve groups
19. Grover's search algorithm
20. Quantum collision and preimage considerations

## Q5: Concrete resources and security models

21. Reversible modular arithmetic
22. Reversible elliptic-curve addition
23. Logical qubits and gate counts
24. Error correction and physical resource estimates
25. Quantum random-oracle model
26. Post-quantum security levels and reductions

## Q6: Optional quantum-cryptography branch

27. BB84 and prepare-and-measure QKD
28. Entanglement-based QKD
29. Information-theoretic versus computational security
30. Authentication requirements and composable security

The Q6 branch is not required for the Shor-Groth16 bridge and will be taken
only if it becomes independently interesting.

## Lesson standard

Every lesson contains one definition or algorithmic idea, its linear-algebraic
derivation, a small circuit or calculation where useful, a mastery checkpoint,
and a note on its cryptographic significance.
