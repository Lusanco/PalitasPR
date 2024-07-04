-- Drop tables if they exist (for testing purposes)
DROP TABLE IF EXISTS user_service_assoc;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS initial_contacts;
DROP TABLE IF EXISTS request_towns;
DROP TABLE If EXISTS promo_towns;
DROP Table IF EXISTS promotions;
DROP Table IF EXISTS requests;
DROP TABLE IF EXISTS profiles;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS towns;
-- Drop trigger and function if they exist (to avoid conflicts)
DROP TRIGGER IF EXISTS tsvectorupdate ON services;
DROP FUNCTION IF EXISTS update_tsvector();
-- Create Extension for encryption
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Create table for User
CREATE TABLE users (
    id VARCHAR(50) PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR(50),
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(50),
    verified BOOLEAN DEFAULT false,
    verification_token VARCHAR(128) UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);
--  ------------------------------------------------------------------------------
-- Create table for Service
CREATE TABLE services (
    id Serial PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tsv tsvector
);

-- Create GIN index on the tsvector column
CREATE INDEX idx_services_tsv ON services USING gin(tsv);

-- Create trigger function to update tsvector column
CREATE FUNCTION update_tsvector() RETURNS trigger AS $$
BEGIN
    NEW.tsv := to_tsvector('english', NEW.name);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create trigger to call the trigger function on insert or update
CREATE TRIGGER tsvectorupdate BEFORE INSERT OR UPDATE
ON services FOR EACH ROW EXECUTE FUNCTION update_tsvector();

-- Update existing rows to populate tsvector column
UPDATE services SET tsv = to_tsvector('english', name);
-- -----------------------------------------------------------------

-- Create table for promotions of users offering services
-- If price max is left null, the price total is the price_min
CREATE TABLE promotions (
    id VARCHAR(50) PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR(50),
    user_id VARCHAR(50) REFERENCES users(id) NOT NULL,
    service_id INT REFERENCES services(id) NOT NULL,
    title VARCHAR(100) not NULL,
    description Text NOT NULL,
    price_min INT DEFAULT 0,
    price_max INT DEFAULT 0,
    pictures varchar(255),
    created_at TIMESTAMP  WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );

-- Create table for public requests of services
CREATE TABLE requests (
    id VARCHAR(50) PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR(50),
    user_id varchar REFERENCES users(id) NOT NULL,
    service_id INT REFERENCES services(id) NOT NULL,
    title VARCHAR(100) not NULL,
    description Text NOT NULL,
    pictures varchar(255),
    created_at TIMESTAMP  WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );

