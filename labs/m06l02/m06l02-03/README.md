# m06l02-03 · Inherent against residual, sorted for the committee

**Lesson:** [Enterprise Risk Registers & Treatment Plans](https://learnsome.tech/learn/cybersecurity-course/m06l02) (lesson 6.2, module 6: Enterprise Strategy & Audit) · Pro  
**Check:** Graded

## Goal

You can write risk register entries with a cause, an owner and a treatment, score inherent and residual risk, and check that every decision is authorised and in date.

In the lesson: The first thing a risk committee wants is the register sorted by residual risk. The script sets the appetite at the top. Appetite is the amount of risk the board has agreed to carry, written here as a rule: a residual score above eight needs treatment or a sign-off. Next, it multiplies likelihood by impact twice, once for inherent and once for residual. Then it sorts, highest residual first, and flags anything above appetite. Look at the output. The checkout risk fell from fifteen to one, because the company stopped storing card numbers at all. The lost laptop risk has not moved: twelve before and twelve after, even though it is insured. Four rows sit above appetite, and those four are the committee's agenda.

## Files

- [`starter/register.csv`](starter/register.csv)
- [`starter/register_view.py`](starter/register_view.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-03/starter`
2. Read `register_view.py` the way the lesson builds it:
   - Lines 1–3: sets the appetite at the top
   - Lines 4–8: multiplies likelihood by impact twice
   - Lines 9–15: then it sorts, highest residual first
3. Run it: `python3 register_view.py`.
4. Check it from the repository root: `./check m06l02-03`.

## Expected output

```text
id    inh  res  treatment  owner
R-01   20   15  mitigate   infra  above appetite
R-05   12   12  transfer   it     above appetite
R-06   16   12  accept     hr     above appetite
R-07   12   12  mitigate   infra  above appetite
R-02   12    8  accept     data
R-03   15    5  mitigate   infra
R-04   15    1  avoid      cto
```

## How to check

`./check m06l02-03` copies `starter/` into a scratch directory and runs `python3 register_view.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
