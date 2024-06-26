DELETE FROM user_service_assoc;
DELETE FROM tasks;
DELETE FROM reviews;
DELETE FROM users;
DELETE FROM services;
DELETE FROM towns;


-- Insert sample data into users table with simulated email addresses
INSERT INTO users (id, first_name, last_name, email, password)
VALUES
    (gen_random_uuid(), 'John', 'Doe', 'jd123@gmail.com', crypt('pwd1', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Jane', 'Smith', 'jane006@gmail.com', crypt('pwd1', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Luis', 'Santiago', 'bestbeast@gmail.com', crypt('pwd3', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Hector', 'Torres', 'hector.torres@gmail.com', crypt('pwd4', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Angelica', 'Diaz', 'angelicadiaz09@gmail.com', crypt('pwd5', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Erick', 'Santiago', 'ericksan_san@gmail.com', crypt('pwd6', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Maria', 'Garcia', 'maria1990@gmail.com', crypt('pwd7', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Carlos', 'Martinez', 'carlos.martinez@gmail.com', crypt('pwd8', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Sofia', 'Rodriguez', 'sofia.rodri@gmail.com', crypt('pwd9', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Daniel', 'Lopez', 'daniellopezPR@gmail.com', crypt('pwd10', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Laura', 'Hernandez', 'lauritaPR@gmail.com', crypt('pwd11', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Pedro', 'Gonzalez', 'pedro.gonzalez@gmail.com', crypt('pwd12', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Ana', 'Perez', 'ana.perez@gmail.com', crypt('pwd13', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Javier', 'Sanchez', 'javier.sanchez@gmail.com', crypt('pwd14', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Marta', 'Lopez', 'marta.lopez@gmail.com', crypt('pwd15', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Gabriel', 'Rivera', 'gabriel.rivera@gmail.com', crypt('pwd16', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Veronica', 'Gomez', 'veronica.gomez@gmail.com', crypt('pwd17', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Miguel', 'Diaz', 'miguel.diaz@gmail.com', crypt('pwd18', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Julia', 'Fernandez', 'julia.fernandez@gmail.com', crypt('pwd19', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Roberto', 'Ramirez', 'roberto.ramirez@gmail.com', crypt('pwd20', gen_salt('bf', 12))),

    -- Outlook email addresses
    (gen_random_uuid(), 'Alice', 'Brown', 'alice.brown@outlook.com', crypt('pwd21', gen_salt('bf', 12))),
    (gen_random_uuid(), 'David', 'Wilson', 'david.wilson@outlook.com', crypt('pwd22', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Emma', 'Jones', 'emma.jones@outlook.com', crypt('pwd23', gen_salt('bf', 12))),
    (gen_random_uuid(), 'James', 'Taylor', 'james.taylor@outlook.com', crypt('pwd24', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Olivia', 'Davis', 'olivia787@outlook.com', crypt('pwd25', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Michael', 'Evans', 'michael_office@outlook.com', crypt('pwd26', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Sophia', 'Clark', 'sophia.clark@outlook.com', crypt('pwd27', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Alexander', 'Thomas', 'alexander.thomas@outlook.com', crypt('pwd28', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Ava', 'White', 'ava.white@outlook.com', crypt('pwd29', gen_salt('bf', 12))),
    (gen_random_uuid(), 'Matthew', 'Walker', 'matthew.walker@outlook.com', crypt('pwd30', gen_salt('bf', 12)));

-- Insert sample data into services table
INSERT INTO services (id, name)
VALUES
    (gen_random_uuid(), 'Nails'),
    (gen_random_uuid(), 'Gardening'),
    (gen_random_uuid(), 'Barber'),
    (gen_random_uuid(), 'Hairstyling'),
    (gen_random_uuid(), 'Pet Sitting'),
    (gen_random_uuid(), 'Car Washing'),
    (gen_random_uuid(), 'Baking'),
    (gen_random_uuid(), 'Plumbing'),
    (gen_random_uuid(), 'Electrical Service'),
    (gen_random_uuid(), 'House Cleaning'),
    (gen_random_uuid(), 'Pet Grooming'),
    (gen_random_uuid(), 'Landscaping'),
    (gen_random_uuid(), 'Event Decorator'),
    (gen_random_uuid(), 'DJ'),
    (gen_random_uuid(), 'Catering'),
    (gen_random_uuid(), 'Auto Body Painting'),
    (gen_random_uuid(), 'Painter');

-- Insert sample data into towns table
INSERT INTO towns (id, name)
VALUES
    (gen_random_uuid(), 'Adjuntas'),
    (gen_random_uuid(), 'Aguada'),
    (gen_random_uuid(), 'Aguadilla'),
    (gen_random_uuid(), 'Aguas Buenas'),
    (gen_random_uuid(), 'Aibonito'),
    (gen_random_uuid(), 'Añasco'),
    (gen_random_uuid(), 'Arecibo'),
    (gen_random_uuid(), 'Arroyo'),
    (gen_random_uuid(), 'Barceloneta'),
    (gen_random_uuid(), 'Barranquitas'),
    (gen_random_uuid(), 'Bayamon'),
    (gen_random_uuid(), 'Cabo Rojo'),
    (gen_random_uuid(), 'Caguas'),
    (gen_random_uuid(), 'Camuy'),
    (gen_random_uuid(), 'Canovanas'),
    (gen_random_uuid(), 'Carolina'),
    (gen_random_uuid(), 'Cataño'),
    (gen_random_uuid(), 'Cayey'),
    (gen_random_uuid(), 'Ceiba'),
    (gen_random_uuid(), 'Ciales'),
    (gen_random_uuid(), 'Cidra'),
    (gen_random_uuid(), 'Coamo'),
    (gen_random_uuid(), 'Comerio'),
    (gen_random_uuid(), 'Corozal'),
    (gen_random_uuid(), 'Culebra'),
    (gen_random_uuid(), 'Dorado'),
    (gen_random_uuid(), 'Fajardo'),
    (gen_random_uuid(), 'Florida'),
    (gen_random_uuid(), 'Guanica'),
    (gen_random_uuid(), 'Guayama'),
    (gen_random_uuid(), 'Guayanilla'),
    (gen_random_uuid(), 'Guaynabo'),
    (gen_random_uuid(), 'Gurabo'),
    (gen_random_uuid(), 'Hatillo'),
    (gen_random_uuid(), 'Hormigueros'),
    (gen_random_uuid(), 'Humacao'),
    (gen_random_uuid(), 'Isabela'),
    (gen_random_uuid(), 'Jayuya'),
    (gen_random_uuid(), 'Juana Diaz'),
    (gen_random_uuid(), 'Juncos'),
    (gen_random_uuid(), 'Lajas'),
    (gen_random_uuid(), 'Lares'),
    (gen_random_uuid(), 'Las Marias'),
    (gen_random_uuid(), 'Las Piedras'),
    (gen_random_uuid(), 'Loiza'),
    (gen_random_uuid(), 'Luquillo'),
    (gen_random_uuid(), 'Manati'),
    (gen_random_uuid(), 'Maricao'),
    (gen_random_uuid(), 'Maunabo'),
    (gen_random_uuid(), 'Mayagüez'),
    (gen_random_uuid(), 'Moca'),
    (gen_random_uuid(), 'Morovis'),
    (gen_random_uuid(), 'Naguabo'),
    (gen_random_uuid(), 'Naranjito'),
    (gen_random_uuid(), 'Orocovis'),
    (gen_random_uuid(), 'Patillas'),
    (gen_random_uuid(), 'Peñuelas'),
    (gen_random_uuid(), 'Ponce'),
    (gen_random_uuid(), 'Quebradillas'),
    (gen_random_uuid(), 'Rincon'),
    (gen_random_uuid(), 'Rio Grande'),
    (gen_random_uuid(), 'Sabana Grande'),
    (gen_random_uuid(), 'Salinas'),
    (gen_random_uuid(), 'San German'),
    (gen_random_uuid(), 'San Juan'),
    (gen_random_uuid(), 'San Lorenzo'),
    (gen_random_uuid(), 'San Sebastian'),
    (gen_random_uuid(), 'Santa Isabel'),
    (gen_random_uuid(), 'Toa Alta'),
    (gen_random_uuid(), 'Toa Baja'),
    (gen_random_uuid(), 'Trujillo Alto'),
    (gen_random_uuid(), 'Utuado'),
    (gen_random_uuid(), 'Vega Alta'),
    (gen_random_uuid(), 'Vega Baja'),
    (gen_random_uuid(), 'Vieques'),
    (gen_random_uuid(), 'Villalba'),
    (gen_random_uuid(), 'Yabucoa'),
    (gen_random_uuid(), 'Yauco');


-- Assigning services to the remaining users randomly with multiple towns

INSERT INTO user_service_assoc (user_id, service_id, town_id)
SELECT u.id, s.id, t.id
FROM users u
JOIN services s ON s.name = 'Auto Body Painting'
JOIN towns t ON t.name IN ('Aguadilla', 'Arecibo')
WHERE u.first_name = 'John' AND u.last_name = 'Doe';

INSERT INTO user_service_assoc (user_id, service_id, town_id)
SELECT u.id, s.id, t.id
FROM users u
JOIN services s ON s.name = 'DJ'
JOIN towns t ON t.name IN ('San Sebastian', 'Loiza')
WHERE u.first_name = 'Jane' AND u.last_name = 'Smith';

INSERT INTO user_service_assoc (user_id, service_id, town_id)
SELECT u.id, s.id, t.id
FROM users u
JOIN services s ON s.name = 'Pet Sitter'
JOIN towns t ON t.name IN ('Caguas', 'Fajardo')
WHERE u.first_name = 'Luis' AND u.last_name = 'Santiago';

INSERT INTO user_service_assoc (user_id, service_id, town_id)
SELECT u.id, s.id, t.id
FROM users u
JOIN services s ON s.name = 'Catering'
JOIN towns t ON t.name IN ('Ponce', 'Carolina')
WHERE u.first_name = 'Hector' AND u.last_name = 'Torres';

INSERT INTO user_service_assoc (user_id, service_id, town_id)
SELECT u.id, s.id, t.id
FROM users u
JOIN services s ON s.name = 'Event Decorator'
JOIN towns t ON t.name IN ('Arecibo', 'Guayama')
WHERE u.first_name = 'Angelica' AND u.last_name = 'Diaz';

INSERT INTO user_service_assoc (user_id, service_id, town_id)
SELECT u.id, s.id, t.id
FROM users u
JOIN services s ON s.name = 'House Cleaning'
JOIN towns t ON t.name IN ('Toa Alta', 'Bayamon')
WHERE u.first_name = 'Erick' AND u.last_name = 'Santiago';

INSERT INTO user_service_assoc (user_id, service_id, town_id)
SELECT u.id, s.id, t.id
FROM users u
JOIN services s ON s.name = 'Landscaping'
JOIN towns t ON t.name IN ('Luquillo', 'Culebra')
WHERE u.first_name = 'Carlos' AND u.last_name = 'Martinez';

INSERT INTO user_service_assoc (user_id, service_id, town_id)
SELECT u.id, s.id, t.id
FROM users u
JOIN services s ON s.name = 'Plumbing'
JOIN towns t ON t.name IN ('Guaynabo', 'Rincon')
WHERE u.first_name = 'Sofia' AND u.last_name = 'Rodriguez';

INSERT INTO user_service_assoc (user_id, service_id, town_id)
SELECT u.id, s.id, t.id
FROM users u
JOIN services s ON s.name = 'Electrical Service'
JOIN towns t ON t.name IN ('Bayamon', 'Isabela')
WHERE u.first_name = 'Daniel' AND u.last_name = 'Lopez';

INSERT INTO user_service_assoc (user_id, service_id, town_id)
SELECT u.id, s.id, t.id
FROM users u
JOIN services s ON s.name = 'Pet Grooming'
JOIN towns t ON t.name IN ('Carolina', 'Manati')
WHERE u.first_name = 'Pedro' AND u.last_name = 'Gonzalez';

INSERT INTO user_service_assoc (user_id, service_id, town_id)
SELECT u.id, s.id, t.id
FROM users u
JOIN services s ON s.name = 'Baking'
JOIN towns t ON t.name IN ('Humacao', 'Ceiba')
WHERE u.first_name = 'Ana' AND u.last_name = 'Perez';

INSERT INTO user_service_assoc (user_id, service_id, town_id)
SELECT u.id, s.id, t.id
FROM users u
JOIN services s ON s.name = 'Hairstyling'
JOIN towns t ON t.name IN ('Aguada', 'Jayuya')
WHERE u.first_name = 'Marta' AND u.last_name = 'Lopez';

INSERT INTO user_service_assoc (user_id, service_id, town_id)
SELECT u.id, s.id, t.id
FROM users u
JOIN services s ON s.name = 'Car Washing'
JOIN towns t ON t.name IN ('Rincon', 'Mayaguez')
WHERE u.first_name = 'Gabriel' AND u.last_name = 'Rivera';

-- End of assingments


-- Output confirmation
SELECT 'Tables created and populated successfully' AS Status;