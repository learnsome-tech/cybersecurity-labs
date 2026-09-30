# m04l02-02 · At rest: what a stolen database file shows

**Lesson:** [Data States: Security at Rest, in Transit, and in Use](https://learnsome.tech/learn/cybersecurity-course/m04l02) (lesson 4.2, module 4: Data Protection & Privacy) · Pro  
**Check:** Graded

## Goal

You can say which state a piece of data is in, which attacker that state invites, and which protection method fits it.

In the lesson: This script builds a small SQLite database with one customer, then plays the thief. SQLite stores rows in the file more or less as they were written, so when we run strings over the file, the output shows the table definition, and then the email and card number in plain text. Anyone who copies that file has the data. Next, openssl encrypts the whole file with a random key. The enc command has no G C M mode, so C B C stands in here; the lesson is about where the key lives, not the mode. Then we search both files for the address: visible in the original, gone from the encrypted copy. Finally the script decrypts it again with the key and the row comes back. That last step is the catch. If the key file sits next to the encrypted file, a thief takes both, which is why keys live in a separate key manager.

## Files

- [`starter/at-rest.sh`](starter/at-rest.sh): the listing from the lesson
- [`starter/command.txt`](starter/command.txt)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-02/starter`
2. Read `at-rest.sh` the way the lesson builds it:
   - Lines 1–4: run strings
   - Lines 5–7: encrypts the whole file
   - Lines 8–11: search both files
   - Lines 12–14: decrypts it again
3. Run it: `bash at-rest.sh`.
4. Check it from the repository root: `./check m04l02-02`.

## Expected output

```text
readable strings in customers.db:
SQLite format 3
tablecustomercustomer
CREATE TABLE customer (id INTEGER, email TEXT, card TEXT)
	/-alice@example.com4111111111111111
customers.db: email visible
customers.db.enc: email not found
1|alice@example.com
```

## How to check

`./check m04l02-02` copies `starter/` into a scratch directory and runs `bash at-rest.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
