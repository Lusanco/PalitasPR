-- Drop tables if they exist (for testing purposes)
DROP TABLE IF EXISTS user_service_assoc;
DROP TABLE IF EXISTS categories_service_assoc;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS towns;
DROP TABLE IF EXISTS categories;

-- Create table for User
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create table for Service
CREATE TABLE services (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create table for towns
CREATE TABLE towns (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- Create table for user_service_assoc
CREATE TABLE user_service_assoc (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE NOT NULL,
    service_id UUID REFERENCES services(id) ON DELETE CASCADE NOT NULL,
    town_id UUID REFERENCES towns(id) ON DELETE CASCADE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_user_service_town UNIQUE (user_id, service_id, town_id)
);

-- Insert sample data into users table with simulated email addresses
INSERT INTO users (id, first_name, last_name, email)
VALUES
    (gen_random_uuid(), 'John', 'Doe', 'jd123@gmail.com'),
    (gen_random_uuid(), 'Jane', 'Smith', 'jane006@gmail.com');

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


-- End of assingments


-- Output confirmation
SELECT 'Tables created and populated successfully' AS Status;
