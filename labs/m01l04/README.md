# m01l04 · Defense-in-Depth & Security Control Categories

Module 1: Core Security Principles · lesson 1.4 · Free · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m01l04)

**Goal:** You can sort any control by category and type under both the ISC2 and Security+ schemes, and test one layer of a real defence in depth design, a fail2ban jail, against an auth.log to find the attacks it misses.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l04-04](m01l04-04/) | One layer: a fail2ban jail | Read along |
| [m01l04-05](m01l04-05/) | What the bastion's auth.log records | Graded |
| [m01l04-06](m01l04-06/) | Applying the jail's rule to the log | Graded |
| [m01l04-07](m01l04-07/) | Closing the gaps, and what it costs | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: tune the jail and classify the layers

1. Set maxretry = 3 in jail.local. Predict which addresses get banned, then run the checker
2. Add a burst of five alice failures from 203.0.113.9 in two minutes. What happens?
3. Support hours in findtime, such as 1h, and rerun retest.sh with findtime = 1h
4. Classify each bastion layer from the first slide by category and by type

> **Hint:** Map the last character of findtime to a timedelta keyword, as in m for minutes and h for hours, before converting the number.

## Check yourself

- The office range sat in ignoreip, so a compromised office laptop made nine failed root logins without a ban. Which principle of defence in depth did that configuration break?
- Fail2ban reads the log, spots repeated failures and then blocks the address for an hour. Which control category and types does it belong to?
- Raising findtime from 10m to 60m caught the slow attacker. What does it cost, and how would you notice?
- A legacy payroll server cannot support MFA. What makes network isolation plus an MFA-protected jump host a valid compensating control rather than just another control?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
