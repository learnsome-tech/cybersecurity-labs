# m05l02-03 · Synchronous versus asynchronous replication

**Lesson:** [Disaster Recovery Sites: Hot, Warm & Cold](https://learnsome.tech/learn/cybersecurity-course/m05l02) (lesson 5.2, module 5: Resilience & Disaster Recovery) · Pro  
**Check:** Graded

## Goal

You can choose between hot, warm and cold recovery sites by working out their real recovery time and data loss against a system's RTO and RPO, and plan how to test the choice.

In the lesson: A hot site is only as current as its replication, and there are two ways to keep a copy in step. This program makes three SQLite databases: the primary and two replicas. The ship function copies any rows a replica has not seen yet, which is the idea behind log shipping written in a few lines of Python. Orders arrive every two minutes. The synchronous replica receives every order before the customer is told it has been paid, so the two never disagree. The asynchronous replica gets a batch every fifteen minutes. The primary fails at fourteen thirty seven. The synchronous copy holds all one hundred and sixty nine orders. The asynchronous copy stops at fourteen thirty, three orders short. That is the rule to remember: asynchronous replication has an R P O equal to its lag.

## Files

- [`starter/replicate.py`](starter/replicate.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-03/starter`
2. Read `replicate.py` the way the lesson builds it:
   - Lines 1–7: makes three SQLite databases
   - Lines 8–12: the ship function
   - Lines 13–15: orders arrive every two minutes
   - Lines 16–20: the synchronous replica receives
   - Lines 21–22: the primary fails
3. Run it: `python3 replicate.py`.
4. Check it from the repository root: `./check m05l02-03`.

## Expected output

```text
primary (169, '2026-03-09T14:36:00')
sync (169, '2026-03-09T14:36:00')
async (166, '2026-03-09T14:30:00')
```

## How to check

`./check m05l02-03` copies `starter/` into a scratch directory and runs `python3 replicate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
