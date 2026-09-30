# m05l04-02 · A written escalation policy

**Lesson:** [Incident Roles, Escalation & Crisis Comm](https://learnsome.tech/learn/cybersecurity-course/m05l04) (lesson 5.4, module 5: Resilience & Disaster Recovery) · Pro  
**Check:** Read along

## Goal

You can staff an incident with clear roles, apply a written escalation policy, and run crisis communication that meets regulatory deadlines.

In the lesson: Escalation works when it is written down before the incident, not negotiated during it. This is a small escalation policy in TOML. Each severity starts with a plain description a tired responder can match against, because the first argument on any call is about severity. The chain lists who gets paged, in order, and the escalate after value is how long each person has to acknowledge before the next one is paged. So severity one reaches the chief information security officer within ten minutes if nobody answers. The comms line sets the update rhythm, so the communications lead is not guessing how often executives expect to hear something. Severity three only ever reaches two people. That is either a choice somebody made on purpose, or a gap nobody noticed.

## Files

- [`starter/severity.toml`](starter/severity.toml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/severity.toml` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: a plain description
   - Lines 4–5: the chain lists who gets paged
   - Lines 6: the comms line
   - Lines 7–18: severity three only ever reaches

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
