# m03l02-02 · Diffie-Hellman in a real 2048-bit group

**Lesson:** [Asymmetric Cryptography: RSA, ECC & Diffie-Hellman](https://learnsome.tech/learn/cybersecurity-course/m03l02) (lesson 3.2, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Graded

## Goal

You can show two parties agreeing a key in public with Diffie-Hellman and X25519, compare RSA and elliptic curve key and signature sizes, and explain why authentication and forward secrecy still matter.

In the lesson: Here is Diffie-Hellman in plain Python, using the real two thousand and forty eight bit group from R F C three five two six. The prime and the generator, which is two, are public and the same for everyone; they sit in a small file beside this one. Alice and Bob each pick a private number. The seed is fixed so the demo repeats, while real code draws these from the secrets module. Each side raises the generator to its private number, modulo the prime, and sends the result. An eavesdropper sees both of those values. Then each side raises the other's public value to its own private number. Run it and compare the two computed lines. They match, because both equal the generator raised to a times b. The listener has the public values but neither private number, and working backwards is the discrete logarithm problem, which is out of reach at this size.

## Files

- [`starter/dh_modp.py`](starter/dh_modp.py): the listing from the lesson
- [`starter/modp2048.py`](starter/modp2048.py)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-02/starter`
2. Read `dh_modp.py` the way the lesson builds it:
   - Lines 1–5: each pick a private number
   - Lines 6–12: sends the result
   - Lines 13–18: raises the other's public value
3. Run it: `python3 dh_modp.py`.
4. Check it from the repository root: `./check m03l02-02`.

## Expected output

```text
prime: 2048 bits
Alice sends: 0xc7ccdf0de0d947f827216c21...
Bob sends:   0x32d862dd640632c307c2dffd...
Alice gets:  0x398aaafc8569ca07b877f1a2...
Bob gets:    0x398aaafc8569ca07b877f1a2...
same secret: True
```

## How to check

`./check m03l02-02` copies `starter/` into a scratch directory and runs `python3 dh_modp.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
