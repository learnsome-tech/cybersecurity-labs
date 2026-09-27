# Cybersecurity Fundamentals, GRC & Cryptography — lesson m02l01 — Security Baselines, Policies & Hardening Standards
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m02l01
# © LearnSome.tech
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1
export GIT_AUTHOR_DATE=2026-02-10T09:00Z GIT_COMMITTER_DATE=2026-02-10T09:00Z
git init -q -b main standards && cd standards
git config user.name "Priya Shah" && git config user.email priya@example.com
cp ../ssh_standard.txt . && git add .
git commit -qm "SSH standard v3 (CAB-118)"

# CHG-2291: approved by the CAB on 3 March, backout plan is git revert
export GIT_AUTHOR_DATE=2026-03-05T21:00Z GIT_COMMITTER_DATE=2026-03-05T21:00Z
sed 's/^maxauthtries 4/maxauthtries 3/' ssh_standard.txt > new
mv new ssh_standard.txt
git commit -qam "Lower maxauthtries to 3 (CHG-2291)"

git log --date=short --format='%h %ad %an: %s'
git diff -U0 HEAD~1 | grep '^[-+][a-z]'
