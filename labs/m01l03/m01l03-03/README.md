# m01l03-03 · A business email compromise, raw

**Lesson:** [Social Engineering, Phishing & Human Defense](https://learnsome.tech/learn/cybersecurity-course/m01l03) (lesson 1.3, module 1: Core Security Principles) · Free  
**Check:** Read along

## Goal

You can name the common attack vectors and social engineering techniques, read a suspicious email's raw headers and authentication results, spot lookalike domains, and judge a phishing awareness programme by how fast people report.

In the lesson: This is the raw message as our mail server stored it. A mail client shows you almost none of it. The first line is the Return Path, where bounces go, and its domain spells example with the digit one in place of the letter l. Next, the Authentication Results header, added by our own gateway, records the S P F, D K I M and D M A R C checks. Then From: the display name your client shows, and an address on the supplier's real domain. Reply To sends your answer to a mailbox somewhere else entirely. Finally the body: urgency, a late fee, and a link whose text shows the real portal while the link itself points at the lookalike domain.

## Files

- [`starter/invoice.eml`](starter/invoice.eml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/invoice.eml` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: where bounces go
   - Lines 2–5: Authentication Results header
   - Lines 6: Then From
   - Lines 7: Reply To sends
   - Lines 8–16: Finally the body

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
