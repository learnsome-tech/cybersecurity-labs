# m04l04-03 · Reconcile the inventory against the leases

**Lesson:** [Asset Lifecycle Management & Media Sanitization](https://learnsome.tech/learn/cybersecurity-course/m04l04) (lesson 4.4, module 4: Data Protection & Privacy) · Pro  
**Check:** Graded

## Goal

You can reconcile an asset inventory against what is really on the network and pick a sanitisation method that matches the media and the data on it.

In the lesson: The first loop pulls the address, hardware address and host name from each lease with regular expressions; the file format is simple enough for that. Then the program reads the inventory, a C S V with the asset tag, hardware address, owner, classification and status of each device. Next it compares each device seen on the network with its inventory record. The last loop goes the other way and looks for assets that should be in use but never appeared. Each output line is a job for someone. L T zero four one two is fine. The unknown desktop is unmanaged, so nobody knows what data it holds or whether it is patched. The worst is L T zero three zero one, recorded as disposed but still online with confidential data. The disposal process has failed. And the laptop assigned to R Ahmed has not been seen, so find out why.

## Files

- [`starter/dhcpd.leases`](starter/dhcpd.leases)
- [`starter/inventory.csv`](starter/inventory.csv)
- [`starter/reconcile.py`](starter/reconcile.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-03/starter`
2. Read `reconcile.py` the way the lesson builds it:
   - Lines 1–7: The first loop
   - Lines 8–9: reads the inventory
   - Lines 10–17: compares each device
   - Lines 18–20: The last loop
3. Run it: `python3 reconcile.py`.
4. Check it from the repository root: `./check m04l04-03`.

## Expected output

```text
192.0.2.41 LT-0412: ok, j.mensah, Confidential
192.0.2.57 LT-0301: recorded as disposed but online, recover it
192.0.2.88 DESKTOP-7Q2K9LM: not in inventory, unmanaged device
LT-0587: assigned to r.ahmed, not seen
```

## How to check

`./check m04l04-03` copies `starter/` into a scratch directory and runs `python3 reconcile.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
