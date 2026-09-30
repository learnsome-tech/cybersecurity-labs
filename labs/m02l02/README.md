# m02l02 · Risk Assessment: Qualitative vs Quantitative

Module 2: Governance, Risk & Compliance · lesson 2.2 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m02l02)

**Goal:** You can score risks on a likelihood and impact matrix, calculate SLE, ARO and ALE to compare a risk with the cost of treating it, and track a key risk indicator against tolerance.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l02-02](m02l02-02/) | Scoring a risk register on a five by five matrix | Graded |
| [m02l02-04](m02l02-04/) | Two tied risks, priced | Graded |
| [m02l02-06](m02l02-06/) | A key risk indicator against its tolerance line | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Move the numbers and predict the decision

1. In register.csv set R5's impact to 4. Predict its band and action, then run qualitative.py.
2. Add an R1 row to quant.csv with your own estimates. Find the control cost where value hits 0.
3. Give web-05 an install date of 2026-03-20. Predict March's KRI colour, then run kri.py.

> **Hint:** Two hosts out of ten is exactly twenty per cent, and the red test uses greater than or equal.

## Check yourself

- Two risks both score twelve on a five by five matrix. Why might they still deserve very different budgets?
- A control would cut a risk's ALE from 12,000 to 1,200 but costs 20,000 a year. What does that tell the risk owner?
- If a control halves a risk's exposure factor but does not change how often the event happens, what happens to the ALE?
- The patching KRI moved from amber to red in March. What should happen differently from a move to amber?
- A company buys cyber insurance against ransomware. What has it not transferred?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
