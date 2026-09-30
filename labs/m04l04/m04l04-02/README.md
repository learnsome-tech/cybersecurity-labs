# m04l04-02 · What the DHCP server says is on the network

**Lesson:** [Asset Lifecycle Management & Media Sanitization](https://learnsome.tech/learn/cybersecurity-course/m04l04) (lesson 4.4, module 4: Data Protection & Privacy) · Pro  
**Check:** Read along

## Goal

You can reconcile an asset inventory against what is really on the network and pick a sanitisation method that matches the media and the data on it.

In the lesson: The inventory is what you believe. For what is true, start with a source that records every device joining the network. Here it is the lease file from an I S C D H C P server, the plain text database it keeps of every address it has handed out. Each block is one lease: the address, when it started, whether it is active, the device's hardware address, and the host name the device announced about itself. The first is a laptop tagged L T zero four one two. The second lease is for laptop L T zero three zero one. The third has a host name in the style Windows generates when nobody renames a new machine. Switch tables, endpoint agents and cloud A P Is give you the same kind of evidence, and a mature programme compares several of them.

## Files

- [`starter/dhcpd.leases`](starter/dhcpd.leases): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/dhcpd.leases` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1: the lease file
   - Lines 2–7: Each block is one lease
   - Lines 8–13: The second lease
   - Lines 14–19: The third

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
