# m06l03-03 · The population: change tickets for the period

**Lesson:** [Internal Audits, Sampling & Evidence Chains](https://learnsome.tech/learn/cybersecurity-course/m06l03) (lesson 6.3, module 6: Enterprise Strategy & Audit) · Pro  
**Check:** Read along

## Goal

You can draw a repeatable audit sample from a complete population, test it against a control statement, seal the evidence with hashes, and write up the finding.

In the lesson: This is the population: change tickets exported from the ticketing system, fifty rows in all, and here are a dozen from the middle. Each row has the ticket number, a summary, who implemented it, who approved it, and two timestamps. Before sampling anything, an auditor asks whether the population is complete. If the export was filtered, or some changes never got a ticket, the sample proves nothing about them. So you record where the export came from and who ran it, and you compare its count with another source, such as the deployment logs. Now notice ticket ten twenty six. It has no approver at all. Keep it in mind.

## Files

- [`starter/changes.csv`](starter/changes.csv): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/changes.csv` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: each row has the ticket number
   - Lines 2–12: notice ticket ten twenty six
3. Notes from the lesson:
   - Line 11: No approver and no approval time, and the sample will not pick it

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
