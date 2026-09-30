# m04l04 · Asset Lifecycle Management & Media Sanitization

Module 4: Data Protection & Privacy · lesson 4.4 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m04l04)

**Goal:** You can reconcile an asset inventory against what is really on the network and pick a sanitisation method that matches the media and the data on it.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l04-02](m04l04-02/) | What the DHCP server says is on the network | Read along |
| [m04l04-03](m04l04-03/) | Reconcile the inventory against the leases | Graded |
| [m04l04-05](m04l04-05/) | Deleting a record is not sanitising it | Graded |
| [m04l04-06](m04l04-06/) | Cryptographic erase: destroy the key, not the disk | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Run the checks on your own data

1. Add a fourth lease for LT-0587 to dhcpd.leases and predict the reconciler's new output.
2. Add a lease with no client-hostname line and check the program still reports it.
3. In delete.py, try PRAGMA secure_delete=FAST and explain what the output tells you.
4. In crypto-erase.sh, keep a copy of media.key before replacing it; what does that undo?

> **Hint:** FAST overwrites content in pages it touches but may leave data in the free list.

## Check yourself

- The reconciler reported LT-0301 as recorded as disposed but online. What does that finding most likely mean for the data on it?
- Why is overwriting a solid state drive from the operating system not a reliable purge, when it is on a magnetic disk?
- In delete.py, SELECT count(*) returned zero in both databases. Why did the raw file check still find the note when secure_delete was off?
- After the media key was replaced in crypto-erase.sh, disk.img was byte for byte unchanged. Why is the data still considered sanitised, and what would undo that?
- A departing manager's laptop is due for disposal, but legal has placed a hold on her mailbox. What should happen before anything is wiped?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
