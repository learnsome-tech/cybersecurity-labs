# m02l01 · Security Baselines, Policies & Hardening Standards

Module 2: Governance, Risk & Compliance · lesson 2.1 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m02l01)

**Goal:** You can trace a security policy down to a testable baseline, prove what a server really enforces, and put changes to that baseline through version-controlled change management.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l01-03](m02l01-03/) | What the file says versus what sshd enforces | Read along |
| [m02l01-04](m02l01-04/) | Auditing a server against the written standard | Read along |
| [m02l01-06](m02l01-06/) | A standard under version control | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Break and fix the SSH baseline yourself

1. Move the Include line to the end of sshd_config. Predict the audit result, then run audit.py.
2. Add 'maxsessions 5' to ssh_standard.txt. Guess what sshd uses when it is unset, then check.
3. In change.sh, back out CHG-2291 with git revert --no-edit HEAD and read the log again.

> **Hint:** For most keywords sshd keeps the first value it reads, and Include is read where it appears.

## Check yourself

- Why can a grep of sshd_config report a compliant server that still accepts password logins?
- A team wants its nightly baseline audit to fail a pipeline when a server drifts. What does the audit need to compare, and how does it signal failure?
- An engineer needs to lower MaxAuthTries on every server. Which item in the change request would stop a legacy monitoring tool from being locked out?
- A vendor appliance cannot meet the no-password rule. Which exception would an auditor accept?
- Who is accountable for a system and signs off exceptions to its baseline, and who runs the controls day to day?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
