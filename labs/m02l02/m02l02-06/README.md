# m02l02-06 · A key risk indicator against its tolerance line

**Lesson:** [Risk Assessment: Qualitative vs Quantitative](https://learnsome.tech/learn/cybersecurity-course/m02l02) (lesson 2.2, module 2: Governance, Risk & Compliance) · Pro  
**Check:** Graded

## Goal

You can score risks on a likelihood and impact matrix, calculate SLE, ARO and ALE to compare a risk with the cost of treating it, and track a key risk indicator against tolerance.

In the lesson: Tolerance only means something if you measure it. A key risk indicator is a number that moves before the loss happens. Here it is the share of internet-facing hosts with a critical patch outstanding for more than fourteen days, taken from a patch export. The grace period and the thresholds sit at the top, where the risk committee can read and change them. The overdue function decides whether one patch on one host was late on a given day. Then the loop evaluates each month end. Run it. January is green. February turns amber because of one V P N gateway. March is red: three hosts out of ten, beyond the tolerance line. That row is what belongs on a dashboard or board scorecard, and red is what triggers escalation to the risk owner. Risk reports to the board are built from rows like these: the top risks, their trend, and which ones sit outside tolerance.

## Files

- [`starter/internet_facing_patches.csv`](starter/internet_facing_patches.csv)
- [`starter/kri.py`](starter/kri.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-06/starter`
2. Read `kri.py` the way the lesson builds it:
   - Lines 1–5: the thresholds sit at the top
   - Lines 6–13: the overdue function
   - Lines 14–20: the loop evaluates each month end
3. Run it: `python3 kri.py`.
4. Check it from the repository root: `./check m02l02-06`.

## Expected output

```text
2026-01-31   0% green
2026-02-28  10% amber vpn-02
2026-03-31  30% red   mail-01 web-05 web-06
```

## How to check

`./check m02l02-06` copies `starter/` into a scratch directory and runs `python3 kri.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
