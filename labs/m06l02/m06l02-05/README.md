# m06l02-05 · Checking the decisions, not only the scores

**Lesson:** [Enterprise Risk Registers & Treatment Plans](https://learnsome.tech/learn/cybersecurity-course/m06l02) (lesson 6.2, module 6: Enterprise Strategy & Audit) · Pro  
**Check:** Graded

## Goal

You can write risk register entries with a cause, an owner and a treatment, score inherent and residual risk, and check that every decision is authorised and in date.

In the lesson: A register with stale decisions is worse than none, because it looks like governance. This second script checks the decisions. It fixes the review date as the day of the committee meeting, and it holds an authority table: the C I S O may accept residual scores up to fifteen, the chief financial officer or chief executive up to twenty five, and anyone else only up to appetite. For every acceptance or transfer it asks two questions: did the signer have the authority, and has the sign-off expired? For every open mitigation it checks whether the due date has passed. Run it and you get three problems. The vendor acceptance lapsed in June. The H R portal risk was signed off by the I T manager, who cannot accept a score of twelve. And the database fix is overdue.

## Files

- [`starter/register.csv`](starter/register.csv)
- [`starter/register_review.py`](starter/register_review.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-05/starter`
2. Read `register_review.py` the way the lesson builds it:
   - Lines 1–6: holds an authority table
   - Lines 7–17: for every acceptance or transfer
   - Lines 18–20: for every open mitigation
3. Notes from the lesson:
   - Line 12: Not in LIMIT: the signer may only accept risk up to appetite
4. Run it: `python3 register_review.py`.
5. Check it from the repository root: `./check m06l02-05`.

## Expected output

```text
R-02 sign-off expired on 2026-06-30
R-06 signed by it-mgr, who may accept up to 8; residual is 12
R-07 action overdue since 2026-09-15, owner infra
```

## How to check

`./check m06l02-05` copies `starter/` into a scratch directory and runs `python3 register_review.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
