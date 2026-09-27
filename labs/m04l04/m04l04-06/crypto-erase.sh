# Cybersecurity Fundamentals, GRC & Cryptography — lesson m04l04 — Asset Lifecycle Management & Media Sanitization
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m04l04
# © LearnSome.tech
# A file stands in for a self-encrypting drive; openssl for its engine.
printf 'Payroll export: j.mensah, r.ahmed\n' > plain.txt
openssl rand -hex 32 > media.key
openssl rand -hex 16 > media.iv
openssl enc -aes-256-cbc -K "$(cat media.key)" -iv "$(cat media.iv)" \
  -in plain.txt -out disk.img
rm plain.txt
cp disk.img before.img
read_disk() {
  openssl enc -d -aes-256-cbc -K "$(cat media.key)" -iv "$(cat media.iv)" \
    -in disk.img 2>/dev/null | grep -q Payroll \
    && echo readable || echo unreadable
}
echo "with the original media key: $(read_disk)"
openssl rand -hex 32 > media.key   # cryptographic erase: replace the key
echo "after the key is replaced: $(read_disk)"
cmp -s disk.img before.img && echo "encrypted blocks on disk: unchanged"
