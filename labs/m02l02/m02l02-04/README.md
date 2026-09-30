# m02l02-04 · Two tied risks, priced

**Lesson:** [Risk Assessment: Qualitative vs Quantitative](https://learnsome.tech/learn/cybersecurity-course/m02l02) (lesson 2.2, module 2: Governance, Risk & Compliance) · Pro  
**Check:** Graded

## Goal

You can score risks on a likelihood and impact matrix, calculate SLE, ARO and ALE to compare a risk with the cost of treating it, and track a key risk indicator against tolerance.

In the lesson: Here are the two tied risks again, with estimates attached, in pounds. The payment platform takes four hundred thousand a day. One regional outage loses a quarter of that, and we expect one every two years. The leavers' accounts expose a data set valued at six hundred thousand, but misuse would cost a tenth of it and happens about once in five years. The function returns the single and annualised loss. For each proposed control, the program recalculates the yearly loss with the control in place and subtracts what the control costs a year. Run it. The outage is worth fifty thousand a year, the leaver risk twelve thousand. Not a tie. A second region pays for itself. The identity suite costs more than the loss it prevents, while a small H R feed that disables leavers comes out ahead.

## Files

- [`starter/quant.csv`](starter/quant.csv)
- [`starter/quantitative.py`](starter/quantitative.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-04/starter`
2. Read `quantitative.py` the way the lesson builds it:
   - Lines 1–5: the function returns
   - Lines 6–16: recalculates the yearly loss
3. Run it: `python3 quantitative.py`.
4. Check it from the repository root: `./check m02l02-04`.

## Expected output

```text
R4 Second region
   SLE 100,000  ALE 50,000 -> 5,000
   control 30,000 a year, net value 15,000
R5 Identity governance suite
   SLE 60,000  ALE 12,000 -> 1,200
   control 20,000 a year, net value -9,200
R5 HR feed disables leavers
   SLE 60,000  ALE 12,000 -> 2,400
   control 3,000 a year, net value 6,600
```

## How to check

`./check m02l02-04` copies `starter/` into a scratch directory and runs `python3 quantitative.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
