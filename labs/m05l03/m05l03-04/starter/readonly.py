import os, stat

os.makedirs("backups", exist_ok=True)
path = "backups/ledger-2026-03-12.csv"
with open(path, "w") as f:
    f.write("invoice,amount\nINV-1001,420.00\n")
os.chmod(path, 0o444)               # read-only for everyone
print(path, stat.filemode(os.stat(path).st_mode))

# ransomware running as the same account that writes the backups
try:
    open(path, "w")
except PermissionError as err:
    print("overwrite refused:", err.strerror)
data = open(path, "rb").read()
with open(path + ".locked", "wb") as f:
    f.write(bytes(b ^ 0x5A for b in data))   # stand-in for real encryption
os.remove(path)                     # needs write access to the folder only
print("left in backups:", os.listdir("backups"))
