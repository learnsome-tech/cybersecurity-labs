# m06l03-06 · Sealing the evidence so tampering shows

**Lesson:** [Internal Audits, Sampling & Evidence Chains](https://learnsome.tech/learn/cybersecurity-course/m06l03) (lesson 6.3, module 6: Enterprise Strategy & Audit) · Pro  
**Check:** Graded

## Goal

You can draw a repeatable audit sample from a complete population, test it against a control statement, seal the evidence with hashes, and write up the finding.

In the lesson: Evidence has to survive until the report is issued and beyond. This shell script seals the pack the moment testing ends. It runs sha two five six sum over the population, the sample and the results, writes the hashes to a manifest, and then hashes the manifest itself. That last hash goes into the audit ticket, outside the evidence folder, so nobody can edit a file and quietly rebuild the manifest to match. Next, the script plays the part of a helpful colleague who changes ticket ten thirty one from exception to pass. Then it checks the pack against the manifest. The population and the sample still match, but the results file fails, and the tool says so. The chain from export to sample to result can now be checked by anyone.

## Files

- [`starter/changes.csv`](starter/changes.csv)
- [`starter/command.txt`](starter/command.txt)
- [`starter/results.csv`](starter/results.csv)
- [`starter/sample.txt`](starter/sample.txt)
- [`starter/seal_evidence.sh`](starter/seal_evidence.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-06/starter`
2. Read `seal_evidence.sh` the way the lesson builds it:
   - Lines 1–5: hashes the manifest itself
   - Lines 6–8: plays the part of a helpful colleague
   - Lines 9–10: checks the pack against the manifest
3. Run it: `bash seal_evidence.sh`.
4. Check it from the repository root: `./check m06l03-06`.

## Expected output

```text
f1691a99e1b080e3d15d1358329688ec4109f181037e4c3b3332213134a0473c  changes.csv
e9d63cd3c923ee4f25daab120eebe0c71b1c590e0dc23265b1e9e733a8dbbd37  sample.txt
7d4ad1dac3cad55e1fee803d7bfc942fba9ae447e50eab811ff9a42506a699d4  results.csv
c524117aef6825cff8bbe6ecbe1899bdf864f29b171905d2e0ecfe90c5c7664f  manifest.sha256
changes.csv: OK
sample.txt: OK
results.csv: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
```

## How to check

`./check m06l03-06` copies `starter/` into a scratch directory and runs `bash seal_evidence.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
