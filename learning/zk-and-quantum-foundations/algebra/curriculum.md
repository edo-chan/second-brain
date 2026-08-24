# Abstract Algebra Curriculum

## Goal

Study abstract algebra slowly as a coherent mathematical subject. Build enough
command to prove the central results, compute with concrete examples, and use
the theory later in finite-field cryptography, elliptic curves, pairings,
Groth16, and algebraic hash permutations.

The downstream applications motivate occasional examples but do not determine
the order or pace of the course.

## A0: Diagnostic and proof language

1. Sets, functions, relations, and equivalence classes
2. Direct proof, contradiction, induction, and counterexamples
3. Modular arithmetic and basic linear algebra retrieval
4. Algebraic structures as sets equipped with operations

## A1: Groups

5. Group axioms and examples
6. Subgroups, generated subgroups, and cyclic groups
7. Permutation groups
8. Cosets and Lagrange's theorem
9. Homomorphisms, kernels, images, and isomorphisms
10. Normal subgroups and quotient groups
11. The isomorphism theorems
12. Group actions, orbits, stabilizers, and counting
13. Direct products and finite abelian groups
14. Sylow theory

## A2: Rings

15. Rings, subrings, units, zero divisors, and domains
16. Ring homomorphisms, ideals, and quotient rings
17. Prime and maximal ideals
18. Euclidean domains, principal ideal domains, and unique factorization
19. Polynomial rings and division
20. Irreducibility and factorization
21. The Chinese remainder theorem

## A3: Fields

22. Field extensions and degrees
23. Algebraic elements and minimal polynomials
24. Splitting fields and algebraic closure
25. Finite fields and their subfields
26. Frobenius, the multiplicative group, trace, and norm
27. Galois groups and the fundamental correspondence

## A4: Linear and multilinear structure

28. Vector spaces, dual spaces, and linear maps over general fields
29. Eigenstructure, canonical forms, and minimal polynomials
30. Bilinear forms and duality
31. Modules as generalized vector spaces
32. Tensor products and multilinear maps

## A5: Polynomial and computational algebra

33. Evaluation, interpolation, roots, and multiplicity
34. Multivariate polynomial rings
35. Ideals and algebraic sets
36. Resultants and elimination
37. Groebner bases as an optional deeper branch
38. Symbolic and finite-field computation in small examples

## A6: Elliptic curves and pairings

39. Affine and projective algebraic curves
40. The elliptic-curve group law
41. Elliptic curves over finite fields
42. Scalar multiplication and discrete logarithms
43. Rational functions and divisors at the level needed for pairings
44. Weil and Tate pairing ideas
45. Miller's algorithm and pairing-friendly curves

## Lesson standard

Each lesson centers on one definition or theorem and includes:

1. a concrete example before abstraction;
2. a proof or derivation by hand;
3. a short problem set;
4. a small computational experiment when it exposes structure;
5. a reconstruction or transfer checkpoint.

Do not require a cryptographic justification for every lesson. Add an
application window only when it clarifies the mathematics already being
studied.

## Completion boundary

The algebra spine is not complete merely because every topic has been read.
Completion requires independent proofs and computations at the level named by
each lesson checkpoint. The Groth16 and algebraic-hash branches may begin once
their actual prerequisites are demonstrated; they do not need to wait for
every optional algebra topic.
