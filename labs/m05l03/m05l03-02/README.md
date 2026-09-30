# m05l03-02 · Full, incremental and differential

**Lesson:** [Backup Architectures: 3-2-1, Immutability & Air-Gaps](https://learnsome.tech/learn/cybersecurity-course/m05l03) (lesson 5.3, module 5: Resilience & Disaster Recovery) · Pro  
**Check:** Graded

## Goal

You can design a backup scheme that survives ransomware, explaining incremental and differential chains, 3-2-1-1-0, immutability and air gaps, and prove a restore is intact.

In the lesson: Before protecting backups, be clear what each night's backup holds. The at function turns a day in a fixed March week into a timestamp, so the result never depends on this machine's clock. The archive function writes a real tar file of every file modified after a given moment, then reads the archive back to list what went in. The edits say which files change on which day. Each night the loop takes an incremental, meaning changes since the previous night's backup of any kind, and a differential, meaning changes since Monday's full backup. On Monday both are full. Read Thursday. The incremental holds two files, so it is quick to write, but a Thursday restore needs the full plus three incrementals, and one broken link loses every change after it. The differential has grown to three files, yet a restore needs only the full and that one differential.

## Files

- [`starter/backup_types.py`](starter/backup_types.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-02/starter`
2. Read `backup_types.py` the way the lesson builds it:
   - Lines 1–5: the at function
   - Lines 6–12: the archive function
   - Lines 13–15: the edits say
   - Lines 16–22: each night the loop
3. Notes from the lesson:
   - Line 20: incremental: changed since the previous night
   - Line 21: differential: changed since Monday's full backup
4. Run it: `python3 backup_types.py`.
5. Check it from the repository root: `./check m05l03-02`.

## Expected output

```text
Mar  9  inc ledger.csv logo.png notes.txt  diff ledger.csv logo.png notes.txt
Mar 10  inc ledger.csv                     diff ledger.csv
Mar 11  inc notes.txt                      diff ledger.csv notes.txt
Mar 12  inc ledger.csv plan.txt            diff ledger.csv notes.txt plan.txt
```

## How to check

`./check m05l03-02` copies `starter/` into a scratch directory and runs `python3 backup_types.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
