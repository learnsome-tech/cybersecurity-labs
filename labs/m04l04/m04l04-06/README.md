# m04l04-06 · Cryptographic erase: destroy the key, not the disk

**Lesson:** [Asset Lifecycle Management & Media Sanitization](https://learnsome.tech/learn/cybersecurity-course/m04l04) (lesson 4.4, module 4: Data Protection & Privacy) · Pro  
**Check:** Graded

## Goal

You can reconcile an asset inventory against what is really on the network and pick a sanitisation method that matches the media and the data on it.

In the lesson: A self encrypting drive encrypts every block with a media key held inside the drive, and cryptographic erase means replacing that key. It takes seconds whatever the drive's size. This script mimics it, with a file standing in for the drive and openssl for its encryption engine. A payroll export is encrypted with a random media key and the plain copy removed. The read disk function decrypts with whatever key is currently installed and checks whether the payroll text comes back. With the original key it does. Then we replace the key and read again: unreadable, even though the encrypted blocks are unchanged. The same idea covers the cloud, where you cannot shred a provider's disks: encrypt with a key you control, and deleting the key is the sanitisation. It only works if the data was encrypted from the start, and no copy of the old key survives in a backup.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/crypto-erase.sh`](starter/crypto-erase.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-06/starter`
2. Read `crypto-erase.sh` the way the lesson builds it:
   - Lines 1–8: encrypted with a random media key
   - Lines 9–13: The read disk function
   - Lines 14–17: replace the key
3. Run it: `bash crypto-erase.sh`.
4. Check it from the repository root: `./check m04l04-06`.

## Expected output

```text
with the original media key: readable
after the key is replaced: unreadable
encrypted blocks on disk: unchanged
```

## How to check

`./check m04l04-06` copies `starter/` into a scratch directory and runs `bash crypto-erase.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
