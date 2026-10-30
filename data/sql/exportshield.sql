-- =====================================================================
-- ExportShield Insurance - training dataset for BA Academy (modules 09 and 10)
-- SQLite script. Everything here is FICTIONAL: company names, people,
-- company IDs (ICO values deliberately fail the Czech checksum), amounts.
-- Country names are real, but risk categories are illustrative only and
-- are NOT official country risk classifications.
-- Data snapshot ("today" in the exercises): 2026-09-30.
-- Dates are ISO text 'YYYY-MM-DD'. Amounts are in the row's currency.
-- Premium rate is a fraction of insured turnover (0.0035 = 0.35 %).
--
-- INSTRUCTOR NOTES - data-quality issues planted on purpose:
--  1. customers.id 3 and 15: same company twice (same ICO, different spelling)  [uniqueness]
--  2. customers.id 9: ICO has only 7 digits                                    [validity]
--  3. buyers.id 24: country_code is NULL                                       [completeness]
--  4. policies.id 19: end_date is before start_date                            [validity]
--  5. credit_limits.id 19: decided_on is before requested_on                [consistency]
--  6. credit_limits.id 6: status REJECTED but approved_amount > 0          [consistency]
--  7. invoices.id 2 and 3: duplicate invoice_no 'INV-2026-01002'            [uniqueness]
--  8. invoices.id 31: due_date is before issue_date                   [validity]
--  9. claims.id 15: claim on invoice 9, which already has a paid_date [consistency]
-- 10. claims.id 8: indemnity_amount is higher than claimed_amount  [accuracy]
-- 11. claims.id 7: status PAID but no row in payments           [consistency]
-- Credit limits with status REQUESTED are open (decision pending) - not an error.
-- =====================================================================


DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS claims;
DROP TABLE IF EXISTS invoices;
DROP TABLE IF EXISTS credit_limits;
DROP TABLE IF EXISTS policies;
DROP TABLE IF EXISTS buyers;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries (
  code           TEXT PRIMARY KEY,          -- ISO 3166-1 alpha-2
  name           TEXT NOT NULL,
  risk_category  INTEGER NOT NULL           -- 1 = lowest risk, 7 = highest (illustrative values)
);

CREATE TABLE customers (                    -- exporters = policyholders
  id             INTEGER PRIMARY KEY,
  name           TEXT NOT NULL,
  ico            TEXT,                      -- Czech company ID, 8 digits (fictional)
  city           TEXT,
  segment        TEXT,                      -- MICRO / SME / CORPORATE
  onboarded_on   TEXT                       -- YYYY-MM-DD
);

CREATE TABLE buyers (                       -- foreign customers of the exporters
  id             INTEGER PRIMARY KEY,
  name           TEXT NOT NULL,
  country_code   TEXT REFERENCES countries(code),
  sector         TEXT
);

CREATE TABLE policies (
  id             INTEGER PRIMARY KEY,
  customer_id    INTEGER NOT NULL REFERENCES customers(id),
  policy_no      TEXT NOT NULL,
  start_date     TEXT NOT NULL,
  end_date       TEXT NOT NULL,
  status         TEXT NOT NULL,             -- ACTIVE / EXPIRED / CANCELLED
  premium_rate   REAL                       -- share of insured turnover, 0.0035 = 0.35 %
);

CREATE TABLE credit_limits (
  id               INTEGER PRIMARY KEY,
  policy_id        INTEGER NOT NULL REFERENCES policies(id),
  buyer_id         INTEGER NOT NULL REFERENCES buyers(id),
  requested_amount REAL NOT NULL,
  approved_amount  REAL,                    -- NULL while REQUESTED
  currency         TEXT NOT NULL,
  status           TEXT NOT NULL,           -- REQUESTED / APPROVED / REDUCED / REJECTED
  requested_on     TEXT NOT NULL,
  decided_on       TEXT,                    -- NULL while REQUESTED
  underwriter      TEXT
);

