# Cybersecurity Fundamentals, GRC & Cryptography — lesson m05l03 — Backup Architectures: 3-2-1, Immutability & Air-Gaps
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m05l03
# © LearnSome.tech
import os, tarfile
from datetime import datetime

def at(day, hour):                  # a fixed March week, no wall clock
    return datetime(2026, 3, day, hour).timestamp()

def archive(name, since):           # take files modified after `since`
    with tarfile.open(name, "w") as tar:
        for f in sorted(os.listdir("data")):
            if os.path.getmtime("data/" + f) > since:
                tar.add("data/" + f, arcname=f)
    return " ".join(tarfile.open(name).getnames()) or "-"
edits = {9: ["ledger.csv", "logo.png", "notes.txt"], 10: ["ledger.csv"],
         11: ["notes.txt"], 12: ["ledger.csv", "plan.txt"]}
os.makedirs("data", exist_ok=True)
for day, names in edits.items():
    for f in names:
        open("data/" + f, "a").write(f"edited on the {day}th\n")
        os.utime("data/" + f, (at(day, 12), at(day, 12)))
    inc = archive(f"inc-{day}.tar", at(day - 1, 20) if day > 9 else 0)
    diff = archive(f"diff-{day}.tar", at(9, 20) if day > 9 else 0)
    print(f"Mar {day:2}  inc {inc:30} diff {diff}")
