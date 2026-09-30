# m04l04-05 · Deleting a record is not sanitising it

**Lesson:** [Asset Lifecycle Management & Media Sanitization](https://learnsome.tech/learn/cybersecurity-course/m04l04) (lesson 4.4, module 4: Data Protection & Privacy) · Pro  
**Check:** Graded

## Goal

You can reconcile an asset inventory against what is really on the network and pick a sanitisation method that matches the media and the data on it.

In the lesson: Deletion leaves data behind at every layer, and SQLite shows it in a few lines. The helper reads the raw bytes of a database file and checks whether some text is in there. The loop builds two H R databases, one with SQLite's secure delete setting off, which is the usual default, and one with it on. Each stores a disciplinary note, commits, then deletes it and commits again. Then the program counts the rows through S Q L and inspects the file. With secure delete off, the query sees nothing, yet the note is still sitting in the file, because SQLite only marks the space as free. With it on, the space is overwritten with zeros. File systems behave the same way: deleting a file removes its directory entry and leaves the blocks for anyone with a recovery tool.

## Files

- [`starter/delete.py`](starter/delete.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-05/starter`
2. Read `delete.py` the way the lesson builds it:
   - Lines 1–4: reads the raw bytes
   - Lines 5–14: then deletes it
   - Lines 15–18: counts the rows
3. Run it: `python3 delete.py`.
4. Check it from the repository root: `./check m04l04-05`.

## Expected output

```text
secure_delete OFF: rows visible 0, note still in file: True
secure_delete ON: rows visible 0, note still in file: False
```

## How to check

`./check m04l04-05` copies `starter/` into a scratch directory and runs `python3 delete.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
