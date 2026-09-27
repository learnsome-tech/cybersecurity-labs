# Cybersecurity Fundamentals, GRC & Cryptography — lesson m06l02 — Enterprise Risk Registers & Treatment Plans
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m06l02
# © LearnSome.tech
import csv

APPETITE = 8     # board-approved: residual above 8 needs treatment or sign-off

rows = list(csv.DictReader(open("register.csv")))
for r in rows:
    r["inherent"] = int(r["L"]) * int(r["I"])      # before controls
    r["residual"] = int(r["rL"]) * int(r["rI"])    # with controls working

rows.sort(key=lambda r: r["residual"], reverse=True)
print("id    inh  res  treatment  owner")
for r in rows:
    flag = "above appetite" if r["residual"] > APPETITE else ""
    print(f"{r['id']}  {r['inherent']:>3}  {r['residual']:>3}  "
          f"{r['treatment']:9}  {r['owner']:5}  {flag}")
