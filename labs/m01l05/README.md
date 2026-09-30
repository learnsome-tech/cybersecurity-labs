# m01l05 · Security Governance vs Security Management

Module 1: Core Security Principles · lesson 1.5 · Free · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m01l05)

**Goal:** You can separate governance decisions from management work, place a document correctly among policy, standard, procedure and guideline, name the governance roles and external obligations, and produce compliance evidence that reflects how a system really behaves.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l05-04](m01l05-04/) | The bastion's sshd_config | Read along |
| [m01l05-05](m01l05-05/) | Checking the standard against real behaviour | Graded |
| [m01l05-07](m01l05-07/) | Auditing the exceptions register | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: fix the evidence, not the paperwork

1. Change the drop-in to PasswordAuthentication no. Predict the checker's output first
2. Rename the drop-in to 99-cloud-init.conf with yes in it. Does the result change? Why?
3. Add the rule permitemptypasswords must be no, leaving it out of both config files
4. Change AS_OF in exceptions.py to 2026-11-01 and predict which new problem appears

> **Hint:** A keyword that appears in neither file falls back to sshd's built-in default, which the checker reports as unset.

## Check yourself

- The board approves a rule that no internet-facing system may accept password logins. Is writing and running the SSH hardening procedure governance or management, and why?
- The main sshd_config says PasswordAuthentication no, yet the checker reported yes. Why, and what would have shown the true value on the server?
- Exception EX-103 still has months to run. Why does the register flag it anyway?
- A company uses a payroll bureau to run its payroll. Which is the data controller, which is the processor, and who decides why the data is collected?
- A standard says MaxAuthTries must be 4 or lower, and a guideline suggests connecting through a jump host. Which one can an auditor raise a finding against, and why?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
