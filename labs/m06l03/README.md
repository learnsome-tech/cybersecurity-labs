# m06l03 · Internal Audits, Sampling & Evidence Chains

Module 6: Enterprise Strategy & Audit · lesson 6.3 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m06l03)

**Goal:** You can draw a repeatable audit sample from a complete population, test it against a control statement, seal the evidence with hashes, and write up the finding.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l03-03](m06l03-03/) | The population: change tickets for the period | Read along |
| [m06l03-04](m06l03-04/) | Drawing a sample anyone can repeat | Graded |
| [m06l03-05](m06l03-05/) | Testing each sampled change against the policy | Graded |
| [m06l03-06](m06l03-06/) | Sealing the evidence so tampering shows | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Reperform and stress the audit

1. Test every ticket in the period instead of the sample. Predict the exception count first.
2. Change SEED, draw a new sample, and note whether the conclusion would have changed.
3. Edit one character in sample.txt, then run sha256sum -c manifest.sha256. Which line fails?

> **Hint:** Build the set from rows whose implemented_at falls in the period instead of reading sample.txt.

## Check yourself

- The change policy lets engineers approve their own changes. Why does that fail the design test before any ticket is sampled?
- Why are the seed and the population file hash recorded before the sample is drawn?
- Which line of the seal script's output proves results.csv changed after testing, and why does the manifest's own hash live in the audit ticket?
- After two exceptions, a manager asks you to test ten more tickets to bring the rate down. Why is that wrong?
- What does a SOC 2 Type 2 report tell a customer that a Type 1 report does not?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
