# m03l01-03 · AES-GCM refuses the same edit

**Lesson:** [Symmetric Encryption: AES-GCM & ChaCha20](https://learnsome.tech/learn/cybersecurity-course/m03l01) (lesson 3.1, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Graded

## Goal

You can explain what AES-GCM and ChaCha20-Poly1305 add to a plain cipher, show a bit-flip attack failing against a tag, and spot the nonce reuse that breaks both.

In the lesson: G C M, Galois counter mode, is counter mode plus an authentication tag. The helper file next to this program calls OpenSSL's own libcrypto through ctypes, the same library a web server uses. Same key, a twelve byte nonce, and a header that travels in the clear but is still protected. That header is the associated data, the A D in A E A D. Seal returns ciphertext and a sixteen byte tag. Now compare the output with the last program: the ciphertext is identical, byte for byte. The tag is the new part. Then we make the same bit flip and try to open both versions. The original decrypts. The tampered copy is rejected before any plaintext is released, so the bank never sees a wrong amount. Edit the header instead and you get the same refusal.

## Files

- [`starter/aead.py`](starter/aead.py)
- [`starter/gcm_tamper.py`](starter/gcm_tamper.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-03/starter`
2. Read `gcm_tamper.py` the way the lesson builds it:
   - Lines 1–4: a header that travels in the clear
   - Lines 5–9: seal returns ciphertext
   - Lines 10–19: the same bit flip
3. Notes from the lesson:
   - Line 7: aead.py wraps EVP_CipherInit_ex2 and friends in libcrypto
4. Run it: `python3 gcm_tamper.py`.
5. Check it from the repository root: `./check m03l01-03`.

## Expected output

```text
on the wire: 7eddccfe851db38d269899155f6ec1b9a62c76621ab2541ab6a98b
tag:         eb61636d712164ba3f3285fc84ed5f25
original: pay 0100.00 GBP to 12345678
tampered: rejected, authentication failed, nothing released
```

## How to check

`./check m03l01-03` copies `starter/` into a scratch directory and runs `python3 gcm_tamper.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