-- Create table for Initial Contacts
CREATE Table initial_contacts (
        id VARCHAR(50) PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR(50),
        sender_id varchar(50) REFERENCES users(id) NOT NULL,
        receiver_id varchar(50) REFERENCES users(id) NOT NULL,
        promo_id varchar(50) References promotions(id) ON DELETE CASCADE,
        request_id varchar(50) References requests(id) ON DELETE CASCADE,
        receiver_read BOOLEAN DEFAULT False,
        receiver_hide BOOLEAN DEFAULT False,
        sender_read BOOLEAN DEFAULT False,
        sender_hide BOOLEAN DEFAULT False,
        sent_task BOOLEAN DEFAULT False,
        created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create table for tasks
CREATE TABLE tasks (
    id VARCHAR(50) PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR(50),
	promo_id varchar(50) References promotions(id) ON DELETE CASCADE,
    request_id varchar(50) References requests(id) ON DELETE CASCADE,
    provider_id varchar(50) REFERENCES users(id) ON DELETE CASCADE NOT NULL,
    receiver_id varchar(50) REFERENCES users(id) ON DELETE CASCADE NOT NULL,
    initial_contact_id varchar(50) REFERENCES initial_contacts(id) ON DELETE CASCADE NOT NULL,
    receiver_confirm BOOLEAN,
    service_id INT REFERENCES services(id) ON DELETE CASCADE NOT NULL,
    description Text NOT NULL,
    status VARCHAR(10) DEFAULT 'pending' CHECK(status in ('active', 'closed', 'pending', 'reviewed')),
    price INT DEFAULT 120,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

--  Create Table for reviews
CREATE TABLE reviews (
    id VARCHAR(50) PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR(50),
    description Text NOT NULL,
    user_id varchar(50) REFERENCES users(id),
    task_id VARCHAR(50) REFERENCES tasks(id) ON DELETE CASCADE,
    rating NUMERIC(2, 1) CHECK (rating >= 1 AND rating <= 5),
    pictures varchar(255),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);
-- Create table for towns
CREATE TABLE towns (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- Create table for promo/towns assoc
CREATE TABLE promo_towns (
    id VARCHAR(50) PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR(50),
    promo_id  varchar(50) REFERENCES promotions(id) ON DELETE CASCADE NOT NULL,
    town_id  INT REFERENCES towns(id) ON DELETE CASCADE NOT NULL,
    created_at TIMESTAMP  WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create table for request/towns assoc
CREATE TABLE request_towns (
    id VARCHAR(50) PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR(50),
    request_id  varchar(50) REFERENCES requests(id) ON DELETE CASCADE NOT NULL,
    town_id  INT REFERENCES towns(id) ON DELETE CASCADE NOT NULL,
    created_at TIMESTAMP  WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create table for Profiles
CREATE TABLE profiles (
    id VARCHAR(50) PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR(50),
    bio TEXT,
    cover_pic varchar(255),
    job_title varchar(100),
    user_id varchar REFERENCES users(id) NOT NULL,
    profile_pic VARCHAR(255),
    gallery VARCHAR(255),
    social_links TEXT,
    qr_pic VARCHAR(255),
    tasks_completed INT,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data into users table with simulated email addresses
INSERT INTO users (id, first_name, last_name, email, password, verified, phone)
VALUES
    (gen_random_uuid(), 'John', 'Doe', 'jd123@gmail.com', crypt('pwd1', gen_salt('bf', 12)), true, '787-555-9999'),
    (gen_random_uuid(), 'Jane', 'Smith', 'jane006@gmail.com', crypt('pwd1', gen_salt('bf', 12)), true, '787-191-0000'),
    (gen_random_uuid(), 'Luis', 'Santiago', 'bestbeast@gmail.com', crypt('pwd3', gen_salt('bf', 12)), true, '787-000-6032'),
    (gen_random_uuid(), 'Hector', 'Torres', 'hector.torres@gmail.com', crypt('pwd4', gen_salt('bf', 12)), true, '787-435-1111'),
    (gen_random_uuid(), 'Angelica', 'Diaz', 'angelicadiaz09@gmail.com', crypt('pwd5', gen_salt('bf', 12)), true, '787-404-6000'),
    (gen_random_uuid(), 'Erick', 'Santiago', 'ericksan_san@gmail.com', crypt('pwd6', gen_salt('bf', 12)), true, '787-123-1012'),
    (gen_random_uuid(), 'Maria', 'Garcia', 'maria1990@gmail.com', crypt('pwd7', gen_salt('bf', 12)), true, '787-590-4040'),
    (gen_random_uuid(), 'Carlos', 'Martinez', 'carlos.martinez@gmail.com', crypt('pwd8', gen_salt('bf', 12)), true, '787-566-9239'),
    (gen_random_uuid(), 'Sofia', 'Rodriguez', 'sofia.rodri@gmail.com', crypt('pwd9', gen_salt('bf', 12)), true, '787-004-0234'),
    (gen_random_uuid(), 'Daniel', 'Lopez', 'daniellopezPR@gmail.com', crypt('pwd10', gen_salt('bf', 12)), true, '787-005-0134'),
    (gen_random_uuid(), 'Laura', 'Hernandez', 'lauritaPR@gmail.com', crypt('pwd11', gen_salt('bf', 12)), true, '787-005-0231'),
    (gen_random_uuid(), 'Pedro', 'Gonzalez', 'pedro.gonzalez@gmail.com', crypt('pwd12', gen_salt('bf', 12)), true, '787-008-0334'),
    (gen_random_uuid(), 'Ana', 'Perez', 'ana.perez@gmail.com', crypt('pwd13', gen_salt('bf', 12)), true, '787-011-0224'),
    (gen_random_uuid(), 'Javier', 'Sanchez', 'javier.sanchez@gmail.com', crypt('pwd14', gen_salt('bf', 12)), true, '787-054-0334'),
    (gen_random_uuid(), 'Marta', 'Lopez', 'marta.lopez@gmail.com', crypt('pwd15', gen_salt('bf', 12)), true, '787-007-0234'),
    (gen_random_uuid(), 'Gabriel', 'Rivera', 'gabriel.rivera@gmail.com', crypt('pwd16', gen_salt('bf', 12)), true, '787-084-0278'),
    (gen_random_uuid(), 'Veronica', 'Gomez', 'veronica.gomez@gmail.com', crypt('pwd17', gen_salt('bf', 12)), true, '787-021-0234'),
    (gen_random_uuid(), 'Miguel', 'Diaz', 'miguel.diaz@gmail.com', crypt('pwd18', gen_salt('bf', 12)), true, '939-004-0234'),
    (gen_random_uuid(), 'Julia', 'Fernandez', 'julia.fernandez@gmail.com', crypt('pwd19', gen_salt('bf', 12)), true, '939-009-0234'),
    (gen_random_uuid(), 'Roberto', 'Ramirez', 'roberto.ramirez@gmail.com', crypt('pwd20', gen_salt('bf', 12)), true, '787-030-0123'),
    (gen_random_uuid(), 'Alice', 'Brown', 'alice.brown@outlook.com', crypt('pwd21', gen_salt('bf', 12)), true, '787-008-0124'),
    (gen_random_uuid(), 'David', 'Wilson', 'david.wilson@outlook.com', crypt('pwd22', gen_salt('bf', 12)), true, '787-123-3424'),
    (gen_random_uuid(), 'Emma', 'Jones', 'emma.jones@outlook.com', crypt('pwd23', gen_salt('bf', 12)), true, '787-763-0643'),
    (gen_random_uuid(), 'James', 'Taylor', 'james.taylor@outlook.com', crypt('pwd24', gen_salt('bf', 12)), true, '787-121-0224'),
    (gen_random_uuid(), 'Olivia', 'Davis', 'olivia787@outlook.com', crypt('pwd25', gen_salt('bf', 12)), true, '787-678-0122'),
    (gen_random_uuid(), 'Michael', 'Evans', 'michael_office@outlook.com', crypt('pwd26', gen_salt('bf', 12)), true, '787-048-0824'),
    (gen_random_uuid(), 'Sophia', 'Clark', 'sophia.clark@outlook.com', crypt('pwd27', gen_salt('bf', 12)), true, '787-028-0144'),
    (gen_random_uuid(), 'Alexander', 'Thomas', 'alexander.thomas@outlook.com', crypt('pwd28', gen_salt('bf', 12)), true, '787-777-0129'),
    (gen_random_uuid(), 'Ava', 'White', 'ava.white@outlook.com', crypt('pwd29', gen_salt('bf', 12)), true, '787-111-0124'),
    (gen_random_uuid(), 'Matthew', 'Walker', 'matthew.walker@outlook.com', crypt('pwd30', gen_salt('bf', 12)), true, '787-333-0324');
-- Insert sample data into services table
INSERT INTO services (name)
VALUES
    ('Unas'),
    ('Jardineria'),
    ('Barberia'),
    ('Estilismo'),
    ('Pet Sitting'),
    ('Lavado de autos'),
    ('Reposteria'),
    ('Plomeria'),
    ('Servicio electrico'),
    ('House Cleaning'),
    ('Pet Grooming'),
    ('Landscaping'),
    ('Decorador de eventos'),
    ('DJ'),
    ('Catering'),
    ('Ojaleteria'),
    ('Diseno grafico'),
    ('Carpinteria'),
    ('Baby sitting'),
    ('Mantenimeinto de picsina'),
    ('Pintura');

-- Insert sample data into towns table
INSERT INTO towns (name, id)
VALUES('All', 0);
INSERT INTO towns (name)
VALUES
    ('Adjuntas'),
    ('Aguada'),
    ('Aguadilla'),
    ('Aguas Buenas'),
    ('Aibonito'),
    ('Añasco'),
    ('Arecibo'),
    ('Arroyo'),
    ('Barceloneta'),
    ('Barranquitas'),
    ('Bayamon'),
    ('Cabo Rojo'),
    ('Caguas'),
    ('Camuy'),
    ('Canovanas'),
    ('Carolina'),
    ('Cataño'),
    ('Cayey'),
    ('Ceiba'),
    ('Ciales'),
    ('Cidra'),
    ('Coamo'),
    ('Comerio'),
    ('Corozal'),
    ('Culebra'),
    ('Dorado'),
    ('Fajardo'),
    ('Florida'),
    ('Guanica'),
    ('Guayama'),
    ('Guayanilla'),
    ('Guaynabo'),
    ('Gurabo'),
    ('Hatillo'),
    ('Hormigueros'),
    ('Humacao'),
    ('Isabela'),
    ('Jayuya'),
    ('Juana Diaz'),
    ('Juncos'),
    ('Lajas'),
    ('Lares'),
    ('Las Marias'),
    ('Las Piedras'),
    ('Loiza'),
    ('Luquillo'),
    ('Manati'),
    ('Maricao'),
    ('Maunabo'),
    ('Mayaguez'),
    ('Moca'),
    ('Morovis'),
    ('Naguabo'),
    ('Naranjito'),
    ('Orocovis'),
    ('Patillas'),
    ('Penuelas'),
    ('Ponce'),
    ('Quebradillas'),
    ('Rincon'),
    ('Rio Grande'),
    ('Sabana Grande'),
    ('Salinas'),
    ('San German'),
    ('San Juan'),
    ('San Lorenzo'),
    ('San Sebastian'),
    ('Santa Isabel'),
    ('Toa Alta'),
    ('Toa Baja'),
    ('Trujillo Alto'),
    ('Utuado'),
    ('Vega Alta'),
    ('Vega Baja'),
    ('Vieques'),
    ('Villalba'),
    ('Yabucoa'),
    ('Yauco');

-- Assigning promos to users
INSERT INTO promotions (user_id, service_id, title, description, pictures)
SELECT u.id, s.id,
'Discotecas y eventos nocturnos',
'Dj profesional y acudo regularmente a discotecas en el area del norte. Mi sests incluyen desde musica urbanna, hip-hop, techno y electronica. Todo equipo necesario es proveido por mi incluyendo luces y maquinas de humo.',
'promo1.PNG|promo2.PNG'
FROM users u
JOIN services s ON s.name = 'DJ'
WHERE u.first_name = 'John' AND u.last_name = 'Doe';

INSERT INTO promotions (user_id, service_id, title, description, pictures)
SELECT u.id, s.id, 'Oferta Especial Jardineria',
'Transforma tu jardín con nuestro servicio experto de jardinería. Ofrecemos una variedad de diseños adaptados a tus preferencias.',
'promo1.PNG|promo2.PNG'
FROM users u
JOIN services s ON s.name = 'Jardineria'
WHERE u.first_name = 'Jane' AND u.last_name = 'Smith';

INSERT INTO promotions (user_id, service_id, title, description, pictures)
SELECT u.id, s.id, 'DJ Urbano',
'Obtén las últimas tendencias y éxitos musicales mezclados. Si buscas involucrar a tus clientes en tu negocio, bríndales el entretenimiento que se merecen.',
'promo1.PNG|promo2.PNG'
FROM users u
JOIN services s ON s.name = 'DJ'
WHERE u.first_name = 'Hector' AND u.last_name = 'Torres';

INSERT INTO promotions (user_id, service_id, title, description, pictures)
SELECT u.id, s.id, 'Nuevos Estilos Modernos',
'Las últimas tendencias en cabello con nuestro servicio profesional. ¡Luce espectacular en tu día especial! Nuestros estilistas destacan en el peinado para ocasiones especiales, desde recogidos elegantes hasta rizos glamorosos, asegurando que brilles en bodas, graduaciones y más.',
'promo1.PNG|promo2.PNG'
FROM users u
JOIN services s ON s.name = 'Estilismo'
WHERE u.first_name = 'Olivia' AND u.last_name = 'Davis';

INSERT INTO promotions (user_id, service_id, title, description, pictures)
SELECT u.id, s.id,
'Los Mejores Estilos',
'Descubre tu estilo de cabello ideal con nuestras consultas personalizadas. Nuestros estilistas evaluarán tu tipo de cabello, forma de rostro y estilo de vida para recomendarte el corte y estilo perfectos para ti.',
'promo1.PNG|promo2.PNG'
FROM users u
JOIN services s ON s.name = 'Estilismo'
WHERE u.first_name = 'Marta' AND u.last_name = 'Lopez';

INSERT INTO promotions (user_id, service_id, title, description, pictures)
SELECT u.id, s.id, 'Nail EXTRAVAGANZA','
Date un gusto con impresionantes diseños de arte para uñas. ¡Nuestros expertos técnicos en uñas transformarán tus uñas en obras de arte!',
'promo1.PNG|promo2.PNG'
FROM users u
JOIN services s ON s.name = 'Unas'
WHERE u.first_name = 'Maria' AND u.last_name = 'Garcia';

INSERT INTO promotions (user_id, service_id, title, description, pictures)
SELECT u.id, s.id, 'Limpieza Extrema de Hogares', '¡Experimenta la alegría de un hogar impecable! Nuestros expertos en limpieza se encargarán de todas tus necesidades de limpieza con cuidado meticuloso.',
'promo1.PNG|promo2.PNG'
FROM users u
JOIN services s ON s.name = 'House Cleaning'
WHERE u.first_name = 'Sofia' AND u.last_name = 'Rodriguez';

INSERT INTO promotions (user_id, service_id, title, description, pictures)
SELECT u.id, s.id, 'Cuidamos tu mascota', '¡El hogar de tus mascotas fuera de casa! Ofrecemos servicios personalizados de cuidado de mascotas para garantizar que tus amigos peludos estén felices y bien cuidados.',
'promo1.PNG|promo2.PNG'
FROM users u
JOIN services s ON s.name = 'Pet Sitting'
WHERE u.first_name = 'Angelica' AND u.last_name = 'Diaz';

INSERT INTO promotions (user_id, service_id, title, description, pictures)
SELECT u.id, s.id, 'Premium Car Wash', 'Revitaliza tu vehículo con nuestros servicios premium de lavado y detallado de autos. ¡Haremos que tu auto brille por dentro y por fuera!',
'promo1.PNG|promo2.PNG'
FROM users u
JOIN services s ON s.name = 'Lavado de autos'
WHERE u.first_name = 'Erick' AND u.last_name = 'Santiago';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Landscaping Masterpieces', '
Transforma tu espacio exterior en un paraíso exuberante. Nuestros expertos en paisajismo se especializan en crear paisajes hermosos y funcionales.'
FROM users u
JOIN services s ON s.name = 'Landscaping'
WHERE u.first_name = 'Gabriel' AND u.last_name = 'Rivera';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Plomeros Expertos', '¿Necesitas reparaciones o instalaciones de plomería? Ofrecemos servicios confiables de plomería adaptados a tus necesidades.'
FROM users u
JOIN services s ON s.name = 'Plomeria'
WHERE u.first_name = 'Carlos' AND u.last_name = 'Martinez';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Catering Delicioso!', 'Indulge in a gourmet feast prepared by our talented chefs. Our catering services will make your event unforgettable.'
FROM users u
JOIN services s ON s.name = 'Catering'
WHERE u.first_name = 'Laura' AND u.last_name = 'Hernandez';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Ultimate Party DJ', '
¡Prende la pista de baile con nuestros servicios energéticos de DJ!
¡Crearemos el ambiente perfecto para tu evento!'
FROM users u
JOIN services s ON s.name = 'DJ'
WHERE u.first_name = 'Javier' AND u.last_name = 'Sanchez';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Electrical Solutions', '¿Necesitas reparaciones o instalaciones eléctricas? Nuestros expertos ofrecen servicios eléctricos seguros y eficientes.'
FROM users u
JOIN services s ON s.name = 'Servicio electrico'
WHERE u.first_name = 'Daniel' AND u.last_name = 'Lopez';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Artistic Painting Services', 'Transforma tu espacio con nuestros servicios artísticos de pintura. Nuestras pinturas aportan creatividad y precisión a cada proyecto.'
FROM users u
JOIN services s ON s.name = 'Pintura'
WHERE u.first_name = 'Roberto' AND u.last_name = 'Ramirez';
-- End of inserts for promos ---------------

-- Insert requests for each user and their preferred services

-- Maria Garcia
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Birthday Party DJ', 'Se busca dj for birthday. Maximo de 6 horas'
FROM users u
JOIN services s ON s.name = 'DJ'
WHERE u.first_name = 'Jane' AND u.last_name = 'Smith';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Eventos Formales', 'Necesito DJ para eventos corporativos, son eventos formales'
FROM users u
JOIN services s ON s.name = 'DJ'
WHERE u.first_name = 'Maria' AND u.last_name = 'Garcia';

-- Jane Smith
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Decoracion de patio', 'Necesito un diseno nuevo en nuestro patio interior!'
FROM users u
JOIN services s ON s.name = 'Jardineria'
WHERE u.first_name = 'Jane' AND u.last_name = 'Smith';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Front Yard Landscaping', 'Paisajista que pueda re-decorar el patio interior a un estilo mas europeo'
FROM users u
JOIN services s ON s.name = 'Landscaping'
WHERE u.first_name = 'Jane' AND u.last_name = 'Smith';

-- Luis Santiago
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Limpieza de hogar', 'Mi madre necesita una limpieza del hogar completa ya que no puede sola'
FROM users u
JOIN services s ON s.name = 'House Cleaning'
WHERE u.first_name = 'Luis' AND u.last_name = 'Santiago';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Semanal Asistencia', 'Asistencia en limpieza semanal de apartamentos'
FROM users u
JOIN services s ON s.name = 'House Cleaning'
WHERE u.first_name = 'Luis' AND u.last_name = 'Santiago';

-- Hector Torres
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Emergencia de plomeria', 'Ayuda de emergencia en tuberias rotas en un segundo piso!'
FROM users u
JOIN services s ON s.name = 'Plomeria'
WHERE u.first_name = 'Hector' AND u.last_name = 'Torres';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Problemas de luces', 'Tengo problema con todas las luces del patio'
FROM users u
JOIN services s ON s.name = 'Servicio electrico'
WHERE u.first_name = 'Hector' AND u.last_name = 'Torres';

-- Angelica Diaz
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Pet Sitting', 'Necesito que alguien cuide mi gato durante 6 horas para este proximo Lunes'
FROM users u
JOIN services s ON s.name = 'Pet Sitting'
WHERE u.first_name = 'Angelica' AND u.last_name = 'Diaz';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Pet Grooming', 'Solicito un servicio de grooming a domicilio para mi perrito que esta viejito ya'
FROM users u
JOIN services s ON s.name = 'Pet Grooming'
WHERE u.first_name = 'Angelica' AND u.last_name = 'Diaz';

-- Erick Santiago
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Lavado de auto a domicilio fin de semana', 'Alguien que pueda pasar por casa a lavar 4 autos???'
FROM users u
JOIN services s ON s.name = 'Lavado de autos'
WHERE u.first_name = 'Erick' AND u.last_name = 'Santiago';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Ojaleteria', 'Necesito pintar mi corolla 2002, pintura con perlas.'
FROM users u
JOIN services s ON s.name = 'Ojaleteria'
WHERE u.first_name = 'Erick' AND u.last_name = 'Santiago';

-- Maria Garcia
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Bizcocho para evento coorporativo', 'Busco Bizcocho para evento coorporativo.'
FROM users u
JOIN services s ON s.name = 'Reposteria'
WHERE u.first_name = 'Maria' AND u.last_name = 'Garcia';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Event Catering', 'Catering para aniversario en la tarde.'
FROM users u
JOIN services s ON s.name = 'Catering'
WHERE u.first_name = 'Maria' AND u.last_name = 'Garcia';

-- Carlos Martinez
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Recorte para persona encamada', 'Tengo una persona de edad avanzada encamada que necesita un recorte.'
FROM users u
JOIN services s ON s.name = 'Barberia'
WHERE u.first_name = 'Carlos' AND u.last_name = 'Martinez';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Estilista para sweet 16', 'Evento especial para mi hija, necesitamos una estilista que pueda cumplir con lo que necesite ella.'
FROM users u
JOIN services s ON s.name = 'Estilismo'
WHERE u.first_name = 'Carlos' AND u.last_name = 'Martinez';

-- Sofia Rodriguez
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Mural para restaurante', 'Restaurante necesita un mural para llamar la atencion! Necesito algo bonito gracias!'
FROM users u
JOIN services s ON s.name = 'Pintura'
WHERE u.first_name = 'Sofia' AND u.last_name = 'Rodriguez';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Evento especial de boda', 'Necesitamos ayuda con un evento antes de boda, va a tenr multiples decoraciones'
FROM users u
JOIN services s ON s.name = 'Decorador de eventos'
WHERE u.first_name = 'Sofia' AND u.last_name = 'Rodriguez';

-- End of requests inserts ---------


-- Insert promotions into promo_towns

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('San Juan', 'Carolina', 'Bayamon', 'Santurce', 'Guaynabo')
WHERE p.title = 'Discotecas y eventos nocturnos' AND u.first_name = 'John' AND u.last_name = 'Doe' AND s.name = 'DJ';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Ponce', 'Juana Diaz')
WHERE p.title = 'Plomeros Expertos' AND u.first_name = 'Carlos' AND u.last_name = 'Martinez' AND s.name = 'Plomeria';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Ponce', 'Salinas', 'Santa Isabel', 'Coamo', 'Juana Diaz')
WHERE p.title = 'Landscaping Masterpieces' AND u.first_name = 'Gabriel' AND u.last_name = 'Rivera' AND s.name = 'DJ';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Aguadilla', 'Isabela', 'Mayaguez', 'Rincon', 'San Sebastian')
WHERE p.title = 'Oferta Especial Jardineria' AND u.first_name = 'Jane' AND u.last_name = 'Smith' AND s.name = 'Jardineria';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Aguadilla', 'Isabela', 'Bayamon', 'Rincon', 'San Sebastian')
WHERE p.title = 'Catering Delicioso!' AND u.first_name = 'Laura' AND u.last_name = 'Hernandez' AND s.name = 'Catering';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('All')
WHERE p.title = 'DJ Urbano' AND u.first_name = 'Hector' AND u.last_name = 'Torres' AND s.name = 'DJ';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('San Juan', 'Carolina', 'Bayamon', 'Santurce', 'Guaynabo')
WHERE p.title = 'Nuevos Estilos Modernos' AND u.first_name = 'Olivia' AND u.last_name = 'Davis' AND s.name = 'Estilismo';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Aibonito', 'Cayey', 'Guayama')
WHERE p.title = 'Los Mejores Estilos' AND u.first_name = 'Marta' AND u.last_name = 'Lopez' AND s.name = 'Estilismo';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Carolina')
WHERE p.title = 'Nail EXTRAVAGANZA' AND u.first_name = 'Maria' AND u.last_name = 'Garcia' AND s.name = 'Unas';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Fajardo')
WHERE p.title = 'Limpieza Extrema de Hogares' AND u.first_name = 'Sofia' AND u.last_name = 'Rodriguez' AND s.name = 'Decorador de eventos';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('All')
WHERE p.title = 'Cuidamos tu mascota' AND u.first_name = 'Angelica' AND u.last_name = 'Diaz' AND s.name = 'Pet Sitting';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Carolina', 'San Juan', 'Guaynabo', 'Bayamon', 'Santurce')
WHERE p.title = 'Premium Car Wash' AND u.first_name = 'Erick' AND u.last_name = 'Santiago' AND s.name = 'Lavado de autos';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Carolina', 'Guaynabo')
WHERE p.title = 'Electrical Solutions' AND u.first_name = 'Daniel' AND u.last_name = 'Lopez' AND s.name = 'Servicio electrico';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Santurce', 'Bayamon')
WHERE p.title = 'Artistic Painting Services' AND u.first_name = 'Roberto' AND u.last_name = 'Ramirez' AND s.name = 'Pintura';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Santurce', 'Bayamon')
WHERE p.title = 'Ultimate Party DJ' AND u.first_name = 'Javier' AND u.last_name = 'Sanchez' AND s.name = 'DJ';

-- Output confirmation
SELECT 'Promotions assigned to towns successfully' AS Status;


-- Insert Requests into Request_town
-- Insert Requests into Request_town for John Doe's requests
INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Ponce'
WHERE r.title = 'Birthday Party DJ'
AND u.first_name = 'John'
AND u.last_name = 'Doe';

-- Insert into request_towns for John Doe's Eventos Formales request (Specify the town)
INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Bayamon'
WHERE r.title = 'Eventos Formales'
AND u.first_name = 'John'
AND u.last_name = 'Doe';

-- Insert Requests into Request_town for Jane Smith's requests
INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Aguadilla'
WHERE r.title = 'Decoracion de patio'
AND u.first_name = 'Jane'
AND u.last_name = 'Smith';

INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Caguas'
WHERE r.title = 'Front Yard Landscaping'
AND u.first_name = 'Jane'
AND u.last_name = 'Smith';

-- Insert Requests into Request_town for Luis Santiago's requests
INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Coamo'
WHERE r.title = 'Limpieza de hogar'
AND u.first_name = 'Luis'
AND u.last_name = 'Santiago';

INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Aibonito'
WHERE r.title = 'Semanal Asistencia'
AND u.first_name = 'Luis'
AND u.last_name = 'Santiago';

-- Insert Requests into Request_town for Hector Torres's requests
INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'San German'
WHERE r.title = 'Emergencia de plomeria'
AND u.first_name = 'Hector'
AND u.last_name = 'Torres';

INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Rincon'
WHERE r.title = 'Problemas de luces'
AND u.first_name = 'Hector'
AND u.last_name = 'Torres';

-- Insert Requests into Request_town for Angelica Diaz's requests
INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Carolina'
WHERE r.title = 'Pet Sitting'
AND u.first_name = 'Angelica'
AND u.last_name = 'Diaz';

INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Vega Baja'
WHERE r.title = 'Pet Grooming'
AND u.first_name = 'Angelica'
AND u.last_name = 'Diaz';

-- Insert Requests into Request_town for Erick Santiago's requests
INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Arecibo'
WHERE r.title = 'Lavado de auto a domicilio fin de semana'
AND u.first_name = 'Erick'
AND u.last_name = 'Santiago';

INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Carolina'
WHERE r.title = 'Ojaleteria'
AND u.first_name = 'Erick'
AND u.last_name = 'Santiago';

-- Insert Requests into Request_town for Maria Garcia's requests
INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Caguas'
WHERE r.title = 'Bizcocho para evento coorporativo'
AND u.first_name = 'Maria'
AND u.last_name = 'Garcia';

INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'San Juan'
WHERE r.title = 'Event Catering'
AND u.first_name = 'Maria'
AND u.last_name = 'Garcia';

-- Insert Requests into Request_town for Carlos Martinez's requests
INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Aibonito'
WHERE r.title = 'Recorte para persona encamada'
AND u.first_name = 'Carlos'
AND u.last_name = 'Martinez';

INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'San Juan'
WHERE r.title = 'Estilista para sweet 16'
AND u.first_name = 'Carlos'
AND u.last_name = 'Martinez';

-- Insert Requests into Request_town for Sofia Rodriguez's requests
INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Ponce'
WHERE r.title = 'Mural para restaurante'
AND u.first_name = 'Sofia'
AND u.last_name = 'Rodriguez';

INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Bayamon'
WHERE r.title = 'Evento especial de boda'
AND u.first_name = 'Sofia'
AND u.last_name = 'Rodriguez';

-- Create initial contact, task and review
-- Initial contact A1
INSERT INTO initial_contacts (sender_id, receiver_id, promo_id, receiver_read, sender_read, sent_task)
SELECT 
    u1.id AS sender_id,           -- Jane Smith (service requester)
    u2.id AS receiver_id,         -- John Doe (service provider)
    p.id AS promo_id, 
    true AS receiver_read,
    true AS sender_read,
    true AS sent_task
FROM 
    users u1
JOIN 
    users u2 ON u2.first_name = 'John' AND u2.last_name = 'Doe' -- Receiver (service provider)
JOIN 
    promotions p ON p.title = 'Discotecas y eventos nocturnos'
WHERE 
    u1.first_name = 'Jane' AND u1.last_name = 'Smith'
LIMIT 1; -- Sender (service requester)

-- Task A1
INSERT INTO tasks (promo_id, provider_id, receiver_id, initial_contact_id, service_id, status, description)
SELECT 
    p.id AS promo_id, 
    u2.id AS provider_id,        -- John Doe (service provider)
    u1.id AS receiver_id,        -- Jane Smith (service requester)
    ic.id AS initial_contact_id,
    p.service_id AS service_id, 
    'reviewed' AS status, 
    'TASK DESCRIPTION: ' || p.title AS description
FROM 
    promotions p
JOIN 
    initial_contacts ic ON ic.promo_id = p.id
JOIN 
    users u1 ON u1.id = ic.sender_id -- Ensure sender of initial contact
JOIN 
    users u2 ON u2.id = ic.receiver_id -- Ensure receiver of initial contact
WHERE 
    p.title = 'Discotecas y eventos nocturnos'
    AND u1.first_name = 'Jane' AND u1.last_name = 'Smith';

-- Review A1
INSERT INTO reviews (description, task_id, rating, pictures, user_id)
VALUES (
    'Awesome DJ performance, kept the party going! Variety of songs, tracks, mixes, all was awesome!', 
    (SELECT id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Discotecas y eventos nocturnos' LIMIT 1), 
    5, 
    'https://www.austinchronicle.com/binary/ba6f/Doc-Daneeka---Kingdom-_3_.jpg',
    (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Discotecas y eventos nocturnos' LIMIT 1)
);

-- Initial contact A2
INSERT INTO initial_contacts (sender_id, receiver_id, promo_id, receiver_read, sender_read, sent_task)
SELECT 
    u1.id AS sender_id,           -- Hector Torres (service requester)
    u2.id AS receiver_id,         -- John Doe (service provider)
    p.id AS promo_id, 
    true AS receiver_read, 
    true AS sender_read,
    true AS sent_task
FROM 
    users u1
JOIN 
    users u2 ON u2.first_name = 'John' AND u2.last_name = 'Doe' -- Receiver (service provider)
JOIN 
    promotions p ON p.title = 'Discotecas y eventos nocturnos'
WHERE 
    u1.first_name = 'Hector' AND u1.last_name = 'Torres'
LIMIT 1; -- Sender (service requester)

-- Task A2
INSERT INTO tasks (promo_id, provider_id, receiver_id, initial_contact_id, service_id, status, description)
SELECT 
    p.id AS promo_id, 
    u2.id AS provider_id,        -- John Doe (service provider)
    u1.id AS receiver_id,        -- Hector Torres (service requester)
    ic.id AS initial_contact_id,
    p.service_id AS service_id, 
    'reviewed' AS status, 
    '2 TASK DESCRIPTION: ' || p.title AS description
FROM 
    promotions p
JOIN 
    initial_contacts ic ON ic.promo_id = p.id
JOIN 
    users u1 ON u1.id = ic.sender_id -- Ensure sender of initial contact
JOIN 
    users u2 ON u2.id = ic.receiver_id -- Ensure receiver of initial contact
WHERE 
    p.title = 'Discotecas y eventos nocturnos'
    AND u1.first_name = 'Hector' AND u1.last_name = 'Torres';

-- Review A2
INSERT INTO reviews (description, task_id, rating, pictures, user_id)
VALUES (
    'Awesome, kept the party going! Would hire again. It was a great experience. Next time we will have him for the company party.', 
    (SELECT id FROM tasks WHERE description LIKE '2 TASK DESCRIPTION: Discotecas y eventos nocturnos' LIMIT 1), 
    5, 
    'https://www.austinchronicle.com/binary/ba6f/Doc-Daneeka---Kingdom-_3_.jpg',
    (SELECT receiver_id FROM tasks WHERE description LIKE '2 TASK DESCRIPTION: Discotecas y eventos nocturnos' LIMIT 1)
);

-- Initial contact B1 (Assuming this is a separate promotion)
INSERT INTO initial_contacts (sender_id, receiver_id, promo_id, receiver_read, sender_read, sent_task)
SELECT 
    u1.id AS sender_id,           -- John Doe (service requester)
    u2.id AS receiver_id,         -- Hector Torres (service provider)
    p.id AS promo_id, 
    true AS receiver_read,
    true AS sender_read,
    true AS sent_task
FROM 
    users u1
JOIN 
    users u2 ON u2.first_name = 'Hector' AND u2.last_name = 'Torres' -- Receiver (service provider)
JOIN 
    promotions p ON p.title = 'DJ Urbano'
WHERE 
    u1.first_name = 'John' AND u1.last_name = 'Doe'
LIMIT 1; -- Sender (service requester)

-- Task B1
INSERT INTO tasks (promo_id, provider_id, receiver_id, initial_contact_id, service_id, status, description)
SELECT 
    p.id AS promo_id, 
    u2.id AS provider_id,        -- Hector Torres (service provider)
    u1.id AS receiver_id,        -- John Doe (service requester)
    ic.id AS initial_contact_id,
    p.service_id AS service_id, 
    'reviewed' AS status, 
    'TASK DESCRIPTION: ' || p.title AS description
FROM 
    promotions p
JOIN 
    initial_contacts ic ON ic.promo_id = p.id
JOIN 
    users u1 ON u1.id = ic.sender_id -- Ensure sender of initial contact
JOIN 
    users u2 ON u2.id = ic.receiver_id -- Ensure receiver of initial contact
WHERE 
    p.title = 'DJ Urbano'
    AND u1.first_name = 'John' AND u1.last_name = 'Doe';

-- Review B1
INSERT INTO reviews (description, task_id, rating, pictures, user_id)
VALUES (
    'Great mix of music, everyone enjoyed the beats.', 
    (SELECT id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: DJ Urbano' LIMIT 1), 
    4, 
    'https://djintershade.com/wp-content/uploads/2022/02/95DF5BD2-C9D4-4C27-B277-C159BAC1ECBB-scaled-1-2048x1536.jpeg',
    (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: DJ Urbano' LIMIT 1)
);

-- Initial contact C1 (Assuming this is a separate promotion)
INSERT INTO initial_contacts (sender_id, receiver_id, promo_id, receiver_read, sender_read, sent_task)
SELECT 
    u1.id AS sender_id,           -- John Doe (service requester)
    u2.id AS receiver_id,         -- Jane Smith (service provider)
    p.id AS promo_id, 
    true AS receiver_read,
    true AS sender_read,
    true AS sent_task
FROM 
    users u1
JOIN 
    users u2 ON u2.first_name = 'Jane' AND u2.last_name = 'Smith' -- Receiver (service provider)
JOIN 
    promotions p ON p.title = 'Oferta Especial Jardineria'
WHERE 
    u1.first_name = 'John' AND u1.last_name = 'Doe'
LIMIT 1; -- Sender (service requester)

-- Task C1
INSERT INTO tasks (promo_id, provider_id, receiver_id, initial_contact_id, service_id, status, description)
SELECT 
    p.id AS promo_id, 
    u2.id AS provider_id,        -- Jane Smith (service provider)
    u1.id AS receiver_id,        -- John Doe (service requester)
    ic.id AS initial_contact_id,
    p.service_id AS service_id, 
    'reviewed' AS status, 
    'TASK DESCRIPTION: ' || p.title AS description
FROM 
    promotions p
JOIN 
    initial_contacts ic ON ic.promo_id = p.id
JOIN 
    users u1 ON u1.id = ic.sender_id -- Ensure sender of initial contact
JOIN 
    users u2 ON u2.id = ic.receiver_id -- Ensure receiver of initial contact
WHERE 
    p.title = 'Oferta Especial Jardineria'
    AND u1.first_name = 'John' AND u1.last_name = 'Doe';

-- Review C1
INSERT INTO reviews (description, task_id, rating, pictures, user_id)
VALUES (
    'Beautiful garden transformation, very pleased. Started small but will hire again for future projects.', 
    (SELECT id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Oferta Especial Jardineria' LIMIT 1), 
    5, 
    'https://www.bobvila.com/wp-content/uploads/2023/08/Vego-Garden-Raised-Beds-Review.jpg',
    (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Oferta Especial Jardineria' LIMIT 1)
);

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK2 DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'DJ Urbano';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK3 DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'DJ Urbano';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK4 DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'DJ Urbano';

-- -- Insert tasks related to promotions
-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'Oferta Especial Jardineria';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK2 DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'Oferta Especial Jardineria';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK3 DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'Oferta Especial Jardineria';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'Nuevos Estilos Modernos';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'Los Mejores Estilos';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'Nail EXTRAVAGANZA';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'Limpieza Extrema de Hogares';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'Cuidamos tu mascota';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'Premium Car Wash';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'Landscaping Masterpieces';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'Plomeros Expertos';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'Catering Delicioso!';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'Ultimate Party DJ';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'Electrical Solutions';

-- INSERT INTO tasks (promo_id, provider_id, receiver_id, service_id, status, description)
-- SELECT p.id, p.user_id, r.id, p.service_id, 'closed', 'TASK DESCRIPTION: ' || p.title
-- FROM promotions p
-- JOIN users r ON r.id = (SELECT id FROM users WHERE id <> p.user_id LIMIT 1)
-- WHERE p.title = 'Artistic Painting Services';

-- Inserting reviews for tasks related to promotions


-- Review

-- -- DJ Urbano (Good communication and service from the DJ.)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Good communication and service from the DJ.', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK2 DESCRIPTION: DJ Urbano' LIMIT 1), 
--         4, 
--         NULL,
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK2 DESCRIPTION: DJ Urbano' LIMIT 1));

-- -- DJ Urbano (Diverse music selection, accommodated all requests.)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Diverse music selection, accommodated all requests.', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK3 DESCRIPTION: DJ Urbano' LIMIT 1), 
--         5, 
--         NULL,
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK3 DESCRIPTION: DJ Urbano' LIMIT 1));

-- -- DJ Urbano (Professional setup, created a lively atmosphere.)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Professional setup, created a lively atmosphere.', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK4 DESCRIPTION: DJ Urbano' LIMIT 1), 
--         4, 
--         NULL,
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK4 DESCRIPTION: DJ Urbano' LIMIT 1));


-- -- Oferta Especial Jardineria (Highly recommend their Jardineria services.)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Highly recommend their Jardineria services.', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK2 DESCRIPTION: Oferta Especial Jardineria' LIMIT 1), 
--         5, 
--         NULL,
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK2 DESCRIPTION: Oferta Especial Jardineria' LIMIT 1));

-- -- Oferta Especial Jardineria (Efficient work, completed the job on time.)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Efficient work, completed the job on time.', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK3 DESCRIPTION: Oferta Especial Jardineria' LIMIT 1), 
--         4, 
--         NULL,
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK3 DESCRIPTION: Oferta Especial Jardineria' LIMIT 1));

-- -- Nuevos Estilos Modernos (Stunning hairstyle, exactly what I wanted!)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Stunning hairstyle, exactly what I wanted!', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Nuevos Estilos Modernos' LIMIT 1), 
--         5, 
--         'https://example.com/hairstyle2.jpg',
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Nuevos Estilos Modernos' LIMIT 1));

-- -- Los Mejores Estilos (Great consultation, got the perfect hairstyle.)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Great consultation, got the perfect hairstyle.', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Los Mejores Estilos' LIMIT 1), 
--         4, 
--         NULL,
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Los Mejores Estilos' LIMIT 1));

-- -- Nail EXTRAVAGANZA (Creative nail designs, exceeded expectations!)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Creative nail designs, exceeded expectations!', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Nail EXTRAVAGANZA' LIMIT 1), 
--         5, 
--         'https://example.com/Unas.jpg',
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Nail EXTRAVAGANZA' LIMIT 1));

-- -- Limpieza Extrema de Hogares (Thorough cleaning job, everything looks pristine.)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Thorough cleaning job, everything looks pristine.', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Limpieza Extrema de Hogares' LIMIT 1), 
--         5, 
--         NULL,
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Limpieza Extrema de Hogares' LIMIT 1));

-- -- Cuidamos tu mascota (Pets were happy and well cared for.)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Pets were happy and well cared for.', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Cuidamos tu mascota' LIMIT 1), 
--         4, 
--         NULL,
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Cuidamos tu mascota' LIMIT 1));

-- -- Premium Car Wash (Car looks brand new after the detailing.)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Car looks brand new after the detailing.', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Premium Car Wash' LIMIT 1), 
--         5, 
--         'https://example.com/car2.jpg',
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Premium Car Wash' LIMIT 1));

-- -- Landscaping Masterpieces (Beautiful landscaping design, very professional.)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Beautiful landscaping design, very professional.', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Landscaping Masterpieces' LIMIT 1), 
--         5, 
--         NULL,
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Landscaping Masterpieces' LIMIT 1));

