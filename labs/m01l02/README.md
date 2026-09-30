# m01l02 · Threat Actors, Motivations & Cyber Kill Chain

Module 1: Core Security Principles · lesson 1.2 · Free · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m01l02)

**Goal:** You can tell threat actors apart by resources, skill and motive, spot a targeted visitor among scanner noise in a web log, and place incident evidence on the seven steps of the Cyber Kill Chain to see where it could have been stopped.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l02-03](m01l02-03/) | One night of web traffic | Read along |
| [m01l02-04](m01l02-04/) | Opportunistic noise or a chosen target | Graded |
| [m01l02-06](m01l02-06/) | Placing an incident on the chain | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: retune the triage and the timeline

1. Add a POST to /login from 192.0.2.51 to access.log. Predict its label, then run triage.py
2. Now change about > 1 to about > 0. Which address flips to targeted, and is that fair?
3. In timeline.csv mark the proxy row alerted as yes. Predict the new dwell time first
4. Add a weaponisation row and write down which team could have supplied that evidence

> **Hint:** Dwell time is measured from the delivery row to the first row marked yes, so work it out from those two timestamps before running.

## Check yourself

- One address in the access log read the board page, a job advert for the accounts team and the supplier list, then posted to the login form. What does that tell you, and what can it not tell you?
- Why does an insider threat often need no exploit at all?
- In the incident timeline, why is weaponisation the one phase with no evidence, and where could evidence of it come from?
- If the proxy had alerted on the first beacon at 09:10 on 3 September, what would have happened to the dwell time and to the chain?
- Why can fear of being disciplined after clicking a phishing link make an incident worse?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
