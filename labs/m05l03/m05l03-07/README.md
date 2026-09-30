# m05l03-07 · Zero errors: proving a restore is intact

**Lesson:** [Backup Architectures: 3-2-1, Immutability & Air-Gaps](https://learnsome.tech/learn/cybersecurity-course/m05l03) (lesson 5.3, module 5: Resilience & Disaster Recovery) · Pro  
**Check:** Graded

## Goal

You can design a backup scheme that survives ransomware, explaining incremental and differential chains, 3-2-1-1-0, immutability and air gaps, and prove a restore is intact.

In the lesson: The zero in three, two, one, one, zero means a restore that has been checked, not assumed. At backup time this program records a S H A two five six digest for every file, using the file digest helper in hashlib, and writes them to a manifest that travels with the offline copy. Then something changes one file after the backup: a failing disk, or an attacker who wants you to restore their version. The restore test recomputes each digest and compares. The notes file matches. The ledger differs, and the short prefixes show the two digests. A manifest is only trustworthy if it sits where the attacker cannot rewrite it, otherwise they update the digests too. And hashes prove the bytes, not that the application starts, so schedule real test restores as well.

## Files

- [`starter/verify.py`](starter/verify.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-07/starter`
2. Read `verify.py` the way the lesson builds it:
   - Lines 1–5: records a S H A two five six digest
   - Lines 6–15: writes them to a manifest
   - Lines 16–18: something changes one file
   - Lines 19–21: the restore test recomputes
3. Run it: `python3 verify.py`.
4. Check it from the repository root: `./check m05l03-07`.

## Expected output

```text
ledger.csv differs: 8f7a3e49c2b8 vs 4f131448eaba
notes.txt ok
```

## How to check

`./check m05l03-07` copies `starter/` into a scratch directory and runs `python3 verify.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
