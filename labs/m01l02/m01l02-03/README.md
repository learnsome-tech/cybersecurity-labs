# m01l02-03 · One night of web traffic

**Lesson:** [Threat Actors, Motivations & Cyber Kill Chain](https://learnsome.tech/learn/cybersecurity-course/m01l02) (lesson 1.2, module 1: Core Security Principles) · Free  
**Check:** Read along

## Goal

You can tell threat actors apart by resources, skill and motive, spot a targeted visitor among scanner noise in a web log, and place incident evidence on the seven steps of the Cyber Kill Chain to see where it could have been stopped.

In the lesson: Here is one night from a web server access log in the common log format: client address, time, request line, status code and response size. The first four lines come from two addresses asking for files that are not on this server, such as a leaked environment file, a WordPress login page and a Git config. Every answer is a four oh four. The next four come from one address that reads the board page, a job advert for an accounts payable clerk and the supplier list, then posts to the login form. The last line is someone reading the same job advert and leaving.

## Files

- [`starter/access.log`](starter/access.log): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/access.log` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: The first four lines
   - Lines 5–8: The next four
   - Lines 9: The last line

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
