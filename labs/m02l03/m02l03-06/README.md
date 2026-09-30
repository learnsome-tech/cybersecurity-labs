# m02l03-06 · Testing a pod manifest against the restricted profile

**Lesson:** [Security Frameworks: NIST CSF 2.0, ISO 27001 & CIS](https://learnsome.tech/learn/cybersecurity-course/m02l03) (lesson 2.3, module 2: Governance, Risk & Compliance) · Pro  
**Check:** Graded

## Goal

You can explain how NIST CSF 2.0, ISO 27001 and the CIS Controls differ, use a crosswalk to find evidence gaps across all three, and test a Kubernetes pod against the restricted Pod Security Standard.

In the lesson: Here is that check written out. Pod Security admission lives in the Kubernetes A P I server and there is no cluster here, so these are a few lines of Python applying the same restricted rules to a real pod manifest in J S O N, a format kubectl also accepts. The pod sets run as non root and a runtime default seccomp profile once, at pod level. The helper gives a container's own setting priority over the pod's. Then come six checks from the restricted profile: no privilege escalation, non root, not user zero, drop all capabilities, add nothing but binding low ports, and a seccomp profile. The program prints a verdict per container. Run it. The app passes. The log shipper sidecar fails four checks. It runs as user zero and adds S Y S admin, which is close to full root on the node.

## Files

- [`starter/check_pod.py`](starter/check_pod.py): the listing from the lesson
- [`starter/pod.json`](starter/pod.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-06/starter`
2. Read `check_pod.py` the way the lesson builds it:
   - Lines 1–4: a real pod manifest
   - Lines 5–8: the helper
   - Lines 9–19: six checks from the restricted profile
   - Lines 20–22: prints a verdict
3. Notes from the lesson:
   - Line 17: SYS_ADMIN is close to root on the node
4. Run it: `python3 check_pod.py`.
5. Check it from the repository root: `./check m02l03-06`.

## Expected output

```text
app meets restricted
log-shipper violates restricted
  needs no privilege escalation
  needs runAsUser not 0
  needs drop ALL capabilities
  needs add only NET_BIND_SERVICE
```

## How to check

`./check m02l03-06` copies `starter/` into a scratch directory and runs `python3 check_pod.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
