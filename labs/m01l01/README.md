# m01l01 · CIA Triad, Non-Repudiation & Parkerian Hexad

Module 1: Core Security Principles · lesson 1.1 · Free · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m01l01)

**Goal:** You can name which security property an incident broke, show why a shared key cannot give non-repudiation while a signature can, and trace identification, authentication, authorisation and accountability through a real auth.log.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l01-02](m01l01-02/) | A hash spots change; only a key spots a forger | Graded |
| [m01l01-03](m01l01-03/) | A signature gives you non-repudiation | Graded |
| [m01l01-05](m01l01-05/) | Reading the four steps in a real auth.log | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: break and repair the proofs

1. In tags.py, set the attacker's key to KEY. Predict the three lines, then run it
2. Add an auth.log line where bob's sudo is allowed; check the output says authz allowed
3. In sign.sh, make a second key pair and verify Alice's order with it. Predict the result
4. Change SHARED to an empty set and explain what the output no longer tells you

> **Hint:** Copy the genpkey and pkey lines with new file names for the second pair, then pass that public key to the first verify command.

## Check yourself

- A bank and a customer share one HMAC key. Why can a valid tag not prove to a court that the customer sent the order?
- An encrypted backup tape falls off a courier's van and is never found. Using the Parkerian hexad, which property did you lose, and why does it still need action?
- In the auth.log demo, bob logged in with his key but his sudo command was refused. Which step of IAAA stopped him, and which log line proves it?
- Every login to the shared deploy account is logged. Why does that account still break accountability and non-repudiation?
- Why is any use of a honeytoken credential treated as a high-confidence alert, when a failed login on a real account is not?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
