# Cybersecurity Fundamentals, GRC & Cryptography — lesson m04l04 — Asset Lifecycle Management & Media Sanitization
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m04l04
# © LearnSome.tech
import sqlite3

def text_in_file(path, text):
    return text.encode() in open(path, "rb").read()

for mode in ("OFF", "ON"):
    path = f"hr-{mode.lower()}.db"
    db = sqlite3.connect(path)
    db.execute(f"PRAGMA secure_delete={mode}")
    db.execute("CREATE TABLE staff (name TEXT, note TEXT)")
    db.execute("INSERT INTO staff VALUES ('Dan Reyes', 'final warning')")
    db.commit()
    db.execute("DELETE FROM staff")
    db.commit()
    rows = db.execute("SELECT count(*) FROM staff").fetchone()[0]
    db.close()
    print(f"secure_delete {mode}: rows visible {rows},",
          "note still in file:", text_in_file(path, "final warning"))
