# m02l02-02 · Scoring a risk register on a five by five matrix

**Lesson:** [Risk Assessment: Qualitative vs Quantitative](https://learnsome.tech/learn/cybersecurity-course/m02l02) (lesson 2.2, module 2: Governance, Risk & Compliance) · Pro  
**Check:** Graded

## Goal

You can score risks on a likelihood and impact matrix, calculate SLE, ARO and ALE to compare a risk with the cost of treating it, and track a key risk indicator against tolerance.

In the lesson: The quickest way to answer is a qualitative scale. Each risk in this register has a likelihood and an impact from one to five, where one means rare or negligible and five means almost certain or severe. At the top is the risk appetite the board set: anything scoring above nine needs a treatment plan. The function puts each score in a band. The program reads the register as C S V, the format most registers export to, and multiplies the two. Then it sorts them and prints the decision. Run it. Ransomware leads at fifteen. Now look at the two risks scoring twelve: the payment outage and the leavers' accounts. The matrix says they are equal. Is three times four really the same as four times three? The scale cannot say, because those numbers are ranks, not measurements.

## Files

- [`starter/qualitative.py`](starter/qualitative.py): the listing from the lesson
- [`starter/register.csv`](starter/register.csv)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-02/starter`
2. Read `qualitative.py` the way the lesson builds it:
   - Lines 1–3: the risk appetite the board set
   - Lines 4–10: puts each score in a band
   - Lines 11–15: multiplies the two
   - Lines 16–20: sorts them
3. Run it: `python3 qualitative.py`.
4. Check it from the repository root: `./check m02l02-02`.

## Expected output

```text
R1 15 critical treat  Ransomware via phished VPN credentials
R4 12 high     treat  Payment API down in its only region
R5 12 high     treat  Leavers' accounts left active
R2 10 high     treat  Cloud bucket exposes customer exports
R3  8 medium   accept Unencrypted laptop stolen
```

## How to check

`./check m02l02-02` copies `starter/` into a scratch directory and runs `python3 qualitative.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
