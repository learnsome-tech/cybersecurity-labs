# m06l02 · Enterprise Risk Registers & Treatment Plans

Module 6: Enterprise Strategy & Audit · lesson 6.2 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m06l02)

**Goal:** You can write risk register entries with a cause, an owner and a treatment, score inherent and residual risk, and check that every decision is authorised and in date.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l02-02](m06l02-02/) | A register exported from the risk spreadsheet | Read along |
| [m06l02-03](m06l02-03/) | Inherent against residual, sorted for the committee | Graded |
| [m06l02-05](m06l02-05/) | Checking the decisions, not only the scores | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Run your own risk committee

1. Set REVIEW to date(2026, 10, 20). Predict the extra line in the review, then run it.
2. Add R-08, accepted by ciso, with rL 4 and rI 4. Predict what the review reports.
3. Add a check that prints any row whose residual score is higher than its inherent score.
4. In register_view.py, print 'at appetite' when the residual equals APPETITE.

> **Hint:** Inside the review loop, compare int(r['L']) * int(r['I']) with the residual you already compute.

## Check yourself

- The lost laptop risk is insured, yet its residual score stayed at twelve. Why is that the right way to score it?
- R-02 has a residual score of eight, within appetite, but the review still flagged it. What was wrong, and why does it matter?
- Why can the IT manager not accept the HR portal risk, even though they signed it in good faith?
- The checkout risk fell from fifteen to one. Which treatment achieved that, and how?
- A colleague adds up every residual score and reports a total risk of seventy. What is wrong with that number?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
