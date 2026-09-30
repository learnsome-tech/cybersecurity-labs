import subprocess
from pathlib import Path

want = {}
for line in Path("ssh_standard.txt").read_text().splitlines():
    if line and not line.startswith("#"):
        key, value = line.split(maxsplit=1)
        want[key] = value

conf = Path("sshd_config").read_text()
Path("test_config").write_text(conf.replace("/etc/ssh/", f"{Path.cwd()}/"))
subprocess.run(["ssh-keygen", "-q", "-t", "ed25519", "-N", "", "-f", "hostkey"])
dump = subprocess.run(["sshd", "-T", "-f", "test_config", "-h", "hostkey"],
                      capture_output=True, text=True, check=True).stdout
got = dict(line.partition(" ")[::2] for line in dump.splitlines())

failed = [k for k in want if got.get(k) != want[k]]
for key in want:
    verdict = "fails" if key in failed else "ok"
    print(f"{key:24} standard {want[key]:3} server {got[key]:3} {verdict}")
print(f"{len(failed)} of {len(want)} settings fail SEC-STD-SSH-01")
raise SystemExit(1 if failed else 0)
