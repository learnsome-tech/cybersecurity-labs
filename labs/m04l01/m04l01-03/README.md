# m04l01-03 · Where an Office document keeps its label

**Lesson:** [Data Classification Schemes & Sensitivity Labeling](https://learnsome.tech/learn/cybersecurity-course/m04l01) (lesson 4.1, module 4: Data Protection & Privacy) · Pro  
**Check:** Read along

## Goal

You can choose a classification label for a dataset, store it where it survives copying, and enforce it where data is shared or stored.

In the lesson: A label only helps if it travels with the data. A folder called confidential stops meaning anything once someone attaches the file to an email. So labelling tools write the label into the document itself. An Office document is a zip archive of X M L parts, and Microsoft sensitivity labels have long been stored in one of them, the custom properties part. Each property name starts with M S I P label, then the label's unique identifier, then a field. Enabled says a label is applied. Name is the label a person sees in Office. Set date records when it was applied. And method says whether a rule applied it by default, which is standard, or a person chose it on purpose, which is privileged. Newer Office builds also keep a copy in a separate label info part, but the idea is the same: the label is bytes inside the file.

## Files

- [`starter/custom.xml`](starter/custom.xml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/custom.xml` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: the custom properties part
   - Lines 5–7: Enabled says
   - Lines 8–10: Name is the label
   - Lines 11–13: Set date records
   - Lines 14–17: method says whether

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
