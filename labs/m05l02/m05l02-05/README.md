# m05l02-05 · What distance does to every commit

**Lesson:** [Disaster Recovery Sites: Hot, Warm & Cold](https://learnsome.tech/learn/cybersecurity-course/m05l02) (lesson 5.2, module 5: Resilience & Disaster Recovery) · Pro  
**Check:** Graded

## Goal

You can choose between hot, warm and cold recovery sites by working out their real recovery time and data loss against a system's RTO and RPO, and plan how to test the choice.

In the lesson: Here is the physics. The program holds approximate coordinates for four candidate sites and a London primary, and uses the haversine formula for the great circle distance between them. Light in optical fibre travels at about two thirds of its speed in a vacuum, roughly two hundred kilometres every millisecond. Double the distance for the round trip and you have a floor on the delay: real fibre routes are longer than the straight line, and every switch adds more. Slough, just over thirty kilometres away, costs a third of a millisecond. Frankfurt costs over six. Ashburn in Virginia costs almost sixty, which caps a single writer that waits on each commit at about seventeen commits a second. That is why transatlantic replicas are almost always asynchronous.

## Files

- [`starter/latency.py`](starter/latency.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-05/starter`
2. Read `latency.py` the way the lesson builds it:
   - Lines 1–6: approximate coordinates
   - Lines 7–12: the haversine formula
   - Lines 13–18: double the distance for the round trip
3. Run it: `python3 latency.py`.
4. Check it from the repository root: `./check m05l02-05`.

## Expected output

```text
Slough         33 km  min RTT   0.3 ms  at most  3,074 commits/s per writer
Manchester    261 km  min RTT   2.6 ms  at most    382 commits/s per writer
Frankfurt     638 km  min RTT   6.4 ms  at most    157 commits/s per writer
Ashburn     5,917 km  min RTT  59.2 ms  at most     17 commits/s per writer
```

## How to check

`./check m05l02-05` copies `starter/` into a scratch directory and runs `python3 latency.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
