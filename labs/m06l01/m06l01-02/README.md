# m06l01-02 · The current state: exported security group rules

**Lesson:** [Security Architecture Gap Analysis](https://learnsome.tech/learn/cybersecurity-course/m06l01) (lesson 6.1, module 6: Enterprise Strategy & Audit) · Pro  
**Check:** Read along

## Goal

You can compare exported security configuration against a written target architecture, find the gaps with a script, and rank them for a plan.

In the lesson: Here is the current state for two tiers, exported from a cloud account with the A W S command line tool, describe security groups, and trimmed to the fields we need. Each security group holds ingress permissions. A permission has a protocol, a port range and a list of source ranges in C I D R notation. The database tier allows Postgres on port five four three two from the app subnet, which matches the diagram. It also allows the same port from a single vendor address, added for a reporting tool. Below that sits a rule with protocol minus one. In A W S that means all traffic on every port, here from the whole ten slash eight block, labelled migration. Finally, the bastion allows S S H on port twenty two from the management subnet, and also from anywhere, labelled temp debug.

## Files

- [`starter/sg.json`](starter/sg.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/sg.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: each security group holds ingress permissions
   - Lines 4–6: allows Postgres on port five four three two
   - Lines 7–8: a rule with protocol minus one
   - Lines 9–14: the bastion allows S S H

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l01-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
