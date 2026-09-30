import hashlib
import json

entries = [{"from": "alice", "to": "bob", "amount": 5},
           {"from": "bob", "to": "chen", "amount": 2},
           {"from": "chen", "to": "dara", "amount": 1}]


def links(entries: list) -> list:
    prev, out = "0" * 64, []
    for entry in entries:     # each link hashes the previous link too
        data = prev + json.dumps(entry, sort_keys=True)
        prev = hashlib.sha256(data.encode()).hexdigest()
        out.append(prev)
    return out


published = links(entries)           # copies held by every participant
entries[0]["amount"] = 50            # someone quietly rewrites history
for i, (old, new) in enumerate(zip(published, links(entries))):
    status = "ok" if old == new else "broken"
    print(f"entry {i}: published {old[:12]}, recomputed {new[:12]} {status}")