CREATE TABLE invoices (
  id             INTEGER PRIMARY KEY,
  policy_id      INTEGER NOT NULL REFERENCES policies(id),
  buyer_id       INTEGER NOT NULL REFERENCES buyers(id),
  invoice_no     TEXT NOT NULL,
  amount         REAL NOT NULL,
  currency       TEXT NOT NULL,
  issue_date     TEXT NOT NULL,
  due_date       TEXT NOT NULL,
  paid_date      TEXT                       -- NULL = not paid (yet)
);

CREATE TABLE claims (
  id               INTEGER PRIMARY KEY,
  invoice_id       INTEGER NOT NULL REFERENCES invoices(id),
  notified_on      TEXT NOT NULL,
  status           TEXT NOT NULL,           -- NOTIFIED / IN_REVIEW / APPROVED / REJECTED / PAID
  claimed_amount   REAL NOT NULL,
  indemnity_amount REAL,                    -- amount ExportShield pays; NULL until decided
  decided_on       TEXT
);

CREATE TABLE payments (                     -- indemnity payments to the exporter
  id             INTEGER PRIMARY KEY,
  claim_id       INTEGER NOT NULL REFERENCES claims(id),
  amount         REAL NOT NULL,
  paid_on        TEXT NOT NULL
);


INSERT INTO countries (code, name, risk_category) VALUES
  ('AT', 'Austria', 1),
  ('DE', 'Germany', 1),
  ('US', 'United States', 1),
  ('PL', 'Poland', 2),
  ('SK', 'Slovakia', 2),
  ('IN', 'India', 3),
  ('CN', 'China', 3),
  ('BR', 'Brazil', 5),
  ('TR', 'Turkey', 5),
  ('KZ', 'Kazakhstan', 5),
  ('EG', 'Egypt', 6),
  ('UA', 'Ukraine', 7);

INSERT INTO customers (id, name, ico, city, segment, onboarded_on) VALUES
  (1, 'Vltavska Precision Tools s.r.o.', '92576004', 'Plzen', 'SME', '2019-03-12'),
  (2, 'Moravia AgroTech a.s.', '98983214', 'Olomouc', 'CORPORATE', '2017-06-01'),
  (3, 'Krkonose Glassworks s.r.o.', '92821319', 'Liberec', 'SME', '2020-02-17'),
  (4, 'Bohemia Pump Systems a.s.', '97483560', 'Brno', 'CORPORATE', '2016-11-23'),
  (5, 'Sumava Timber s.r.o.', '94256899', 'Strakonice', 'SME', '2021-04-08'),
  (6, 'Ostrava Steel Components a.s.', '92939450', 'Ostrava', 'CORPORATE', '2015-09-30'),
  (7, 'Hana Food Export s.r.o.', '95572646', 'Prostejov', 'SME', '2022-01-19'),
  (8, 'Jizera Textiles s.r.o.', '99886718', 'Jablonec nad Nisou', 'MICRO', '2023-05-02'),
  (9, 'Polabi Chemicals a.s.', '4471203', 'Pardubice', 'CORPORATE', '2018-03-14'),
  (10, 'Beskydy Bikes s.r.o.', '93632447', 'Frydek-Mistek', 'SME', '2021-10-11'),
  (11, 'Labe Medical Devices s.r.o.', '91369595', 'Hradec Kralove', 'SME', '2022-07-25'),
  (12, 'Podyji Wine Group s.r.o.', '99742414', 'Znojmo', 'MICRO', '2024-02-05'),
  (13, 'Praha Rail Parts a.s.', '97093282', 'Praha', 'CORPORATE', '2016-04-18'),
  (14, 'Orlice Electronics s.r.o.', '93499500', 'Usti nad Orlici', 'SME', '2023-09-04'),
  (15, 'Krkonose Glassworks s r o', '92821319', 'Liberec', 'SME', '2025-03-03');

