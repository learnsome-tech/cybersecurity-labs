# m05l03-04 · Read-only is not immutable

**Lesson:** [Backup Architectures: 3-2-1, Immutability & Air-Gaps](https://learnsome.tech/learn/cybersecurity-course/m05l03) (lesson 5.3, module 5: Resilience & Disaster Recovery) · Pro  
**Check:** Graded

## Goal

You can design a backup scheme that survives ransomware, explaining incremental and differential chains, 3-2-1-1-0, immutability and air gaps, and prove a restore is intact.

In the lesson: Now the attacker. Ransomware operators go after backups first, because a company that can restore has less reason to pay. A common defence is marking backup files read only. This program writes a backup file and sets its mode to four four four, read only for everyone. Then it plays the attacker, running under the same account as the backup job. Overwriting the file is refused, as expected. But the attacker reads it, writes a scrambled copy beside it as a stand in for real encryption, and deletes the original. The only file left is the locked one. On Unix, deleting a file needs write permission on the folder, not on the file, and the owner could have changed the mode back anyway. Anything the same credentials can undo is not immutability.

## Files

- [`starter/readonly.py`](starter/readonly.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-04/starter`
2. Read `readonly.py` the way the lesson builds it:
   - Lines 1–8: sets its mode to four four four
   - Lines 9–14: overwriting the file is refused
   - Lines 15–19: writes a scrambled copy
3. Notes from the lesson:
   - Line 18: deleting needs write access to the folder, not the file
4. Run it: `python3 readonly.py`.
5. Check it from the repository root: `./check m05l03-04`.

## Expected output

```text
backups/ledger-2026-03-12.csv -r--r--r--
overwrite refused: Permission denied
left in backups: ['ledger-2026-03-12.csv.locked']
```

## How to check

`./check m05l03-04` copies `starter/` into a scratch directory and runs `python3 readonly.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
