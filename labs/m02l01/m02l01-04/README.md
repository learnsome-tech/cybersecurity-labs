# m02l01-04 · Auditing a server against the written standard

**Lesson:** [Security Baselines, Policies & Hardening Standards](https://learnsome.tech/learn/cybersecurity-course/m02l01) (lesson 2.1, module 2: Governance, Risk & Compliance) · Pro  
**Check:** Read along

## Goal

You can trace a security policy down to a testable baseline, prove what a server really enforces, and put changes to that baseline through version-controlled change management.

In the lesson: Now turn that into a check you can schedule. The program loads the standard from a text file, one keyword and value per line, written in lower case because that is how sshd prints them. The file carries its own identifier, version, owner and approval date, so an auditor can see which approved document the server is measured against. Next it builds the same test config, runs sshd with dash capital T and turns the effective configuration into a lookup of keyword to value. Finally it compares each setting and exits with status one if anything fails, so a pipeline or a nightly job goes red. Here is the result. Root login and the attempt limit pass. Password login fails, because of the drop-in, and X eleven forwarding fails because Ubuntu's stock file turns it on and nobody changed it. That second one is drift from day one.

## Files

- [`starter/audit.py`](starter/audit.py): the listing from the lesson
- [`starter/ssh_standard.txt`](starter/ssh_standard.txt)
- [`starter/sshd_config`](starter/sshd_config)
- [`starter/sshd_config.d/50-cloud-init.conf`](starter/sshd_config.d/50-cloud-init.conf)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/audit.py` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–8: loads the standard
   - Lines 9–15: effective configuration
   - Lines 16–22: compares each setting

## How to check

**Read along.** It needs root access or system services (systemd, firewall rules, raw sockets) that the lab sandbox does not allow. Run it on a Linux machine or VM you control.

There is nothing to check: `./check m02l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
