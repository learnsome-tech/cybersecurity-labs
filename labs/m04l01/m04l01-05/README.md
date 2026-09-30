# m04l01-05 · A sharing gate that reads the label

**Lesson:** [Data Classification Schemes & Sensitivity Labeling](https://learnsome.tech/learn/cybersecurity-course/m04l01) (lesson 4.1, module 4: Data Protection & Privacy) · Pro  
**Check:** Graded

## Goal

You can choose a classification label for a dataset, store it where it survives copying, and enforce it where data is shared or stored.

In the lesson: Labels earn their keep when something enforces them. This gate sits where files leave, such as an upload service, and it imports the reader from the last listing. The rules table gives each label two answers: may it leave the company, and which storage regions may hold it. Confidential and restricted are pinned to European regions. That is data sovereignty in practice: data is subject to the laws of the country where it is stored, so a regulator or a customer contract can require records to stay in the E U. The decide function reads the label from the file itself, and an unknown label gets no regions at all, so the gate fails closed. Four requests go through, each saying whether the file is being shared outside the company or only stored internally, and in which region. The brochure leaves freely. Pricing may be stored in Ireland but not in Virginia. The board minutes are refused before the region is even checked.

## Files

- [`starter/custom.xml`](starter/custom.xml)
- [`starter/gate.py`](starter/gate.py): the listing from the lesson
- [`starter/labels.py`](starter/labels.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-05/starter`
2. Read `gate.py` the way the lesson builds it:
   - Lines 1: imports the reader
   - Lines 2–5: The rules table
   - Lines 6–14: The decide function
   - Lines 15–22: Four requests go through
3. Run it: `python3 gate.py`.
4. Check it from the repository root: `./check m04l01-05`.

## Expected output

```text
brochure.docx external us-east-1 Public allow
pricing.docx internal eu-west-1 Confidential allow
pricing.docx internal us-east-1 Confidential block: us-east-1 not allowed for Confidential
board-minutes.docx external eu-central-1 Restricted block: label forbids external sharing
```

## How to check

`./check m04l01-05` copies `starter/` into a scratch directory and runs `python3 gate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
