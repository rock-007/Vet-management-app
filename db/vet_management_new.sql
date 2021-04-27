DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    telephone_number TEXT
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    contact_number text,
    date_of_birth DATE
);


CREATE TABLE Appointments (
    id SERIAL PRIMARY KEY,
    date DATE,
    time TIME,
    vet_id SERIAL REFERENCES vets(id),
    pets_id SERIAL REFERENCES pets(id)
);