INSERT INTO buyers (id, name, country_code, sector) VALUES
  (1, 'Rheinwerk Handels GmbH', 'DE', 'Machinery'),
  (2, 'Nordhafen Logistik GmbH', 'DE', 'Transport'),
  (3, 'Bavaria Bau Supplies GmbH', 'DE', 'Construction'),
  (4, 'Alpenmarkt Vertrieb GmbH', 'AT', 'Retail'),
  (5, 'Donau Medtech GmbH', 'AT', 'Healthcare'),
  (6, 'Wisla Budowa Sp. z o.o.', 'PL', 'Construction'),
  (7, 'Krakowskie Hurt Sp. z o.o.', 'PL', 'Food'),
  (8, 'Tatra Distribucia s.r.o.', 'SK', 'Retail'),
  (9, 'Dunaj Agro s.r.o.', 'SK', 'Agriculture'),
  (10, 'Great Lakes Industrial Supply Inc.', 'US', 'Machinery'),
  (11, 'Lone Star Outdoor LLC', 'US', 'Retail'),
  (12, 'Bayview Health Partners Inc.', 'US', 'Healthcare'),
  (13, 'Deccan Engineering Pvt Ltd', 'IN', 'Machinery'),
  (14, 'Ganga Textiles Pvt Ltd', 'IN', 'Textiles'),
  (15, 'Pearl River Trading Co Ltd', 'CN', 'Chemicals'),
  (16, 'Yangtze Glass Import Co Ltd', 'CN', 'Glass'),
  (17, 'Parana Agro Comercial Ltda', 'BR', 'Agriculture'),
  (18, 'Rio Bikes Distribuidora Ltda', 'BR', 'Retail'),
  (19, 'Anatolia Makine A.S.', 'TR', 'Machinery'),
  (20, 'Bosphorus Gida Ltd', 'TR', 'Food'),
  (21, 'Steppe Rail Service LLP', 'KZ', 'Transport'),
  (22, 'Nile Pharma Distribution SAE', 'EG', 'Healthcare'),
  (23, 'Dnipro Agro Holding LLC', 'UA', 'Agriculture'),
  (24, 'Baltic Timber Traders', NULL, 'Construction'),
  (25, 'Marmara Insaat A.S.', 'TR', 'Construction');

INSERT INTO policies (id, customer_id, policy_no, start_date, end_date, status, premium_rate) VALUES
  (1, 1, 'ES-2025-1001', '2025-07-01', '2026-06-30', 'EXPIRED', 0.0041),
  (2, 2, 'ES-2024-1002', '2024-04-01', '2025-03-31', 'EXPIRED', 0.0041),
  (3, 2, 'ES-2025-1003', '2025-04-01', '2026-03-31', 'EXPIRED', 0.0052),
  (4, 3, 'ES-2025-1004', '2025-02-01', '2026-01-31', 'EXPIRED', 0.0052),
  (5, 4, 'ES-2024-1005', '2024-01-01', '2024-12-31', 'EXPIRED', 0.0032),
  (6, 4, 'ES-2025-1006', '2025-01-01', '2025-12-31', 'EXPIRED', 0.0052),
  (7, 5, 'ES-2025-1007', '2025-10-01', '2026-09-30', 'ACTIVE', 0.0035),
  (8, 6, 'ES-2024-1008', '2024-06-01', '2025-05-31', 'EXPIRED', 0.0052),
  (9, 6, 'ES-2025-1009', '2025-06-01', '2026-05-31', 'EXPIRED', 0.0045),
  (10, 7, 'ES-2025-1010', '2025-03-01', '2026-02-28', 'EXPIRED', 0.0052),
  (11, 8, 'ES-2026-1011', '2026-01-01', '2026-12-31', 'ACTIVE', 0.0052),
  (12, 9, 'ES-2024-1012', '2024-09-01', '2025-08-31', 'EXPIRED', 0.0052),
  (13, 9, 'ES-2025-1013', '2025-09-01', '2026-08-31', 'EXPIRED', 0.0041),
  (14, 10, 'ES-2025-1014', '2025-05-01', '2026-01-31', 'CANCELLED', 0.0028),
  (15, 11, 'ES-2025-1015', '2025-11-01', '2026-10-31', 'ACTIVE', 0.0028),
  (16, 12, 'ES-2026-1016', '2026-03-01', '2027-02-28', 'ACTIVE', 0.0045),
  (17, 13, 'ES-2024-1017', '2024-10-01', '2025-09-30', 'EXPIRED', 0.0052),
  (18, 13, 'ES-2025-1018', '2025-10-01', '2026-09-30', 'ACTIVE', 0.0035),
  (19, 14, 'ES-2025-1019', '2025-08-01', '2025-07-31', 'EXPIRED', 0.0041),
  (20, 15, 'ES-2026-1020', '2026-04-01', '2027-03-31', 'ACTIVE', 0.0045);

