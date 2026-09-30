# m03l05-03 · Post-quantum signatures and what they weigh

**Lesson:** [Post-Quantum Cryptography & Key Lifecycles](https://learnsome.tech/learn/cybersecurity-course/m03l05) (lesson 3.5, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Runs, not graded

## Goal

You can explain what a quantum computer would break, run ML-KEM and ML-DSA and weigh their sizes, plan a hybrid migration, and rotate keys with envelope encryption.

In the lesson: Signatures change too, and here the size difference is far larger. The script signs a firmware file with three algorithms: Ed twenty five five one nine from the asymmetric lesson, M L D S A sixty five, a lattice scheme from FIPS two hundred and four, and S L H D S A, a hash based scheme from FIPS two hundred and five. The loop signs, then verifies each one with only the public key. Run it and read the three lines. All three verify. Ed twenty five five one nine needs sixty four bytes of signature. M L D S A needs over three thousand, with a public key near two thousand bytes. S L H D S A has a tiny public key but a signature near eight thousand bytes; its security rests only on the hash function, which makes it the conservative backup. For firmware signed once, fine. For every certificate in every T L S handshake, those bytes add up.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/pqsign.sh`](starter/pqsign.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-03/starter`
2. Read `pqsign.sh` the way the lesson builds it:
   - Lines 1–4: signs a firmware file with three algorithms
   - Lines 5–15: the loop signs, then verifies
3. Run it: `bash pqsign.sh`.
4. Check it from the repository root: `./check m03l05-03`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
ED25519: public key 44 bytes, signature 64 bytes, verifies
ML-DSA-65: public key 1974 bytes, signature 3309 bytes, verifies
SLH-DSA-SHA2-128s: public key 50 bytes, signature 7856 bytes, verifies
```

## How to check

`./check m03l05-03` copies `starter/` into a scratch directory and runs `bash pqsign.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
