# m05l01-02 · The BIA worksheet, one row per process

**Lesson:** [Business Impact Analysis, RTO & RPO Modeling](https://learnsome.tech/learn/cybersecurity-course/m05l01) (lesson 5.1, module 5: Resilience & Disaster Recovery) · Pro  
**Check:** Read along

## Goal

You can turn a business impact analysis into RTO and RPO targets, test them against real restore times and backup schedules, and work out what redundancy does to availability.

In the lesson: Here is what a B I A worksheet boils down to once the interviews are done. One row per business process. The maximum tolerable downtime and the work recovery time come from the process owner. The restore time is not a guess: it is how long the last restore test actually took. The backup interval is what the backup system is really configured to do, and the R P O is what the owner asked for. The last column lists dependencies. Checkout cannot take a single order until payments and identity are running, and payments itself needs identity. Dependencies are where most plans quietly fail, because each team measures its own restore in isolation.

## Files

- [`starter/bia.csv`](starter/bia.csv): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/bia.csv` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–2: one row per business process
   - Lines 3–5: the last column lists dependencies

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l01-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
