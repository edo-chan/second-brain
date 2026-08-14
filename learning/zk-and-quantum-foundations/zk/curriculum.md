# ZK Track Curriculum

## Goal

Develop the mathematics and security vocabulary needed to derive Groth16 from
arithmetic computation and place it within the broader ZK proof-system
landscape.

## Z0: Diagnostic

- Complete the [ZK diagnostic](diagnostic.md).
- Choose the earliest non-operational dependency as the first lesson.

## Z1: Algebraic language

1. Finite fields and extension fields
2. Cyclic groups and scalar encodings
3. Elliptic-curve groups
4. Polynomial rings and polynomial evaluation
5. Interpolation, root bounds, and vanishing polynomials

## Z2: Statements as constraints

6. Relations, statements, witnesses, and languages
7. Arithmetic circuits
8. Rank-1 constraint systems
9. Witness vectors and public/private input boundaries
10. From R1CS to quadratic arithmetic programs
11. Divisibility and polynomial identity checks

## Z3: Proof-system properties

12. Completeness and soundness
13. Proofs versus arguments
14. Knowledge soundness and extraction
15. Zero knowledge and simulation
16. Interactive proofs and Fiat-Shamir
17. Polynomial commitments and structured reference strings

## Z4: Pairing-based cryptography

18. Bilinear groups and non-degeneracy
19. Pairing-friendly curves and embedding fields
20. Hidden scalar arithmetic through pairings
21. Relevant bilinear-group assumptions

## Z5: Groth16

22. QAP evaluation at the secret point tau
23. Alpha, beta, gamma, and delta
24. Proving and verification keys
25. Constructing A, B, and C
26. Deriving the verifier equation
27. Perfect completeness and zero knowledge
28. Classical soundness and toxic-waste boundaries

## Z6: Broader ZK foundations

29. Sumcheck and multilinear extensions
30. FRI and code-based commitments
31. PLONKish and AIR arithmetizations
32. STARKs, Binius, and Flock

The Z6 ordering is provisional and does not select a future research direction.

## Lesson standard

Every lesson contains one definition or theorem, its derivation, a worked
example, a mastery checkpoint, and a short note on how it feeds the ZK track or
a later bridge.
