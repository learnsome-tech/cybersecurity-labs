# Cybersecurity Fundamentals, GRC & Cryptography — lesson m02l01 — Security Baselines, Policies & Hardening Standards
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m02l01
# © LearnSome.tech
echo "sshd_config says:"
grep -Ei '^(PermitRootLogin|PasswordAuthentication)' sshd_config

# Point the Include at our local copy, then ask sshd what it will enforce
sed "s|/etc/ssh/|$PWD/|" sshd_config > test_config
ssh-keygen -q -t ed25519 -N '' -f hostkey
echo "sshd -T says:"
sshd -T -f test_config -h hostkey |
  grep -Ei '^(permitrootlogin|passwordauthentication)'
