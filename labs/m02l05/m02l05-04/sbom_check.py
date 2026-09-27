# Cybersecurity Fundamentals, GRC & Cryptography — lesson m02l05 — Vendor & Third-Party Risk Management Programs
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m02l05
# © LearnSome.tech
import json

def ver(v):  # "2.14.1" -> (2, 14, 1), so versions compare as numbers
    return tuple(int(part) for part in v.split("."))

bom = json.load(open("forwarder.cdx.json"))
advisories = json.load(open("advisories.json"))
app = bom["metadata"]["component"]
print(f"{app['name']} {app['version']}: {len(bom['components'])} components")

for c in bom["components"]:
    name = f"{c.get('group', '')}:{c['name']}".lstrip(":")
    for a in advisories:
        if a["package"] != name:
            continue
        affected = ver(a["introduced"]) <= ver(c["version"]) < ver(a["fixed"])
        verdict = f"affected below {a['fixed']}" if affected else "not affected"
        print(f"  {a['id']} {name} {c['version']}: {verdict}")
