# m04l03-06 · Erasure, legal holds and retention sweeps

**Lesson:** [Privacy Principles, GDPR Subject Rights & Minimization](https://learnsome.tech/learn/cybersecurity-course/m04l03) (lesson 4.3, module 4: Data Protection & Privacy) · Pro  
**Check:** Graded

## Goal

You can tell a controller from a processor, find everything held about one person, and answer an access or erasure request without breaking another law.

In the lesson: Erasure is not a single delete statement. This program prints row counts at each step. Alice now asks to be forgotten. Her marketing record and support tickets go, and her account row is stripped of her name and email. Her orders stay, because erasure does not apply when you need the data to meet a legal obligation, and tax law requires those records. Tell her so in your reply; keeping data silently is the failure. The retention sweep comes next, and it applies to every customer, requested or not. Using a fixed date so the output repeats, it deletes tickets closed more than two years ago and orders older than six years. In the output, the sweep removes Ben's old support ticket and two orders from twenty nineteen and twenty twenty, one of them Alice's. Her remaining order is kept for the tax years still open.

## Files

- [`starter/erase.py`](starter/erase.py): the listing from the lesson
- [`starter/shop.sql`](starter/shop.sql)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-06/starter`
2. Read `erase.py` the way the lesson builds it:
   - Lines 1–9: prints row counts
   - Lines 10–14: Alice now asks to be forgotten
   - Lines 15–20: retention sweep
   - Lines 21–22: her remaining order
3. Run it: `python3 erase.py`.
4. Check it from the repository root: `./check m04l03-06`.

## Expected output

```text
before     {'customers': 3, 'orders': 5, 'marketing': 2, 'support_tickets': 3}
erasure    {'customers': 3, 'orders': 5, 'marketing': 1, 'support_tickets': 1}
retention  {'customers': 3, 'orders': 3, 'marketing': 1, 'support_tickets': 0}
alice's orders kept: [(2, 1, 1250, '2025-12-03')]
```

## How to check

`./check m04l03-06` copies `starter/` into a scratch directory and runs `python3 erase.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
