# m04l03-04 · Answering an access request from the database itself

**Lesson:** [Privacy Principles, GDPR Subject Rights & Minimization](https://learnsome.tech/learn/cybersecurity-course/m04l03) (lesson 4.3, module 4: Data Protection & Privacy) · Pro  
**Check:** Graded

## Goal

You can tell a controller from a processor, find everything held about one person, and answer an access or erasure request without breaking another law.

In the lesson: Alice has asked for a copy of everything the shop holds about her. The program loads the schema, then looks up Alice's customer number from her email address. Rather than trusting a list of tables someone typed into a runbook, it asks SQLite for every table in the database and reads each table's columns. Where a table has an email column it matches on that, and otherwise on the customer number. Then it writes the result as J S O N. That single file answers two rights at once: access, which is a copy of the data, and portability, which asks for it in a structured, commonly used, machine readable format. In the output, the orders were found through the customer number, not the email. Six records in total. A search on email alone would have missed two of them.

## Files

- [`starter/sar.py`](starter/sar.py): the listing from the lesson
- [`starter/shop.sql`](starter/shop.sql)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-04/starter`
2. Read `sar.py` the way the lesson builds it:
   - Lines 1–5: looks up Alice's customer number
   - Lines 6–13: asks SQLite for every table
   - Lines 14–17: writes the result as J S O N
3. Run it: `python3 sar.py`.
4. Check it from the repository root: `./check m04l03-04`.

## Expected output

```text
customers: 1 row(s) matched on email
orders: 2 row(s) matched on customer_id
marketing: 1 row(s) matched on email
support_tickets: 2 row(s) matched on email
wrote alice-export.json with 6 records
```

## How to check

`./check m04l03-04` copies `starter/` into a scratch directory and runs `python3 sar.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
