import hashlib

users = {"amara": "Summer2026!", "ben": "Summer2026!", "chen": "t4k-Ow1-riv3r"}
wordlist = ["123456", "password", "Winter2025!", "Summer2026!", "qwerty"]

# the mistake: one fast, unsalted hash per password
leaked = {u: hashlib.sha256(p.encode()).hexdigest() for u, p in users.items()}
print("amara and ben share a hash:", leaked["amara"] == leaked["ben"])
table = {hashlib.sha256(w.encode()).hexdigest(): w for w in wordlist}
for user, digest in leaked.items():
    print(f"  {user}: {table.get(digest, 'not in the wordlist')}")

# the fix: a unique random salt per user, and a slow, memory-hard function
N, R = 2**14, 8
def store(password: str, salt: bytes) -> str:
    return hashlib.scrypt(password.encode(), salt=salt, n=N, r=R, p=1).hex()

salts = {"amara": bytes(16), "ben": bytes(15) + b"\x01"}  # demo; use os.urandom
for user, salt in salts.items():
    print(f"  {user}: scrypt {store(users[user], salt)[:32]}...")
print("memory per guess:", 128 * R * N // 2**20, "MiB")
