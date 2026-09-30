# m04l01-04 · Stamp a label, copy the file, read it back

**Lesson:** [Data Classification Schemes & Sensitivity Labeling](https://learnsome.tech/learn/cybersecurity-course/m04l01) (lesson 4.1, module 4: Data Protection & Privacy) · Pro  
**Check:** Graded

## Goal

You can choose a classification label for a dataset, store it where it survives copying, and enforce it where data is shared or stored.

In the lesson: Here is a short Python program that treats the file the way a labelling client or a scanner does. The stamp function writes that X M L into a zip, which is all a docx really is, swapping in whichever label name we ask for. The read label function opens the zip, parses the custom properties part, and returns the value of the property whose name starts with M S I P label and ends in name. At the bottom we stamp a pricing document as confidential, copy it under a new name as if someone were getting it ready for a partner, and read both. The output shows the copy still says confidential. The folder, the file name and the person holding it made no difference. That is the property you want from a label: it follows the bytes wherever they go.

## Files

- [`starter/custom.xml`](starter/custom.xml)
- [`starter/labels.py`](starter/labels.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-04/starter`
2. Read `labels.py` the way the lesson builds it:
   - Lines 1–4: a short Python program
   - Lines 5–9: The stamp function
   - Lines 10–17: The read label function
   - Lines 18–22: At the bottom
3. Run it: `python3 labels.py`.
4. Check it from the repository root: `./check m04l01-04`.

## Expected output

```text
pricing-2027.docx is labelled Confidential
copy-for-partner.docx is labelled Confidential
```

## How to check

`./check m04l01-04` copies `starter/` into a scratch directory and runs `python3 labels.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
