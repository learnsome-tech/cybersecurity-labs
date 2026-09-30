# m04l05-04 · Exact data match: fingerprints of your own records

**Lesson:** [Data Loss Prevention & Egress Monitoring](https://learnsome.tech/learn/cybersecurity-course/m04l05) (lesson 4.5, module 4: Data Protection & Privacy) · Pro  
**Check:** Graded

## Goal

You can explain how a DLP rule decides that outbound content is sensitive, tune it against false positives, and spot bulk exfiltration in connection logs.

In the lesson: Patterns find anything shaped like sensitive data. Exact data match finds your data. The fingerprint function normalises a value, trimming punctuation and lower casing it, then hashes it. The program builds the index from the customer table, keeping only fingerprints, so the D L P server never holds the raw values. Commercial products add a secret salt so the fingerprints cannot be guessed back. Each outgoing message is split into tokens, and every token is fingerprinted and looked up. The policy blocks a message when two or more fields of the same customer appear together, alerts on one, and allows the rest. So the partner chat is blocked, because it holds Tom's phone number and email. The newsletter address is not a customer, so it passes. The support reply gets an alert, and the pasted C S V row is blocked.

## Files

- [`starter/customers.csv`](starter/customers.csv)
- [`starter/edm.py`](starter/edm.py): the listing from the lesson
- [`starter/outgoing.txt`](starter/outgoing.txt)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-04/starter`
2. Read `edm.py` the way the lesson builds it:
   - Lines 1–5: normalises a value
   - Lines 6–10: builds the index
   - Lines 11–18: Each outgoing message
   - Lines 19–21: two or more fields
3. Run it: `python3 edm.py`.
4. Check it from the repository root: `./check m04l05-04`.

## Expected output

```text
partner-chat   block  {'1002': ['phone', 'email']}
newsletter     allow  no customer data
support-reply  alert  {'1001': ['email']}
upload         block  {'1001': ['email', 'phone', 'ni_number']}
```

## How to check

`./check m04l05-04` copies `starter/` into a scratch directory and runs `python3 edm.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
