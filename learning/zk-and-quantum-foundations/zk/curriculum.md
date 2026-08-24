# ZK Track Curriculum

## Goal

Use the algebra spine to derive Groth16 from arithmetic computation, then
reconstruct Poseidon-style algebraic hashes and place both within the broader
ZK landscape.

## Z0: Diagnostic

- Complete the [ZK diagnostic](diagnostic.md).
- Choose the earliest non-operational dependency as the first lesson.

## Z1: Algebraic bridge

Complete the relevant checkpoints in the
[abstract-algebra spine](../algebra/curriculum.md), then synthesize:

1. finite fields and extension fields;
2. cyclic groups and scalar encodings;
3. elliptic-curve groups;
4. polynomial rings, evaluation, and interpolation;
5. root bounds and vanishing polynomials.

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

## Z6: Algebraic hashes

29. Hash functions, permutations, and sponge constructions
30. Arithmetization cost and field-native design
31. Power-map S-boxes and algebraic degree
32. Linear layers, diffusion, and MDS matrices
33. Poseidon round structure and parameter reasoning
34. Differential, linear, and algebraic attack models
35. Reconstructing and implementing a toy Poseidon instance
36. Formulating, testing, and attacking a variant

## Z7: Broader ZK foundations

37. Sumcheck and multilinear extensions
38. FRI and code-based commitments
39. PLONKish and AIR arithmetizations
40. STARKs, Binius, and Flock

The Z7 ordering is provisional and does not select a future research direction.

## Lesson standard

Every lesson contains one definition or theorem, its derivation, a worked
example, a mastery checkpoint, and a small computation when useful. Application
notes are optional; they must not become the justification for every topic.
