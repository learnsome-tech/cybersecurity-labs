# m02l04-04 · Why PCI DSS wants keyed hashes

**Lesson:** [Regulatory Compliance: SOC 2, HIPAA, GDPR & PCI-DSS](https://learnsome.tech/learn/cybersecurity-course/m02l04) (lesson 2.4, module 2: Governance, Risk & Compliance) · Pro  
**Check:** Graded

## Goal

You can tell which of SOC 2, HIPAA, GDPR and PCI DSS applies and why, find card data that has leaked into scope, and work out the breach notification deadlines one incident triggers.

In the lesson: Suppose a developer stores a hash of the PAN to spot returning customers, and also stores the masked number for display. It feels safe. The program hashes a test card number with S H A two five six, as the developer did, and also stores the masked number. An attacker who copies the database has both columns, so only the middle six digits are unknown: at most a million guesses. The loop tries them all. Then the second part plays the same attacker against a keyed hash, an H MAC, while holding the wrong key. Run it. The plain hash falls in about a second on a laptop. The keyed hash gives nothing. That is why PCI DSS version four requires keyed hashes, with the key in a key management service or H S M, never in the database beside the data.

## Files

- [`starter/hash_vs_hmac.py`](starter/hash_vs_hmac.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-04/starter`
2. Read `hash_vs_hmac.py` the way the lesson builds it:
   - Lines 1–5: also stores the masked number
   - Lines 6–12: tries them all
   - Lines 13–19: the second part
3. Run it: `python3 hash_vs_hmac.py`.
4. Check it from the repository root: `./check m02l04-04`.

## Expected output

```text
plain SHA-256: recovered 4111111111111111 after 111,112 guesses
keyed HMAC-SHA-256: 0 matches in 1,000,000 guesses
```

## How to check

`./check m02l04-04` copies `starter/` into a scratch directory and runs `python3 hash_vs_hmac.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
