-- SQLite
-- DROP TABLE owners;

-- CREATE TABLE owners(
--   id INTEGER PRIMARY KEY,
--   name TEXT,
--   address TEXT,
--   email TEXT,
--   phone INTEGER
-- );

-- CREATE TABLE pets(
--   id INTEGER PRIMARY KEY,
--   name TEXT,
--   breed TEXT,
--   last_fed at DATETIME,
--   owner_id INTEGER,
--   FOREIGN KEY (owner_id) REFERENCES owners(id)
-- );

-- SQLite
-- INSERT INTO owners (
-- name, address, email, phone)
-- VALUES ("Jacob", "456 St", "jacob@example.com", 6666666666);

-- INSERT INTO owners (
-- name, address, email, phone)
-- VALUES ("Jane", "789 St", "jane@example.com", 7666666666);

-- -- SQLite
-- INSERT INTO pets (name, breed, owner_id)
-- VALUES ("Martin", "Poodle", 1);

-- INSERT INTO pets (name, breed, owner_id)
-- VALUES ("Luna", "Chihuahua", 1);

-- INSERT INTO pets (name, breed, owner_id)
-- VALUES ("Maggie", "Australian Shepherd", 3);

-- INSERT INTO pets (name, breed, owner_id)
-- VALUES ("Martin 2", "Poodle", 1);

-- SELECT * FROM pets
-- WHERE owner_id = 1
-- And breed = "Poodle";

-- SELECT * FROM pets
-- WHERE name LIKE "%artin 2%";


-- DELETE FROM pets
-- WHERE name LIKE "%artin 2%";

-- SELECT pets.id, pets.name, pets.breed, owners.name as "owner", owners.phone as "owner phone"
-- FROM pets
-- JOIN owners ON pets.owner_id = owners.id;

-- CREATE TABLE handlers(
--   id INTEGER PRIMARY KEY,
--   name TEXT
-- );

-- CREATE TABLE appointments(
--   id INTEGER PRIMARY KEY,
--   time DATETIME,
--   purpose TEXT,
--   pet_id INTEGER,
--   handler_id INTEGER,
--   FOREIGN KEY(handler_id) REFERENCES handlers(id),
--   FOREIGN KEY(pet_id) REFERENCES pets(id)
-- );

-- INSERT INTO handlers(name)
-- VALUES ('Sam');

-- INSERT INTO handlers(name)
-- VALUES ('Ali');

-- INSERT INTO appointments (
-- time,
-- purpose,
-- pet_id,
-- handler_id
-- )
-- VALUES (
-- '2023-09-19 12:00:00',
-- 'walk',
-- 1,
-- 1
-- );

-- INSERT INTO appointments (
-- time,
-- purpose,
-- pet_id,
-- handler_id
-- )
-- VALUES (
-- '2023-09-19 13:00:00',
-- 'walk',
-- 1,
-- 2
-- );

-- INSERT INTO appointments (
-- time,
-- purpose,
-- pet_id,
-- handler_id
-- )
-- VALUES (
-- '2023-09-19 12:00:00',
-- 'feed',
-- 2,
-- 2
-- );

-- INSERT INTO appointments (
-- time,
-- purpose,
-- pet_id,
-- handler_id
-- )
-- VALUES (
-- '2023-09-20 12:00:00',
-- 'walk',
-- 2,
-- 1
-- );

-- INSERT INTO appointments (
-- time,
-- purpose,
-- pet_id,
-- handler_id
-- )
-- VALUES (
-- '2023-09-20 13:00:00',
-- 'walk',
-- 3,
-- 2
-- );

-- INSERT INTO appointments(
-- time,
-- purpose,
-- pet_id,
-- handler_id
-- )
-- VALUES (
-- "2023-09-19 11:00:00",
-- "feed",
-- 2,
-- 1);

-- UPDATE appointments
-- SET pet_id = 3, handler_id = 2
-- WHERE id = 5;

-- SELECT
-- appointments.id,
-- pets.name as "pet",
-- handlers.name as "handler",
-- appointments.purpose,
-- appointments.time
-- FROM appointments
-- JOIN pets
-- ON appointments.pet_id = pets.id
-- JOIN handlers
-- ON appointments.handler_id = handlers.id;

SELECT DISTINCT
handlers.name, pets.name, appointments.purpose
FROM appointments
JOIN pets
ON appointments.pet_id = pets.id
JOIN handlers
ON appointments.handler_id = handlers.id
