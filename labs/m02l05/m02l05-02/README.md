# m02l05-02 · Tiering vendors from the intake list

**Lesson:** [Vendor & Third-Party Risk Management Programs](https://learnsome.tech/learn/cybersecurity-course/m02l05) (lesson 2.5, module 2: Governance, Risk & Compliance) · Pro  
**Check:** Graded

## Goal

You can tier vendors by the risk they bring, choose the evidence and contract terms each tier needs, check a vendor's SBOM against advisories, and verify their SLA with your own data.

In the lesson: Here is an intake list from procurement, one row per vendor. Each row records the service, the most sensitive data the vendor will hold, what access it gets into our environment, and whether the business stops without it. The table at the top says what evidence each tier must produce. The tier function applies the rules: sensitive data plus either access or business dependence is tier one; sensitive data or access alone is tier two; anything else is tier three. The loop prints each vendor with its tier. Run it. Payroll, helpdesk and logs are tier one and owe an independent report, a full questionnaire and a pen test summary every year. The printer company is tier two because its devices sit on our network, even though it holds no data. The snack supplier needs a contract and nothing more.

## Files

- [`starter/tiering.py`](starter/tiering.py): the listing from the lesson
- [`starter/vendors.csv`](starter/vendors.csv)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-02/starter`
2. Read `tiering.py` the way the lesson builds it:
   - Lines 1–8: what evidence each tier must produce
   - Lines 9–15: the tier function applies the rules
   - Lines 16–19: prints each vendor
3. Run it: `python3 tiering.py`.
4. Check it from the repository root: `./check m02l05-02`.

## Expected output

```text
Northwind Payroll tier 1  SOC 2 Type II or ISO 27001, SIG Core, pen test; yearly
Contoso Helpdesk  tier 1  SOC 2 Type II or ISO 27001, SIG Core, pen test; yearly
Fabrikam Logs     tier 1  SOC 2 Type II or ISO 27001, SIG Core, pen test; yearly
Wingtip Surveys   tier 2  SIG Lite or CAIQ; every two years
Litware Print     tier 2  SIG Lite or CAIQ; every two years
Tailspin Snacks   tier 3  contract terms only; at renewal
```

## How to check

`./check m02l05-02` copies `starter/` into a scratch directory and runs `python3 tiering.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
