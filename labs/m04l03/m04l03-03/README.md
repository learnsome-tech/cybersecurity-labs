# m04l03-03 · A schema that doubles as a data inventory

**Lesson:** [Privacy Principles, GDPR Subject Rights & Minimization](https://learnsome.tech/learn/cybersecurity-course/m04l03) (lesson 4.3, module 4: Data Protection & Privacy) · Pro  
**Check:** Read along

## Goal

You can tell a controller from a processor, find everything held about one person, and answer an access or erasure request without breaking another law.

In the lesson: You cannot answer a privacy request for data you do not know you hold, so a data inventory comes first. Here it lives in the schema of a small online shop, with a purpose and a retention period written against each table. Customers holds the account, kept while the account is open. The orders are kept six years, because tax rules demand the records. Then marketing and support tickets. Marketing rests on consent, so it lasts until the customer withdraws it, and support notes are kept two years after the ticket closes. Below that are three customers, their orders, two newsletter sign ups and three tickets. Notice that the orders table has no email column at all. It links to a person only through the customer number, which is exactly the kind of detail that makes a manual search miss data.

## Files

- [`starter/shop.sql`](starter/shop.sql): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shop.sql` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–3: Customers holds the account
   - Lines 4–5: orders are kept six years
   - Lines 6–9: marketing and support tickets
   - Lines 10–21: three customers

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
