# m01l05-07 · Auditing the exceptions register

**Lesson:** [Security Governance vs Security Management](https://learnsome.tech/learn/cybersecurity-course/m01l05) (lesson 1.5, module 1: Core Security Principles) · Free  
**Check:** Graded

## Goal

You can separate governance decisions from management work, place a document correctly among policy, standard, procedure and guideline, name the governance roles and external obligations, and produce compliance evidence that reflects how a system really behaves.

In the lesson: Exceptions are where governance and management meet. When a system cannot meet a standard, someone records an exception, and the governance rule says who may accept the risk and for how long. The program reads the register as of a fixed date, so the report can be reproduced. The table says who may accept each level of risk: only the C I S O or the risk committee for high. For each exception, it first checks the approver, then the expiry: past, or more than a year out. Four of the five need attention. One expired in June. One has no approver at all. One runs for more than a year. And the password login on the bastion, the very finding from the last check, was waved through by an I T manager who cannot accept a high risk.

## Files

- [`starter/exceptions.csv`](starter/exceptions.csv)
- [`starter/exceptions.py`](starter/exceptions.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-07/starter`
2. Read `exceptions.py` the way the lesson builds it:
   - Lines 1–4: fixed date
   - Lines 5–6: The table says
   - Lines 7–13: approver
   - Lines 14–19: expiry
3. Run it: `python3 exceptions.py`.
4. Check it from the repository root: `./check m01l05-07`.

## Expected output

```text
EX-101 payroll-legacy  ok
EX-102 lab-laptop-07   expired on 2026-06-30
EX-103 bastion01       IT manager cannot accept high risk
EX-104 portal          nobody approved it
EX-105 scanner-02      longer than the one year maximum
```

## How to check

`./check m01l05-07` copies `starter/` into a scratch directory and runs `python3 exceptions.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
