set -e
printf 'release 2.4.1, approved for production\n' > release.txt
openssl genpkey -quiet -algorithm RSA -pkeyopt rsa_keygen_bits:3072 -out rsa.key
openssl genpkey -quiet -algorithm ED25519 -out ed.key

check() {  # $1 = key name, $2 = extra flags
  openssl pkeyutl -verify -rawin $2 -pubin -inkey "$1.pub" \
    -in release.txt -sigfile "$1.sig" 2>/dev/null || true
}
for k in rsa ed; do
  flags=""; [ "$k" = rsa ] && flags="-digest sha256"
  openssl pkey -in "$k.key" -pubout -out "$k.pub"
  openssl pkeyutl -sign -rawin $flags -inkey "$k.key" \
    -in release.txt -out "$k.sig"
  pub=$(openssl pkey -pubin -in "$k.pub" -outform DER | wc -c | tr -d ' ')
  sig=$(wc -c < "$k.sig" | tr -d ' ')
  echo "$k: public key $pub bytes, signature $sig bytes"
  echo "  $(check $k "$flags")"
done
sed -i.bak 's/2.4.1/2.4.2/' release.txt   # one character changed
echo "after the edit, rsa: $(check rsa '-digest sha256')"
echo "after the edit, ed:  $(check ed)"
