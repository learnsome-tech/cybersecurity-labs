# Cybersecurity Fundamentals, GRC & Cryptography — lesson m01l02 — Threat Actors, Motivations & Cyber Kill Chain
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m01l02
# © LearnSome.tech
import csv
from datetime import datetime

PHASES = ["reconnaissance", "weaponisation", "delivery", "exploitation",
          "installation", "command and control", "actions on objectives"]
rows = list(csv.DictReader(open("timeline.csv")))

for phase in PHASES:
    seen = [r for r in rows if r["phase"] == phase]
    if not seen:
        print(f"{phase:<22} nothing in our logs")
        continue
    alerted = any(r["alerted"] == "yes" for r in seen)
    print(f"{phase:<22} {seen[0]['time']}", "alert" if alerted else "missed")

start = next(r["time"] for r in rows if r["phase"] == "delivery")
alert = next(r["time"] for r in rows if r["alerted"] == "yes")
gap = datetime.fromisoformat(alert) - datetime.fromisoformat(start)
print("first alert at", alert, "which is", gap, "after delivery")
