# m04l02 · Data States: Security at Rest, in Transit, and in Use

Module 4: Data Protection & Privacy · lesson 4.2 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m04l02)

**Goal:** You can say which state a piece of data is in, which attacker that state invites, and which protection method fits it.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l02-02](m04l02-02/) | At rest: what a stolen database file shows | Graded |
| [m04l02-03](m04l02-03/) | In transit: what the network path sees | Graded |
| [m04l02-04](m04l02-04/) | In use: tokenise what you store, mask what you show | Graded |
| [m04l02-05](m04l02-05/) | Hashing is not hiding when inputs are guessable | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Break and repair each state

1. In at-rest.sh, delete db.key right after encrypting. Predict what the restore step prints.
2. In tokens.py, add an order for card 4111111111111111 and predict its token before running.
3. In hashes.py, add a random salt kept beside the hash. Does the guess still succeed? Why?
4. Change wire.py to send JSON with a bearer token and confirm it is just as visible.

> **Hint:** A salt stored with the hash is public, so the attacker just adds it to each guess.

## Check yourself

- A company encrypts its database backups, but the backup job writes the key file into the same storage bucket. What does an attacker who copies the bucket get?
- In wire.py the service account's password was recovered from the Authorization header. Why did no key or cracking step appear in the program?
- Orders 1001 and 1003 used the same card and received the same token. What does that allow, and what does the orders table still not reveal?
- An export replaces every date of birth with its plain SHA-256 hash. Why did hashes.py recover the date, and why did the HMAC version resist?
- A support agent needs to confirm which card a customer used but never needs to charge it. Which method fits, and why not encryption?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
