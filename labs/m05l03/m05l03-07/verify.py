# Cybersecurity Fundamentals, GRC & Cryptography — lesson m05l03 — Backup Architectures: 3-2-1, Immutability & Air-Gaps
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m05l03
# © LearnSome.tech
import hashlib, json, os

def sha256(path):
    with open(path, "rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()

os.makedirs("restore", exist_ok=True)
for name, text in {"ledger.csv": "invoice,amount\nINV-1001,420.00\n",
                   "notes.txt": "board meeting moved to Friday\n"}.items():
    with open("restore/" + name, "w") as f:
        f.write(text)
# at backup time: one digest per file, kept with the offline copy
manifest = {n: sha256("restore/" + n) for n in sorted(os.listdir("restore"))}
with open("manifest.json", "w") as f:
    json.dump(manifest, f, indent=1)

with open("restore/ledger.csv", "a") as f:   # a silent change in storage
    f.write("INV-1002,9999.00\n")
for name, want in json.load(open("manifest.json")).items():
    got = sha256("restore/" + name)
    print(name, "ok" if got == want else f"differs: {want[:12]} vs {got[:12]}")
