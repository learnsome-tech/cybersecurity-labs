# Cybersecurity Fundamentals, GRC & Cryptography — lesson m03l02 — Asymmetric Cryptography: RSA, ECC & Diffie-Hellman
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m03l02
# © LearnSome.tech
set -e
for who in alice bob; do
  openssl genpkey -algorithm X25519 -out "$who.key"
  openssl pkey -in "$who.key" -pubout -out "$who.pub"
done

# each side: its own private key plus the other side's public key
openssl pkeyutl -derive -inkey alice.key -peerkey bob.pub -out alice.bin
openssl pkeyutl -derive -inkey bob.key -peerkey alice.pub -out bob.bin

der=$(openssl pkey -pubin -in bob.pub -outform DER | wc -c | tr -d ' ')
echo "Bob's public key on the wire: $der bytes"
echo "shared secret: $(wc -c < alice.bin | tr -d ' ') bytes"
cmp -s alice.bin bob.bin && echo "Alice and Bob derived the same secret"
