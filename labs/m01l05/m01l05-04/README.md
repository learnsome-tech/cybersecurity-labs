# m01l05-04 · The bastion's sshd_config

**Lesson:** [Security Governance vs Security Management](https://learnsome.tech/learn/cybersecurity-course/m01l05) (lesson 1.5, module 1: Core Security Principles) · Free  
**Check:** Read along

## Goal

You can separate governance decisions from management work, place a document correctly among policy, standard, procedure and guideline, name the governance roles and external obligations, and produce compliance evidence that reflects how a system really behaves.

In the lesson: Here is the evidence side. This is the main S S H daemon configuration on the bastion. The Include line near the top pulls in every dot conf file from a drop in directory; a relative path like this one is taken as relative to the S S H configuration directory. Everything below it reads like a model answer to the standard: root login off, three attempts, X eleven forwarding off, password authentication off. An engineer who opened this file, or searched it for the word password, would sign it off as compliant. Hold that thought, because the drop in directory has one file in it, written by the image build.

## Files

- [`starter/sshd_config`](starter/sshd_config): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/sshd_config` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–2: The Include line
   - Lines 3–9: Everything below it

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l05-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
