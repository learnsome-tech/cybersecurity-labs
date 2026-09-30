# m05l01-04 · Watching an RPO happen to real data

**Lesson:** [Business Impact Analysis, RTO & RPO Modeling](https://learnsome.tech/learn/cybersecurity-course/m05l01) (lesson 5.1, module 5: Resilience & Disaster Recovery) · Pro  
**Check:** Graded

## Goal

You can turn a business impact analysis into RTO and RPO targets, test them against real restore times and backup schedules, and work out what redundancy does to availability.

In the lesson: Numbers in a spreadsheet are easy to ignore, so here is an R P O happening to real data. At the top are two facts: backups run every four hours, and the disk controller dies at five thirty seven in the morning. The program builds a SQLite orders table in memory, then takes an order every three minutes from midnight. On each four hour boundary it copies the live database with SQLite's online backup A P I, a call that gives a consistent copy of a database while it is in use. When the failure hits, only that copy survives. The last backup was at four, so an hour and thirty seven minutes of orders exist nowhere except in customer inboxes: thirty three orders to chase by hand. Fail at three fifty nine instead and nearly four hours are gone.

## Files

- [`starter/rpo_demo.py`](starter/rpo_demo.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-04/starter`
2. Read `rpo_demo.py` the way the lesson builds it:
   - Lines 1–5: two facts
   - Lines 6–8: builds a SQLite orders table
   - Lines 9–16: takes an order every three minutes
   - Lines 17–22: when the failure hits
3. Run it: `python3 rpo_demo.py`.
4. Check it from the repository root: `./check m05l01-04`.

## Expected output

```text
last backup 04:00, failure 05:37, gap 1:37:00
orders taken 113, in the backup 80, newest 03:57
orders that exist nowhere now: 33
```

## How to check

`./check m05l01-04` copies `starter/` into a scratch directory and runs `python3 rpo_demo.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