INSERT INTO credit_limits (id, policy_id, buyer_id, requested_amount, approved_amount, currency, status, requested_on, decided_on, underwriter) VALUES
  (1, 1, 1, 50000, 37000, 'EUR', 'REDUCED', '2025-07-31', '2025-08-04', 'J. Marek'),
  (2, 1, 10, 500000, 500000, 'USD', 'APPROVED', '2025-08-12', '2025-08-26', 'T. Bily'),
  (3, 2, 9, 80000, 60000, 'EUR', 'REDUCED', '2024-05-24', '2024-05-27', 'J. Marek'),
  (4, 2, 17, 500000, 200000, 'EUR', 'REDUCED', '2024-04-04', '2024-04-12', 'J. Marek'),
  (5, 3, 17, 200000, 200000, 'EUR', 'APPROVED', '2025-05-31', '2025-06-19', 'P. Novotna'),
  (6, 3, 23, 200000, 75000, 'EUR', 'REJECTED', '2025-05-07', '2025-05-14', 'E. Kralova'),
  (7, 4, 16, 300000, 300000, 'EUR', 'APPROVED', '2025-03-31', '2025-04-20', 'T. Bily'),
  (8, 4, 4, 50000, 50000, 'EUR', 'APPROVED', '2025-02-20', '2025-02-28', 'T. Bily'),
  (9, 5, 19, 200000, 100000, 'EUR', 'REDUCED', '2024-02-14', '2024-02-18', 'J. Marek'),
  (10, 5, 1, 200000, 200000, 'EUR', 'APPROVED', '2024-01-27', '2024-02-12', 'T. Bily'),
  (11, 6, 1, 400000, 400000, 'EUR', 'APPROVED', '2025-01-24', '2025-02-12', 'T. Bily'),
  (12, 6, 21, 80000, 0, 'EUR', 'REJECTED', '2025-01-20', '2025-01-31', 'J. Marek'),
  (13, 7, 3, 200000, 150000, 'EUR', 'REDUCED', '2025-11-28', '2025-12-01', 'E. Kralova'),
  (14, 7, 24, 200000, 200000, 'EUR', 'APPROVED', '2025-11-24', '2025-12-06', 'T. Bily'),
  (15, 8, 3, 50000, 50000, 'EUR', 'APPROVED', '2024-06-04', '2024-06-22', 'E. Kralova'),
  (16, 8, 25, 80000, 60000, 'EUR', 'REDUCED', '2024-07-16', '2024-08-05', 'P. Novotna'),
  (17, 9, 25, 200000, 80000, 'EUR', 'REDUCED', '2025-06-12', '2025-07-02', 'T. Bily'),
  (18, 9, 21, 250000, 100000, 'EUR', 'REDUCED', '2025-07-19', '2025-07-24', 'T. Bily'),
  (19, 10, 7, 400000, 400000, 'EUR', 'APPROVED', '2025-03-08', '2025-03-03', 'T. Bily'),
  (20, 10, 20, 500000, 200000, 'EUR', 'REDUCED', '2025-04-07', '2025-04-11', 'E. Kralova'),
  (21, 11, 14, 500000, 200000, 'EUR', 'REDUCED', '2026-01-20', '2026-02-04', 'P. Novotna'),
  (22, 11, 8, 100000, 100000, 'EUR', 'APPROVED', '2026-02-14', '2026-02-17', 'P. Novotna'),
  (23, 12, 15, 80000, 80000, 'EUR', 'APPROVED', '2024-10-26', '2024-10-29', 'J. Marek'),
  (24, 12, 5, 50000, 50000, 'EUR', 'APPROVED', '2024-09-25', '2024-10-15', 'E. Kralova'),
  (25, 13, 15, 150000, 150000, 'EUR', 'APPROVED', '2025-10-06', '2025-10-14', 'E. Kralova'),
  (26, 13, 5, 250000, 250000, 'EUR', 'APPROVED', '2025-10-07', '2025-10-22', 'T. Bily'),
  (27, 14, 18, 300000, 300000, 'EUR', 'APPROVED', '2025-05-19', '2025-06-09', 'J. Marek'),
  (28, 14, 11, 80000, 80000, 'USD', 'APPROVED', '2025-05-15', '2025-06-04', 'E. Kralova'),
  (29, 15, 12, 300000, 300000, 'USD', 'APPROVED', '2025-12-03', '2025-12-23', 'J. Marek'),
  (30, 15, 22, 80000, 32000, 'EUR', 'REDUCED', '2025-12-30', '2026-01-16', 'E. Kralova'),
  (31, 16, 7, 250000, 125000, 'EUR', 'REDUCED', '2026-04-03', '2026-04-17', 'P. Novotna'),
  (32, 16, 4, 150000, 150000, 'EUR', 'APPROVED', '2026-04-29', '2026-05-19', 'P. Novotna'),
  (33, 17, 21, 500000, 0, 'EUR', 'REJECTED', '2024-10-30', '2024-11-14', 'E. Kralova'),
  (34, 17, 2, 250000, 250000, 'EUR', 'APPROVED', '2024-11-05', '2024-11-19', 'J. Marek'),
  (35, 18, 21, 100000, 0, 'EUR', 'REJECTED', '2025-10-18', '2025-11-04', 'E. Kralova'),
  (36, 18, 2, 300000, 150000, 'EUR', 'REDUCED', '2025-11-11', '2025-11-24', 'E. Kralova'),
  (37, 19, 10, 100000, 100000, 'USD', 'APPROVED', '2025-08-12', '2025-08-25', 'P. Novotna'),
  (38, 19, 19, 200000, 80000, 'EUR', 'REDUCED', '2025-09-15', '2025-10-03', 'J. Marek'),
  (39, 20, 16, 300000, 300000, 'EUR', 'APPROVED', '2026-04-25', '2026-05-07', 'E. Kralova'),
  (40, 7, 6, 200000, NULL, 'EUR', 'REQUESTED', '2026-09-08', NULL, NULL),
  (41, 18, 2, 120000, NULL, 'EUR', 'REQUESTED', '2026-09-14', NULL, NULL),
  (42, 15, 5, 150000, NULL, 'EUR', 'REQUESTED', '2026-09-21', NULL, NULL),
  (43, 20, 4, 60000, NULL, 'EUR', 'REQUESTED', '2026-09-25', NULL, NULL);

