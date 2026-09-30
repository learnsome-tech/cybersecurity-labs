# m06l04-03 · Measuring the real recovery point from backups

**Lesson:** [Security Capstone Review & Certification](https://learnsome.tech/learn/cybersecurity-course/m06l04) (lesson 6.4, module 6: Enterprise Strategy & Audit) · Pro  
**Check:** Graded

## Goal

You can gather certificate and backup evidence, test it against written targets, turn the gaps into owned register entries, and choose a sensible next certification.

In the lesson: Now availability. The business impact analysis set a recovery point objective of twenty four hours for the bookings database: losing up to a day of bookings is survivable, more is not. The database team saves the output of restic snapshots with the json flag, which lists every backup with its timestamp. The program trims each timestamp to the minute, sorts them, and adds the review time at the end, because data written since the last backup is also at risk. Then it measures every gap between neighbouring snapshots. Run it. Nine snapshots, but none for three nights, from the twenty third to the twenty sixth. Had the database been lost late on the twenty fifth, nearly three days of bookings would have gone. Then ask why nobody noticed. A backup job that fails silently is the deeper finding.

## Files

- [`starter/backup_rpo.py`](starter/backup_rpo.py): the listing from the lesson
- [`starter/snapshots.json`](starter/snapshots.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l04/m06l04-03/starter`
2. Read `backup_rpo.py` the way the lesson builds it:
   - Lines 1–5: set a recovery point objective of twenty four hours
   - Lines 6–11: adds the review time at the end
   - Lines 12–21: measures every gap between neighbouring snapshots
3. Notes from the lesson:
   - Line 11: Data written since the last snapshot is at risk too
4. Run it: `python3 backup_rpo.py`.
5. Check it from the repository root: `./check m06l04-03`.

## Expected output

```text
snapshots: 9 from 2026-09-20 to 2026-09-30
2026-09-23 01:00 to 2026-09-26 01:00: 3 days, 0:00:00
worst case data loss: 3 days, 0:00:00 against an RPO of 1 day, 0:00:00
PR.DS-11 backups: gap
```

## How to check

`./check m06l04-03` copies `starter/` into a scratch directory and runs `python3 backup_rpo.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
