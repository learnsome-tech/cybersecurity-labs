# m02l03-04 · One crosswalk, three frameworks, four gaps

**Lesson:** [Security Frameworks: NIST CSF 2.0, ISO 27001 & CIS](https://learnsome.tech/learn/cybersecurity-course/m02l03) (lesson 2.3, module 2: Governance, Risk & Compliance) · Pro  
**Check:** Graded

## Goal

You can explain how NIST CSF 2.0, ISO 27001 and the CIS Controls differ, use a crosswalk to find evidence gaps across all three, and test a Kubernetes pod against the restricted Pod Security Standard.

In the lesson: Most companies answer to more than one framework, so they keep a crosswalk: a table of which requirement in one lines up with which in another. This is a small crosswalk written for this lesson, not an official mapping. Each row ties a C S F subcategory to an ISO Annex A control and a C I S safeguard. Beside it is the evidence log: which artefact was collected, and when. The program fixes the audit date and a maximum age of one year, because auditors reject stale evidence. The status function returns ok, no evidence, or evidence too old. Then the loop prints every gap with its references, and a score per function. Run it. Four gaps. Training records are over a year old, and nothing proves backups, network monitoring, or that backups are checked before a restore. Meanwhile one hardware inventory export satisfies three frameworks at once.

## Files

- [`starter/crosswalk.csv`](starter/crosswalk.csv)
- [`starter/crosswalk.py`](starter/crosswalk.py): the listing from the lesson
- [`starter/evidence.csv`](starter/evidence.csv)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-04/starter`
2. Read `crosswalk.py` the way the lesson builds it:
   - Lines 1–7: fixes the audit date
   - Lines 8–13: the status function
   - Lines 14–22: the loop prints every gap
3. Run it: `python3 crosswalk.py`.
4. Check it from the repository root: `./check m02l03-04`.

## Expected output

```text
PR.DS-11  no evidence      ISO A.8.13  CIS 11.2
PR.AT-01  evidence too old ISO A.6.3   CIS 14.1
DE.CM-01  no evidence      ISO A.8.16  CIS 13.1
RC.RP-03  no evidence      ISO A.8.13  CIS 11.5
GV 1/1  ID 2/2  PR 2/4  DE 0/1  RS 1/1  RC 0/1
```

## How to check

`./check m02l03-04` copies `starter/` into a scratch directory and runs `python3 crosswalk.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