INSERT INTO invoices (id, policy_id, buyer_id, invoice_no, amount, currency, issue_date, due_date, paid_date) VALUES
  (1, 1, 1, 'INV-2026-01001', 7200.0, 'EUR', '2026-03-08', '2026-04-07', NULL),
  (2, 1, 1, 'INV-2026-01002', 6500.0, 'EUR', '2026-03-01', '2026-04-30', '2026-05-20'),
  (3, 1, 1, 'INV-2026-01002', 11300.0, 'EUR', '2025-11-21', '2026-03-21', '2026-03-18'),
  (4, 1, 10, 'INV-2026-01004', 119100.0, 'USD', '2026-03-23', '2026-07-21', NULL),
  (5, 1, 10, 'INV-2026-01005', 152200.0, 'USD', '2026-02-05', '2026-06-05', '2026-06-27'),
  (6, 2, 9, 'INV-2025-02001', 18300.0, 'EUR', '2025-02-19', '2025-03-21', NULL),
  (7, 2, 9, 'INV-2025-02002', 16900.0, 'EUR', '2025-03-12', '2025-05-11', NULL),
  (8, 2, 17, 'INV-2024-02003', 24200.0, 'EUR', '2024-06-24', '2024-07-24', NULL),
  (9, 2, 17, 'INV-2025-02004', 86800.0, 'EUR', '2025-01-21', '2025-03-22', '2025-03-15'),
  (10, 3, 17, 'INV-2025-02005', 42400.0, 'EUR', '2025-08-19', '2025-09-18', NULL),
  (11, 3, 17, 'INV-2025-02006', 38400.0, 'EUR', '2025-11-24', '2026-02-22', '2026-02-26'),
  (12, 4, 16, 'INV-2025-03001', 133300.0, 'EUR', '2025-12-25', '2026-04-24', '2026-04-15'),
  (13, 4, 16, 'INV-2025-03002', 69500.0, 'EUR', '2025-10-02', '2025-12-01', '2025-12-04'),
  (14, 4, 4, 'INV-2025-03003', 10600.0, 'EUR', '2025-11-02', '2026-01-31', NULL),
  (15, 4, 4, 'INV-2026-03004', 18900.0, 'EUR', '2026-01-12', '2026-05-12', '2026-05-14'),
  (16, 4, 4, 'INV-2025-03005', 17300.0, 'EUR', '2025-03-05', '2025-07-03', NULL),
  (17, 5, 19, 'INV-2024-04001', 15200.0, 'EUR', '2024-04-22', '2024-08-20', NULL),
  (18, 5, 19, 'INV-2024-04002', 31900.0, 'EUR', '2024-05-16', '2024-09-13', '2024-10-07'),
  (19, 5, 1, 'INV-2024-04003', 72400.0, 'EUR', '2024-12-09', '2025-02-07', '2025-02-17'),
  (20, 5, 1, 'INV-2024-04004', 25700.0, 'EUR', '2024-11-09', '2025-01-08', NULL),
  (21, 6, 1, 'INV-2025-04005', 103500.0, 'EUR', '2025-12-15', '2026-03-15', '2026-04-08'),
  (22, 6, 1, 'INV-2025-04006', 140100.0, 'EUR', '2025-03-17', '2025-06-15', '2025-07-03'),
  (23, 7, 3, 'INV-2026-05001', 42900.0, 'EUR', '2026-01-27', '2026-05-27', '2026-06-02'),
  (24, 7, 3, 'INV-2026-05002', 29100.0, 'EUR', '2026-01-04', '2026-02-03', '2026-01-28'),
  (25, 7, 24, 'INV-2026-05003', 59500.0, 'EUR', '2026-03-01', '2026-03-31', '2026-04-19'),
  (26, 7, 24, 'INV-2026-05004', 79900.0, 'EUR', '2026-01-02', '2026-03-03', '2026-03-23'),
  (27, 8, 3, 'INV-2025-06001', 5800.0, 'EUR', '2025-04-20', '2025-05-20', '2025-06-10'),
  (28, 8, 3, 'INV-2025-06002', 18100.0, 'EUR', '2025-05-09', '2025-09-06', '2025-10-01'),
  (29, 8, 25, 'INV-2024-06003', 21300.0, 'EUR', '2024-08-22', '2024-11-20', NULL),
  (30, 8, 25, 'INV-2025-06004', 7900.0, 'EUR', '2025-03-28', '2025-07-26', '2025-08-17'),
  (31, 9, 25, 'INV-2026-06005', 13600.0, 'EUR', '2026-05-22', '2026-05-07', NULL),
  (32, 9, 25, 'INV-2025-06006', 15800.0, 'EUR', '2025-12-14', '2026-03-14', '2026-03-21'),
  (33, 9, 21, 'INV-2025-06007', 32900.0, 'EUR', '2025-08-25', '2025-09-24', '2025-09-15'),
  (34, 9, 21, 'INV-2025-06008', 11700.0, 'EUR', '2025-10-12', '2025-12-11', NULL),
  (35, 10, 7, 'INV-2025-07001', 118800.0, 'EUR', '2025-11-19', '2026-03-19', '2026-03-14'),
  (36, 10, 7, 'INV-2025-07002', 157900.0, 'EUR', '2025-09-30', '2025-12-29', '2026-01-02'),
  (37, 10, 20, 'INV-2025-07003', 33500.0, 'EUR', '2025-06-19', '2025-10-17', '2025-11-03'),
  (38, 10, 20, 'INV-2025-07004', 33100.0, 'EUR', '2025-12-22', '2026-01-21', '2026-01-15'),
  (39, 11, 14, 'INV-2026-08001', 21000.0, 'EUR', '2026-08-15', '2026-09-14', NULL),
  (40, 11, 14, 'INV-2026-08002', 27100.0, 'EUR', '2026-04-26', '2026-06-25', NULL),
  (41, 11, 14, 'INV-2026-08003', 43200.0, 'EUR', '2026-03-12', '2026-04-11', '2026-04-17'),
  (42, 11, 8, 'INV-2026-08004', 28700.0, 'EUR', '2026-07-27', '2026-11-24', NULL),
  (43, 11, 8, 'INV-2026-08005', 42900.0, 'EUR', '2026-06-08', '2026-08-07', NULL),
  (44, 11, 8, 'INV-2026-08006', 36400.0, 'EUR', '2026-07-17', '2026-10-15', NULL),
  (45, 12, 15, 'INV-2025-09001', 27500.0, 'EUR', '2025-07-30', '2025-08-29', '2025-09-14'),
  (46, 12, 15, 'INV-2025-09002', 20900.0, 'EUR', '2025-07-17', '2025-11-14', NULL),
  (47, 12, 5, 'INV-2025-09003', 12200.0, 'EUR', '2025-05-30', '2025-09-27', NULL),
  (48, 12, 5, 'INV-2025-09004', 15100.0, 'EUR', '2025-02-07', '2025-05-08', '2025-05-02'),
  (49, 12, 5, 'INV-2025-09005', 17800.0, 'EUR', '2025-02-07', '2025-04-08', '2025-04-11'),
  (50, 13, 15, 'INV-2026-09006', 49900.0, 'EUR', '2026-01-12', '2026-04-12', '2026-05-05'),
  (51, 13, 15, 'INV-2026-09007', 55500.0, 'EUR', '2026-01-05', '2026-03-06', '2026-03-16'),
  (52, 13, 5, 'INV-2026-09008', 106000.0, 'EUR', '2026-05-27', '2026-09-24', NULL),
  (53, 13, 5, 'INV-2026-09009', 53500.0, 'EUR', '2026-08-25', '2026-11-23', NULL),
  (54, 14, 18, 'INV-2025-10001', 106400.0, 'EUR', '2025-08-14', '2025-10-13', '2025-10-06'),
  (55, 14, 18, 'INV-2025-10002', 108400.0, 'EUR', '2025-11-24', '2026-01-23', '2026-01-19'),
  (56, 14, 18, 'INV-2025-10003', 53800.0, 'EUR', '2025-09-07', '2026-01-05', '2026-01-04'),
  (57, 14, 11, 'INV-2025-10004', 8800.0, 'USD', '2025-10-01', '2025-11-30', '2025-12-08'),
  (58, 14, 11, 'INV-2026-10005', 12100.0, 'USD', '2026-01-09', '2026-03-10', '2026-03-25'),
  (59, 14, 11, 'INV-2025-10006', 6700.0, 'USD', '2025-09-09', '2025-11-08', NULL),
  (60, 15, 12, 'INV-2026-11001', 29700.0, 'USD', '2026-09-05', '2026-11-04', NULL),
  (61, 15, 12, 'INV-2026-11002', 70000.0, 'USD', '2026-04-18', '2026-06-17', '2026-06-26'),
  (62, 15, 22, 'INV-2026-11003', 12600.0, 'EUR', '2026-05-24', '2026-07-23', '2026-08-06'),
  (63, 15, 22, 'INV-2026-11004', 3300.0, 'EUR', '2026-03-30', '2026-07-28', '2026-08-10'),
  (64, 16, 7, 'INV-2026-12001', 15300.0, 'EUR', '2026-07-17', '2026-10-15', NULL),
  (65, 16, 7, 'INV-2026-12002', 27900.0, 'EUR', '2026-09-17', '2026-11-16', NULL),
  (66, 16, 4, 'INV-2026-12003', 28600.0, 'EUR', '2026-08-21', '2026-11-19', NULL),
  (67, 16, 4, 'INV-2026-12004', 57700.0, 'EUR', '2026-07-07', '2026-11-04', NULL),
  (68, 17, 2, 'INV-2025-13001', 30800.0, 'EUR', '2025-05-09', '2025-06-08', '2025-06-10'),
  (69, 17, 2, 'INV-2025-13002', 42300.0, 'EUR', '2025-07-12', '2025-09-10', '2025-10-01'),
  (70, 18, 2, 'INV-2026-13003', 62800.0, 'EUR', '2026-01-23', '2026-03-24', '2026-04-08'),
  (71, 18, 2, 'INV-2026-13004', 34700.0, 'EUR', '2026-04-25', '2026-07-24', '2026-07-21'),
  (72, 19, 10, 'INV-2026-14001', 10500.0, 'USD', '2026-01-16', '2026-05-16', '2026-06-10'),
  (73, 19, 10, 'INV-2026-14002', 34200.0, 'USD', '2026-01-19', '2026-03-20', NULL),
  (74, 19, 19, 'INV-2026-14003', 17700.0, 'EUR', '2026-02-08', '2026-04-09', NULL),
  (75, 19, 19, 'INV-2026-14004', 29900.0, 'EUR', '2026-02-13', '2026-04-14', NULL),
  (76, 19, 19, 'INV-2025-14005', 13500.0, 'EUR', '2025-10-12', '2025-12-11', '2025-12-05'),
  (77, 20, 16, 'INV-2026-15001', 123600.0, 'EUR', '2026-05-18', '2026-08-16', '2026-08-18'),
  (78, 20, 16, 'INV-2026-15002', 61200.0, 'EUR', '2026-06-12', '2026-08-11', '2026-08-27');

