# Progress

## Project state

- **Project phase:** Foundations
- **Current activity:** Abstract-algebra diagnostic
- **Research direction:** Intentionally deferred
- **Started:** 2026-08-13

## Learning preferences and prior evidence

- Enjoys homework-style problem solving, hand derivations, symbolic
  manipulation, seeing how equations are built, and small computational
  experiments that support interactive "what if" questions.
- Finds abstract algebra and physics intrinsically motivating; wants a
  protected setting where mathematical depth is the point even when current
  project work does not reward digging deeper.
- Prefers a traditional, cumulative subject sequence with homework and
  internal mathematical coherence. Practical relevance can remain visible,
  but should not be the justification for every topic or determine the pace.
- Previously earned strong grades in undergraduate quantum mechanics. Treat
  this as evidence of prior facility, while using retrieval problems to
  determine what remains operational now.

## Abstract-algebra track

- **Diagnostic:** In progress
- **Strongest existing foundation:** Pending
- **Earliest missing dependency:** Pending
- **First lesson:** Pending

| Lesson | Concept | Status | Mastery evidence | Questions generated |
| --- | --- | --- | --- | --- |
| A0 | Diagnostic boundary | In progress | Prior enjoyment reported; current operational boundary untested | How much group, ring, and field theory remains retrievable? |

## ZK track

- **Diagnostic:** In progress
- **Strongest existing foundation:** Pending
- **Earliest missing dependency:** Pending
- **First lesson:** Pending

| Lesson | Concept | Status | Mastery evidence | Questions generated |
| --- | --- | --- | --- | --- |
| Z0 | Diagnostic boundary | In progress | Pending | Pending |

## Quantum-cryptography track

- **Diagnostic:** In progress
- **Strongest existing foundation:** Pending
- **Earliest missing dependency:** Pending
- **First lesson:** Pending

| Lesson | Concept | Status | Mastery evidence | Questions generated |
| --- | --- | --- | --- | --- |
| Q0 | Diagnostic boundary | In progress | Pending | Pending |

## Bridges

| Bridge | ZK prerequisite | Quantum prerequisite | Status |
| --- | --- | --- | --- |
| B1: Discrete-log boundary | Group encoding and ECDLP | Shor DLP | Locked |
| B2: Groth16 soundness | Groth16 verifier derivation | Shor on G1/G2 | Locked |
| B3: PQ proof systems | Commitment and verifier models | QROM and quantum attacks | Locked |

## Question log

Record questions without converting them prematurely into research directions.

- Why exactly does Shor's discrete-logarithm algorithm destroy Groth16
  soundness?
- Which foundations belong specifically to ZK, specifically to quantum
  cryptography, or genuinely to both?
- Can the components of Groth16 and Poseidon be reconstructed from their
  algebraic design constraints rather than memorized as finished protocols?
- After reproducing existing constructions and attacks, which nearby design
  tradeoff is poorly understood enough to support an original conjecture or
  variant?

## Curriculum observations

Record evidence that may justify changing topic order, lesson size,
prerequisites, examples, or checkpoints.

| Date | Track | Observed signal | Candidate change | Status |
| --- | --- | --- | --- | --- |
| 2026-08-14 | Project | The Shor-to-Groth16 destination may reproduce the utilitarian pressure Ed wants relief from | Use a traditional subject sequence as the spine and treat work relevance or bridge modules as optional connections rather than the reason for learning | Adopted: abstract algebra is the active spine |
| 2026-08-14 | Algebra and ZK | Ed explicitly chose slow, deep abstract algebra leading eventually to independent Groth16 and Poseidon reconstruction and possible original research | Expand the compressed algebra prelude into a traditional algebra course, then branch into Groth16 and algebraic hashes | Adopted |
