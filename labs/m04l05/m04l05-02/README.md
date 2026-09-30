# m04l05-02 · The message the rule will inspect

**Lesson:** [Data Loss Prevention & Egress Monitoring](https://learnsome.tech/learn/cybersecurity-course/m04l05) (lesson 4.5, module 4: Data Protection & Privacy) · Pro  
**Check:** Read along

## Goal

You can explain how a DLP rule decides that outbound content is sensitive, tune it against false positives, and spot bulk exfiltration in connection logs.

In the lesson: Here is what the mail gateway sees: an ordinary reply to a supplier, in the plain text format every mail system uses. The headers say who sent it, to whom, and when. The body mentions an order number, an invoice number and two card numbers. The cards should not be there at all, since the payment card rules require full card numbers sent by email or chat to be protected with strong cryptography. To a person the four numbers look nothing alike. To a regular expression they are four runs of sixteen digits.

## Files

- [`starter/outbound.eml`](starter/outbound.eml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/outbound.eml` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–5: The headers say
   - Lines 6–15: The body mentions

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
