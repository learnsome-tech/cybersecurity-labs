import hashlib

a = b"Transfer 100 GBP to account 12345678"
b = b"Transfer 900 GBP to account 12345678"   # one character changed
big = bytes(10_000_000)                        # ten megabytes of zeros

for name in ("sha256", "sha3_256"):
    da = hashlib.new(name, a).digest()
    db = hashlib.new(name, b).digest()
    differ = bin(int.from_bytes(da) ^ int.from_bytes(db)).count("1")
    print(f"{name} of a: {da.hex()[:40]}...")
    print(f"{name} of b: {db.hex()[:40]}...")
    print(f"  {differ} of 256 bits differ")
    size = len(hashlib.new(name, big).digest())
    print(f"  ten megabytes in, {size} bytes out")
