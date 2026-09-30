# m03l01-02 · Counter mode hides the amount but not the edit

**Lesson:** [Symmetric Encryption: AES-GCM & ChaCha20](https://learnsome.tech/learn/cybersecurity-course/m03l01) (lesson 3.1, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Graded

## Goal

You can explain what AES-GCM and ChaCha20-Poly1305 add to a plain cipher, show a bit-flip attack failing against a tag, and spot the nonce reuse that breaks both.

In the lesson: This is real A E S with a two hundred and fifty six bit key in counter mode, run by the openssl command. The key is shown in class on purpose; a real key comes from the operating system's random generator and never sits in code. Counter mode encrypts a counter to make keystream, then combines it with your message using exclusive-or. The counter starts at two, a detail that pays off in the next program. The message is a payment instruction. Now the attacker. They cannot read the key, but they know the format, so they flip the bits at position four that turn a zero into a nine. Run it and read the last line. The bank decrypts pay nine thousand one hundred pounds, and nothing complains. Confidentiality held. Integrity did not.

## Files

- [`starter/ctr_flip.py`](starter/ctr_flip.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-02/starter`
2. Read `ctr_flip.py` the way the lesson builds it:
   - Lines 1–10: a real key comes from
   - Lines 11–14: the message is a payment instruction
   - Lines 15–18: now the attacker
3. Notes from the lesson:
   - Line 4: GCM runs its counter from two, so this matches it
   - Line 17: XOR mask: '0' becomes '9' with no key needed
4. Run it: `python3 ctr_flip.py`.
5. Check it from the repository root: `./check m03l01-02`.

## Expected output

```text
on the wire: 7eddccfe851db38d269899155f6ec1b9a62c76621ab2541ab6a98b
bank reads:  pay 9100.00 GBP to 12345678
```

## How to check

`./check m03l01-02` copies `starter/` into a scratch directory and runs `python3 ctr_flip.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
