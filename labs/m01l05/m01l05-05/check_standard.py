# Cybersecurity Fundamentals, GRC & Cryptography — lesson m01l05 — Security Governance vs Security Management
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m01l05
# © LearnSome.tech
import glob

STANDARD = {"permitrootlogin": "no", "passwordauthentication": "no",
            "x11forwarding": "no", "maxauthtries": 4}

# sshd keeps the first value it reads for each keyword
def effective(path, found):
    for line in open(path):
        words = line.split("#")[0].split()
        if words and words[0].lower() == "include":
            for part in sorted(glob.glob(words[1])):
                effective(part, found)
        elif words:
            found.setdefault(words[0].lower(), (" ".join(words[1:]), path))
    return found

config = effective("sshd_config", {})
for key, rule in STANDARD.items():
    value, source = config.get(key, ("unset", "built-in default"))
    ok = int(value) <= rule if isinstance(rule, int) else value == rule
    print("pass" if ok else "fail", key, value, "from", source)
