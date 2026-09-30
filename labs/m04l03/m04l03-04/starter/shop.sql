-- Data inventory: each table states its purpose and how long it is kept
CREATE TABLE customers (id INTEGER PRIMARY KEY, email TEXT, name TEXT,
  created TEXT);                     -- account: kept while account is open
CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER,
  total_pence INTEGER, placed TEXT); -- tax records: kept six years
CREATE TABLE marketing (customer_id INTEGER, email TEXT,
  consent_given TEXT);               -- newsletter: until consent withdrawn
CREATE TABLE support_tickets (id INTEGER PRIMARY KEY, email TEXT,
  note TEXT, closed TEXT);           -- support: kept two years after close
INSERT INTO customers VALUES (1, 'alice@example.com', 'Alice Hart',
  '2019-05-02'), (2, 'ben@example.org', 'Ben Osei', '2019-11-20'),
  (3, 'chloe@example.com', 'Chloe Park', '2024-02-11');
INSERT INTO orders VALUES (1, 1, 4599, '2019-06-01'),
  (2, 1, 1250, '2025-12-03'), (3, 2, 8900, '2020-01-15'),
  (4, 3, 2300, '2024-03-01'), (5, 2, 1999, '2026-08-30');
INSERT INTO marketing VALUES (1, 'alice@example.com', '2019-05-02'),
  (3, 'chloe@example.com', '2024-02-11');
INSERT INTO support_tickets VALUES
  (1, 'alice@example.com', 'Parcel left with neighbour', '2025-01-09'),
  (2, 'ben@example.org', 'Refund for damaged kettle', '2023-04-18'),
  (3, 'alice@example.com', 'Change delivery address', '2026-07-02');
