# m05l03-05 · Immutability enforced by the storage

**Lesson:** [Backup Architectures: 3-2-1, Immutability & Air-Gaps](https://learnsome.tech/learn/cybersecurity-course/m05l03) (lesson 5.3, module 5: Resilience & Disaster Recovery) · Pro  
**Check:** Read along

## Goal

You can design a backup scheme that survives ransomware, explaining incremental and differential chains, 3-2-1-1-0, immutability and air gaps, and prove a restore is intact.

In the lesson: Real immutability is enforced by a system the attacker's credentials cannot change. Amazon S three Object Lock is one example, and this is the configuration document you pass to its put object lock configuration call. Object Lock works on versioned buckets. With a default retention rule, every new object version is protected for thirty days. The mode matters. In governance mode, users granted a special bypass permission can still delete early, which helps with mistakes but means a stolen admin role can too. In compliance mode, nobody can delete the version or shorten the retention before it expires, not even the root user of the account. A legal hold is separate: it has no end date and stays until someone with permission removes it. The trade-off is real, because compliance mode also stops you fixing your own mistake.

## Files

- [`starter/object-lock.json`](starter/object-lock.json): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/object-lock.json` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–2: works on versioned buckets
   - Lines 3–5: protected for thirty days
   - Lines 6–9: the mode matters
3. Notes from the lesson:
   - Line 6: COMPLIANCE: nobody, root included, can delete early

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l03-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
