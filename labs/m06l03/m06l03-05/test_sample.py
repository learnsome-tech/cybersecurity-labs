# Cybersecurity Fundamentals, GRC & Cryptography — lesson m06l03 — Internal Audits, Sampling & Evidence Chains
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m06l03
# © LearnSome.tech
import csv

sample = set(open("sample.txt").read().split())
out = open("results.csv", "w")
out.write("number,result,reason\n")
failed = 0
for r in csv.DictReader(open("changes.csv")):
    if r["number"] not in sample:
        continue
    if not r["approver"]:
        reason = "no approval recorded"
    elif r["approver"] == r["implementer"]:
        reason = "approved by the person who deployed it"
    elif r["approved_at"] >= r["implemented_at"]:
        reason = "approved after it was deployed"
    else:
        reason = ""
    out.write(f"{r['number']},{'exception' if reason else 'pass'},{reason}\n")
    if reason:
        failed += 1
        print(r["number"], reason, r["approved_at"], r["implemented_at"])
print(f"{failed} exception(s) in {len(sample)} tested; tolerable exceptions: 0")