-- -- Plomeros Expertos (Fixed the Plomeria issue quickly and effectively.)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Fixed the Plomeria issue quickly and effectively.', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Plomeros Expertos' LIMIT 1), 
--         4, 
--         NULL,
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Plomeros Expertos' LIMIT 1));

-- -- Catering Delicioso! (Delicious food, everyone enjoyed the catering.)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Delicious food, everyone enjoyed the catering.', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Catering Delicioso!' LIMIT 1), 
--         5, 
--         'https://example.com/catering2.jpg',
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Catering Delicioso!' LIMIT 1));

-- -- Ultimate Party DJ (DJ created a fantastic atmosphere for the party.)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('DJ created a fantastic atmosphere for the party.', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Ultimate Party DJ' LIMIT 1), 
--         5, 
--         NULL,
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Ultimate Party DJ' LIMIT 1));

-- -- Electrical Solutions (Resolved electrical issues efficiently.)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Resolved electrical issues efficiently.', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Electrical Solutions' LIMIT 1), 
--         4, 
--         NULL,
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Electrical Solutions' LIMIT 1));

-- -- Artistic Painting Services (Transformed the space with creative painting.)
-- INSERT INTO reviews (description, task_id, rating, pictures, user_id)
-- VALUES ('Transformed the space with creative painting.', 
--         (SELECT id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Artistic Painting Services' LIMIT 1), 
--         5, 
--         'https://example.com/painting2.jpg',
--         (SELECT receiver_id FROM tasks WHERE description LIKE 'TASK DESCRIPTION: Artistic Painting Services' LIMIT 1));

-- Populate Profiles table
INSERT INTO profiles(user_id, job_title, bio, tasks_completed)
SELECT 
    users.id as user_id,
    'Dj' as job_title,
    'Experto en mixes urbanos, trabajo en discotecas area norte' as bio,
    2 as tasks_completed
    from users
    where users.first_name = 'John' and users.last_name = 'Doe';

INSERT INTO profiles(user_id, job_title, bio, tasks_completed)
SELECT 
    users.id as user_id,
    'Jardinera de por vida' as job_title,
    'Los jardines son mi pasión. Con mucho amor y dedicación, hago que tu jardín cobre vida.' as bio,
    1 as tasks_completed
    from users
    where users.first_name = 'Jane' and users.last_name = 'Smith';

INSERT INTO profiles(user_id, job_title, bio, tasks_completed)
SELECT 
    users.id as user_id,
    'Ingeniero de audio' as job_title,
    'Profesional y graduado de ingenieria de sonido' as bio,
    1 as tasks_completed
    from users
    where users.first_name = 'Hector' and users.last_name = 'Torres';

INSERT INTO profiles(user_id, job_title, bio, tasks_completed)
SELECT 
    users.id as user_id,
    'Estilista' as job_title,
    'Me especializo en peinados para ocasiones especiales, asegurando que luzcas espectacular en tu día especial.' as bio,
    0 as tasks_completed
    from users
    where users.first_name = 'Olivia' and users.last_name = 'Davis';

INSERT INTO profiles(user_id, job_title, bio, tasks_completed)
SELECT 
    users.id as user_id,
    'Estilista <3' as job_title,
    'Descubre tu estilo ideal de peinado con consultas personalizadas y estilistas expertos.' as bio,
    0 as tasks_completed
    from users
    where users.first_name = 'Marta' and users.last_name = 'Lopez';

INSERT INTO profiles(user_id, job_title, bio, tasks_completed)
SELECT 
    users.id as user_id,
    'Técnica de uñas' as job_title,
    'Transforma tus uñas en impresionantes obras de arte con nuestros diseños expertos.' as bio,
    0 as tasks_completed
    from users
    where users.first_name = 'Maria' and users.last_name = 'Garcia';

INSERT INTO profiles(user_id, job_title, bio, tasks_completed)
SELECT 
    users.id as user_id,
    'House Cleaner' as job_title,
    'Experimenta la alegría de un hogar impecable con servicios de limpieza meticulosos.' as bio,
    0 as tasks_completed
    from users
    where users.first_name = 'Sofia' and users.last_name = 'Rodriguez';

INSERT INTO profiles(user_id, job_title, bio, tasks_completed)
SELECT 
    users.id as user_id,
    'Cuidador de mascotas' as job_title,
    'El hogar de tus mascotas fuera de casa con servicios personalizados de cuidado de mascotas.' as bio,
    0 as tasks_completed
    from users
    where users.first_name = 'Angelica' and users.last_name = 'Diaz';

INSERT INTO profiles(user_id, job_title, bio, tasks_completed)
SELECT 
    users.id as user_id,
    'Limpieza de autos' as job_title,
    'Revitaliza tu vehículo con servicios premium de lavado y detalle de autos.' as bio,
    0 as tasks_completed
    from users
    where users.first_name = 'Erick' and users.last_name = 'Santiago';

INSERT INTO profiles(user_id, job_title, bio, tasks_completed)
SELECT 
    users.id as user_id,
    'Landscaper' as job_title,
    'Transforma tu espacio exterior en un paraíso exuberante con paisajismo experto.' as bio,
    0 as tasks_completed
    from users
    where users.first_name = 'Gabriel' and users.last_name = 'Rivera';

INSERT INTO profiles(user_id, job_title, bio, tasks_completed)
SELECT 
    users.id as user_id,
    'Plomero Experto' as job_title,
    'Servicios confiables de plomería adaptados a tus necesidades.' as bio,
    0 as tasks_completed
    from users
    where users.first_name = 'Carlos' and users.last_name = 'Martinez';

INSERT INTO profiles(user_id, job_title, bio, tasks_completed)
SELECT 
    users.id as user_id,
    'Caterer' as job_title,
    'Disfruta de un festín gourmet preparado por talentosos chefs.' as bio,
    0 as tasks_completed
    from users
    where users.first_name = 'Laura' and users.last_name = 'Hernandez';

INSERT INTO profiles(user_id, job_title, bio, tasks_completed)
SELECT 
    users.id as user_id,
    'DJ' as job_title,
    'Desata el Ritmo: Eleva tu Evento con Servicios Dinámicos de DJ!' as bio,
    0 as tasks_completed
    from users
    where users.first_name = 'Javier' and users.last_name = 'Sanchez';

INSERT INTO profiles(user_id, job_title, bio, tasks_completed)
SELECT 
    users.id as user_id,
    'Electricista' as job_title,
    'Servicio eléctrico seguro y eficiente para reparaciones e instalaciones.' as bio,
    0 as tasks_completed
    from users
    where users.first_name = 'Daniel' and users.last_name = 'Lopez';

INSERT INTO profiles(user_id, job_title, bio, tasks_completed)
SELECT 
    users.id as user_id,
    'Pintura' as job_title,
    'Transforma tu espacio con servicios artísticos de pintura, llevando creatividad y precisión a cada proyecto.' as bio,
    0 as tasks_completed
    from users
    where users.first_name = 'Roberto' and users.last_name = 'Ramirez';


-- Output confirmation
SELECT 'Tables created and populated successfully' AS Status;
