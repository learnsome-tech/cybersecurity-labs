import csv
import hashlib
import random

SEED = 20260930                         # chosen and recorded before sampling
START, END = "2026-04-01", "2026-09-30"  # the audit period

raw = open("changes.csv", "rb").read()
rows = list(csv.DictReader(raw.decode().splitlines()))
population = [r["number"] for r in rows
              if START <= r["implemented_at"][:10] <= END]

picked = sorted(random.Random(SEED).sample(population, 15))
open("sample.txt", "w").write("\n".join(picked) + "\n")

print("population file sha256:")
print(hashlib.sha256(raw).hexdigest())
print("rows in file:", len(rows), "in period:", len(population))
print("seed:", SEED, "sample size:", len(picked))
for i in range(0, 15, 5):
    print(" ".join(picked[i:i + 5]))
