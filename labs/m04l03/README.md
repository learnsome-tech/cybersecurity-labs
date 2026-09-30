# m04l03 · Privacy Principles, GDPR Subject Rights & Minimization

Module 4: Data Protection & Privacy · lesson 4.3 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m04l03)

**Goal:** You can tell a controller from a processor, find everything held about one person, and answer an access or erasure request without breaking another law.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l03-03](m04l03-03/) | A schema that doubles as a data inventory | Read along |
| [m04l03-04](m04l03-04/) | Answering an access request from the database itself | Graded |
| [m04l03-06](m04l03-06/) | Erasure, legal holds and retention sweeps | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Handle the next two requests

1. Run sar.py for ben@example.org. Predict each table's row count before you run it.
2. Add a reviews table keyed on customer_id with one row for Alice; does sar.py find it?
3. Chloe withdraws marketing consent only. Write the one statement that honours that.
4. Change TODAY in erase.py to 2027-01-01 and predict which extra rows disappear.

> **Hint:** Withdrawing consent affects marketing only; her account and orders have other bases.

## Check yourself

- A booking company stores a clinic's patient appointments under contract, then starts using that data to target its own adverts. What has changed in its role?
- sar.py found six records for Alice. Why would a search of every table for her email address alone have missed two of them?
- After Alice's erasure request, erase.py still kept one of her orders. Under what condition is that correct?
- An email from alice.hart.home@example.net asks for a copy of all Alice's data. Why should the team not simply send the export?
- A newsletter sign-up form asks for email, date of birth and phone number. Which principle does it break, and what is the fix?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
