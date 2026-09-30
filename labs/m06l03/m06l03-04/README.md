# m06l03-04 · Drawing a sample anyone can repeat

**Lesson:** [Internal Audits, Sampling & Evidence Chains](https://learnsome.tech/learn/cybersecurity-course/m06l03) (lesson 6.3, module 6: Enterprise Strategy & Audit) · Pro  
**Check:** Graded

## Goal

You can draw a repeatable audit sample from a complete population, test it against a control statement, seal the evidence with hashes, and write up the finding.

In the lesson: Sampling is fair when you choose tickets without looking at them first, and useful when anyone can repeat your choice. So the seed is fixed and written down before sampling, and the audit period is set at the top. Next, the script hashes the export exactly as received, keeps only changes implemented inside the period, and draws fifteen of them with Python's random module seeded with that number. Fifteen comes from our audit method, not from a law of nature. Run it. The file holds fifty rows, forty five of them in the period. Anyone with this file, this hash and this seed will draw the same fifteen tickets, which is what lets a reviewer reperform your work.

## Files

- [`starter/changes.csv`](starter/changes.csv)
- [`starter/sample.py`](starter/sample.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-04/starter`
2. Read `sample.py` the way the lesson builds it:
   - Lines 1–6: the audit period is set at the top
   - Lines 7–11: the script hashes the export exactly as received
   - Lines 12–14: draws fifteen of them
   - Lines 15–21: run it
3. Notes from the lesson:
   - Line 5: Pick the seed before seeing the data, and record it in the workpaper
4. Run it: `python3 sample.py`.
5. Check it from the repository root: `./check m06l03-04`.

## Expected output

```text
population file sha256:
f1691a99e1b080e3d15d1358329688ec4109f181037e4c3b3332213134a0473c
rows in file: 50 in period: 45
seed: 20260930 sample size: 15
CHG-1005 CHG-1006 CHG-1007 CHG-1018 CHG-1019
CHG-1021 CHG-1023 CHG-1029 CHG-1030 CHG-1031
CHG-1033 CHG-1036 CHG-1041 CHG-1044 CHG-1048
```

## How to check

`./check m06l03-04` copies `starter/` into a scratch directory and runs `python3 sample.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
