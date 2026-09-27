# Cybersecurity Fundamentals, GRC & Cryptography — lesson m03l05 — Post-Quantum Cryptography & Key Lifecycles
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m03l05
# © LearnSome.tech
set -e
# Bob publishes an ML-KEM-768 public key (FIPS 203)
openssl genpkey -algorithm ML-KEM-768 -out bob.key
openssl pkey -in bob.key -pubout -out bob.pub

# Alice encapsulates: a fresh random secret, plus a ciphertext only Bob opens
openssl pkeyutl -encap -pubin -inkey bob.pub -secret alice.bin -out ct.bin
# Bob decapsulates the ciphertext with his private key
openssl pkeyutl -decap -inkey bob.key -in ct.bin -secret bob.bin

bytes() { wc -c < "$1" | tr -d ' '; }
openssl pkey -pubin -in bob.pub -outform DER -out bob.der
echo "public key, DER:     $(bytes bob.der) bytes"
echo "ciphertext to Bob:   $(bytes ct.bin) bytes"
echo "shared secret:       $(bytes bob.bin) bytes"
cmp -s alice.bin bob.bin && echo "Alice and Bob hold the same secret"
