# m05l01 · Business Impact Analysis, RTO & RPO Modeling

Module 5: Resilience & Disaster Recovery · lesson 5.1 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m05l01)

**Goal:** You can turn a business impact analysis into RTO and RPO targets, test them against real restore times and backup schedules, and work out what redundancy does to availability.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l01-02](m05l01-02/) | The BIA worksheet, one row per process | Read along |
| [m05l01-03](m05l01-03/) | Checking the targets against real restore times | Graded |
| [m05l01-04](m05l01-04/) | Watching an RPO happen to real data | Graded |
| [m05l01-06](m05l01-06/) | Counting the nines | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Change the inputs, predict, then run

1. Add an email row to bia.csv that depends on identity; predict its ready time, then run.
2. Set identity's restore_h to 1 and predict which late verdict disappears.
3. In rpo_demo.py set EVERY to one hour and predict how many orders are lost.
4. In availability.py double only the database; which part now limits you?

> **Hint:** Ready time is your own restore plus the slowest dependency; worst-case loss is one backup interval.

## Check yourself

- Checkout restores in two hours on its own. Why did the analysis report it ready only after seven hours?
- Backups run every four hours and the RPO is one hour. What is the worst-case data loss, and which failure time produces it?
- Why must the RTO be shorter than the maximum tolerable downtime rather than equal to it?
- Two web servers share the same power strip. Why does the pair formula overstate their availability?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
