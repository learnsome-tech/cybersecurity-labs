# m02l01-03 · What the file says versus what sshd enforces

**Lesson:** [Security Baselines, Policies & Hardening Standards](https://learnsome.tech/learn/cybersecurity-course/m02l01) (lesson 2.1, module 2: Governance, Risk & Compliance) · Pro  
**Check:** Read along

## Goal

You can trace a security policy down to a testable baseline, prove what a server really enforces, and put changes to that baseline through version-controlled change management.

In the lesson: Here is the check a lot of audits really run. The script reads the main file with grep and prints the two lines that matter. Then it asks sshd itself. The dash capital T flag makes the daemon parse its configuration, follow every Include, fill in defaults and print the result, without starting a server. We point the Include at our local copy and hand it a throwaway host key so it works without root. Run it. The file says no passwords. sshd says passwords are allowed. The culprit is a drop-in called fifty cloud init dot conf, the kind cloud-init on Ubuntu writes to switch password login on. It is included at the top of the main file, and for most keywords sshd keeps the first value it reads. The grep was right about the file. It answered the wrong question.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/effective.sh`](starter/effective.sh): the listing from the lesson
- [`starter/sshd_config`](starter/sshd_config)
- [`starter/sshd_config.d/50-cloud-init.conf`](starter/sshd_config.d/50-cloud-init.conf)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/effective.sh` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–2: reads the main file with grep
   - Lines 3–9: then it asks sshd itself
3. Notes from the lesson:
   - Line 8: -T: parse config, follow Includes, apply defaults, print, exit
4. On a machine that has what it needs, the lesson ran it with:

   ```sh
   bash effective.sh
   ```

## How to check

**Read along.** It needs root access or system services (systemd, firewall rules, raw sockets) that the lab sandbox does not allow. Run it on a Linux machine or VM you control.

There is nothing to check: `./check m02l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