INSERT INTO claims (id, invoice_id, notified_on, status, claimed_amount, indemnity_amount, decided_on) VALUES
  (1, 8, '2024-08-30', 'PAID', 24200.0, 21780.0, '2024-10-01'),
  (2, 17, '2024-11-02', 'PAID', 15200.0, 13680.0, '2024-11-25'),
  (3, 29, '2024-12-27', 'PAID', 21300.0, 19170.0, '2025-02-05'),
  (4, 20, '2025-03-23', 'PAID', 25700.0, 23130.0, '2025-05-06'),
  (5, 6, '2025-05-18', 'PAID', 18300.0, 16470.0, '2025-06-28'),
  (6, 7, '2025-06-21', 'PAID', 16900.0, 15210.0, '2025-08-05'),
  (7, 16, '2025-08-17', 'PAID', 17300.0, 15570.0, '2025-09-29'),
  (8, 10, '2025-11-21', 'APPROVED', 42400.0, 46640.0, '2026-01-03'),
  (9, 47, '2025-12-05', 'APPROVED', 12200.0, 10980.0, '2026-01-08'),
  (10, 59, '2025-12-28', 'REJECTED', 6700.0, 0.0, '2026-01-28'),
  (11, 46, '2026-01-18', 'IN_REVIEW', 20900.0, NULL, NULL),
  (12, 34, '2026-02-15', 'IN_REVIEW', 11700.0, NULL, NULL),
  (13, 14, '2026-04-08', 'NOTIFIED', 10600.0, NULL, NULL),
  (14, 73, '2026-04-25', 'NOTIFIED', 34200.0, NULL, NULL),
  (15, 9, '2025-04-24', 'IN_REVIEW', 86800.0, NULL, NULL);

INSERT INTO payments (id, claim_id, amount, paid_on) VALUES
  (1, 1, 21780.0, '2024-10-14'),
  (2, 2, 13680.0, '2024-12-06'),
  (3, 3, 19170.0, '2025-02-13'),
  (4, 4, 23130.0, '2025-05-16'),
  (5, 5, 9882.0, '2025-07-13'),
  (6, 5, 6588.0, '2025-08-12'),
  (7, 6, 9126.0, '2025-08-14'),
  (8, 6, 6084.0, '2025-09-13');
