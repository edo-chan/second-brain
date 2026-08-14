# Two-Track Diagnostic

The diagnostics select two independent starting points: one for
zero-knowledge proof systems and one for quantum cryptography. They do not
assume the tracks are equally advanced.

## Step 1: Confidence maps

Complete both confidence maps without references:

1. [ZK confidence map](zk/diagnostic.md#confidence-map)
2. [Quantum confidence map](quantum-cryptography/diagnostic.md#confidence-map)

Use the same scale in both:

- **0 - New:** I have not studied it.
- **1 - Familiar:** I recognize the terms.
- **2 - Usable:** I can solve standard exercises with references.
- **3 - Operational:** I can derive and explain it without references.
- **4 - Fluent:** I can implement it, prove the relevant claims, or teach it.

## Step 2: Adaptive probes

After reviewing the confidence maps, answer only the selected probes from each
track. Approximately three to five probes per track should locate the real
boundary.

## Step 3: Starting lessons

Record these results in [progress.md](progress.md):

- strongest existing foundation in each track;
- earliest missing dependency in each track;
- first ZK lesson;
- first quantum-cryptography lesson;
- whether the tracks should alternate evenly or one should temporarily lead.

## Initial response format

```text
ZK ratings:
Z1:
Z2:
Z3:
Z4:
Z5:
Z6:
Z7:
Z8:
Z9:
Z10:
Z11:
Z12:

Quantum ratings:
Q1:
Q2:
Q3:
Q4:
Q5:
Q6:
Q7:
Q8:
Q9:
Q10:
Q11:
Q12:

Preferred learning modes:
Sustainable session size:
Preferred experiment tools:
```
