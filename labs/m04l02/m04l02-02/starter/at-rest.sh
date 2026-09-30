sqlite3 customers.db "CREATE TABLE customer (id INTEGER, email TEXT, card TEXT);
  INSERT INTO customer VALUES (1, 'alice@example.com', '4111111111111111');"
echo "readable strings in customers.db:"
strings -n 12 customers.db
openssl rand -hex 32 > db.key   # stand-in for a key held in a key manager
openssl enc -aes-256-cbc -pbkdf2 -pass file:db.key \
  -in customers.db -out customers.db.enc
for f in customers.db customers.db.enc; do
  if grep -q "alice@example.com" "$f"; then echo "$f: email visible"
  else echo "$f: email not found"; fi
done
openssl enc -d -aes-256-cbc -pbkdf2 -pass file:db.key \
  -in customers.db.enc -out restored.db
sqlite3 restored.db "SELECT id, email FROM customer;"
