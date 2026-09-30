# m02l01-06 · A standard under version control

**Lesson:** [Security Baselines, Policies & Hardening Standards](https://learnsome.tech/learn/cybersecurity-course/m02l01) (lesson 2.1, module 2: Governance, Risk & Compliance) · Pro  
**Check:** Graded

## Goal

You can trace a security policy down to a testable baseline, prove what a server really enforces, and put changes to that baseline through version-controlled change management.

In the lesson: Here is the standard kept in git, which is how most teams hold baselines as code. The first lines pin the author, the dates and the configuration, so the commit hashes are the same every time you run it. We commit the approved version three, with the CAB reference in the message. Then an approved change: lower the attempt limit from four to three. The change record number goes in the commit message, so the ticket and the edit point at each other. The backout plan is a git revert, which records the undo as its own commit rather than rewriting history. Now read the log and the diff. You get who, when, why, and exactly which line moved. That is the evidence an auditor asks for when they sample a change.

## Files

- [`starter/change.sh`](starter/change.sh): the listing from the lesson
- [`starter/command.txt`](starter/command.txt)
- [`starter/ssh_standard.txt`](starter/ssh_standard.txt)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-06/starter`
2. Read `change.sh` the way the lesson builds it:
   - Lines 1–6: the approved version three
   - Lines 7–12: approved change
   - Lines 13–15: the log and the diff
3. Run it: `bash change.sh`.
4. Check it from the repository root: `./check m02l01-06`.

## Expected output

```text
226c31d 2026-03-05 Priya Shah: Lower maxauthtries to 3 (CHG-2291)
50358c6 2026-02-10 Priya Shah: SSH standard v3 (CAB-118)
-maxauthtries 4
+maxauthtries 3
```

## How to check

`./check m02l01-06` copies `starter/` into a scratch directory and runs `bash change.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
