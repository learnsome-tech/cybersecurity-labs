# m02l05-04 · Checking a vendor's SBOM against advisories

**Lesson:** [Vendor & Third-Party Risk Management Programs](https://learnsome.tech/learn/cybersecurity-course/m02l05) (lesson 2.5, module 2: Governance, Risk & Compliance) · Pro  
**Check:** Graded

## Goal

You can tier vendors by the risk they bring, choose the evidence and contract terms each tier needs, check a vendor's SBOM against advisories, and verify their SLA with your own data.

In the lesson: The log vendor's agent runs on our servers, so we asked for its software bill of materials in CycloneDX, a standard J S O N format listing every component inside. We check it against a short advisory feed, shaped like O S V records with versions simplified to plain numbers. The ver function turns a version string into numbers, so two point nine sorts below two point fourteen, which text comparison gets wrong. The program prints what the bill describes, then checks each component against any advisory for that package, using the introduced and fixed versions. Run it. The agent still bundles log four j core two point fourteen point one, hit by Log four Shell, and a SnakeYAML release older than two point zero. The OpenSSL copy is the fixed release, so it passes. Those findings go back to the vendor with a deadline the contract already sets.

## Files

- [`starter/advisories.json`](starter/advisories.json)
- [`starter/forwarder.cdx.json`](starter/forwarder.cdx.json)
- [`starter/sbom_check.py`](starter/sbom_check.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-04/starter`
2. Read `sbom_check.py` the way the lesson builds it:
   - Lines 1–4: the ver function
   - Lines 5–9: prints what the bill describes
   - Lines 10–18: the introduced and fixed versions
3. Run it: `python3 sbom_check.py`.
4. Check it from the repository root: `./check m02l05-04`.

## Expected output

```text
fabrikam-forwarder 3.4.0: 4 components
  CVE-2021-44228 org.apache.logging.log4j:log4j-core 2.14.1: affected below 2.15.0
  CVE-2022-1471 org.yaml:snakeyaml 1.33: affected below 2.0
  CVE-2022-3602 openssl 3.0.7: not affected
```

## How to check

`./check m02l05-04` copies `starter/` into a scratch directory and runs `python3 sbom_check.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
