# m04l02-03 · In transit: what the network path sees

**Lesson:** [Data States: Security at Rest, in Transit, and in Use](https://learnsome.tech/learn/cybersecurity-course/m04l02) (lesson 4.2, module 4: Data Protection & Privacy) · Pro  
**Check:** Graded

## Goal

You can say which state a piece of data is in, which attacker that state invites, and which protection method fits it.

In the lesson: Now data in transit. The program opens a listener on the loopback address, playing an internal A P I. The client function is a reporting job that sends a request over plain H T T P, with basic authentication and a customer's email in the body. Basic authentication is only base sixty four, which is encoding, not encryption. The main program reads every byte that arrives and prints it. Here the listener is the server, but a proxy or a mirrored switch port on the path would receive exactly the same bytes. Then it decodes the header. The last line is the service account's password, recovered without any key at all. The fix is to wrap the connection in T L S, or to carry it through an I P sec or S S H tunnel, so that the path only sees ciphertext. Being inside the company network is not a substitute.

## Files

- [`starter/wire.py`](starter/wire.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-03/starter`
2. Read `wire.py` the way the lesson builds it:
   - Lines 1–3: opens a listener
   - Lines 4–10: The client function
   - Lines 11–18: reads every byte
   - Lines 19–20: decodes the header
3. Run it: `python3 wire.py`.
4. Check it from the repository root: `./check m04l02-03`.

## Expected output

```text
wire: POST /v1/export HTTP/1.1
wire: Host: api.example.com
wire: Authorization: Basic c3ZjLXJlcG9ydDpub3QtYS1yZWFsLXBhc3N3b3Jk
wire: Content-Length: 33
wire:
wire: {"customer": "alice@example.com"}
decoded: svc-report:not-a-real-password
```

## How to check

`./check m04l02-03` copies `starter/` into a scratch directory and runs `python3 wire.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
