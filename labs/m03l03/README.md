# m03l03 · Cryptographic Hashing: SHA-256, SHA-3 & Passwords

Module 3: Applied Cryptography & Keys · lesson 3.3 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m03l03)

**Goal:** You can show what SHA-256 and SHA-3 guarantee, use HMAC where a bare hash is forgeable, store passwords with salt and a slow function, and explain how a hash chain makes a ledger tamper-evident.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l03-02](m03l03-02/) | SHA-256 and SHA-3 on a one-character change | Graded |
| [m03l03-03](m03l03-03/) | Integrity needs a key: HMAC | Graded |
| [m03l03-04](m03l03-04/) | Passwords: fast hashes fall, salted slow ones hold | Graded |
| [m03l03-05](m03l03-05/) | Hash chains: why a ledger shows tampering | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Predict the digest, then break the chain

1. fingerprint.py: change the case of one letter in a. Predict how many bits differ, then run.
2. webhook.py: call hmac_check(forged, header) with the original header. Accepted or not?
3. passwords.py: add the word that cracks chen, then give every user an os.urandom(16) salt.
4. ledger.py: edit the last entry instead of the first. Which links break now?

> **Hint:** Expect about half of the bits, whatever the change. A chain only breaks at the edited entry and after it.

## Check yourself

- In fingerprint.py one character changed and about half the output bits flipped. Why does that behaviour matter for integrity checks?
- webhook.py's plain check accepted a forged request carrying a freshly computed SHA-256. What was missing, and why did the HMAC check stop it?
- Amara and Ben were both cracked in one wordlist pass. Which two changes in the fix stop that, and what does each one defend against?
- In ledger.py only the first entry was edited, yet every link reported broken. Why?
- A developer authenticates API calls with sha256(secret + message). What attack does that invite, and what should they use instead?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
