# m05l01-03 · Checking the targets against real restore times

**Lesson:** [Business Impact Analysis, RTO & RPO Modeling](https://learnsome.tech/learn/cybersecurity-course/m05l01) (lesson 5.1, module 5: Resilience & Disaster Recovery) · Pro  
**Check:** Graded

## Goal

You can turn a business impact analysis into RTO and RPO targets, test them against real restore times and backup schedules, and work out what redundancy does to availability.

In the lesson: This program reads the worksheet with Python's C S V module, then puts the processes in dependency order using graphlib from the standard library. For each process it works out the R T O as maximum tolerable downtime minus work recovery time. A process cannot start restoring until everything it depends on is back, so its ready time is its own restore plus the slowest dependency. Last, it compares the backup interval with the R P O, because the worst case loss is a failure just before the next backup runs. Now read the checkout lines. Checkout restores in two hours on its own, yet it is ready only after seven, an hour past its target. Identity and checkout are also backed up daily against much tighter R P O targets.

## Files

- [`starter/bia.csv`](starter/bia.csv)
- [`starter/bia_gaps.py`](starter/bia_gaps.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-03/starter`
2. Read `bia_gaps.py` the way the lesson builds it:
   - Lines 1–6: reads the worksheet
   - Lines 7–10: minus work recovery time
   - Lines 11–12: the slowest dependency
   - Lines 13–18: compares the backup interval
3. Notes from the lesson:
   - Line 11: a process waits for everything it depends on
4. Run it: `python3 bia_gaps.py`.
5. Check it from the repository root: `./check m05l01-03`.

## Expected output

```text
identity: RTO 3h, ready after 3h ok
identity: RPO 4h, backup every 24h could lose 24h of data
payments: RTO 5h, ready after 5h ok
payments: RPO 1h, backup every 1h ok
payroll: RTO 64h, ready after 23h ok
payroll: RPO 24h, backup every 24h ok
checkout: RTO 6h, ready after 7h late by 1h
checkout: RPO 1h, backup every 24h could lose 24h of data
```

## How to check

`./check m05l01-03` copies `starter/` into a scratch directory and runs `python3 bia_gaps.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
