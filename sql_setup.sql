-- Drop foreign key constraints
ALTER TABLE IF EXISTS users_services_assc DROP CONSTRAINT IF EXISTS users_services_assc_user_id_fkey;
ALTER TABLE IF EXISTS users_services_assc DROP CONSTRAINT IF EXISTS users_services_assc_service_id_fkey;

-- Drop tables if they exist (for testing purposes)
DROP TABLE IF EXISTS users_services_assc;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS towns;

-- Create table for User
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create table for Service
CREATE TABLE services (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create table for towns
CREATE TABLE towns (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create table for users_services_association
CREATE TABLE users_services_assc (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) NOT NULL,
    service_id UUID REFERENCES services(id) NOT NULL,
    town_id UUID REFERENCES towns(id) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_user_service_town UNIQUE (user_id, service_id, town_id)
);

-- Insert sample data into users table
INSERT INTO users (id, first_name, last_name)
VALUES
    (gen_random_uuid(), 'John', 'Doe'),
    (gen_random_uuid(), 'Jane', 'Smith'),
    (gen_random_uuid(), 'Erick', 'Santiago');

-- Insert sample data into services table
INSERT INTO services (id, name)
VALUES
    (gen_random_uuid(), 'Nails'),
    (gen_random_uuid(), 'Gardening'),
    (gen_random_uuid(), 'Barber');

-- Insert sample data into towns table
INSERT INTO towns (id, name)
VALUES
    (gen_random_uuid(), 'Ponce'),
    (gen_random_uuid(), 'Juana Diaz'),
    (gen_random_uuid(), 'Salinas'),
    (gen_random_uuid(), 'Coamo');

-- Assign 'Barber' service to 'John' in 'Ponce'
INSERT INTO users_services_assc (user_id, service_id, town_id)
VALUES (
    (SELECT id FROM users WHERE first_name = 'John' LIMIT 1),
    (SELECT id FROM services WHERE name = 'Barber' LIMIT 1),
    (SELECT id FROM towns WHERE name = 'Ponce' LIMIT 1)
);

-- Assign 'Gardening' service to 'Erick' in 'Coamo' and 'Salinas'
INSERT INTO users_services_assc (user_id, service_id, town_id)
VALUES (
    (SELECT id FROM users WHERE first_name = 'Erick' LIMIT 1),
    (SELECT id FROM services WHERE name = 'Gardening' LIMIT 1),
    (SELECT id FROM towns WHERE name = 'Coamo' LIMIT 1)
),
(
    (SELECT id FROM users WHERE first_name = 'Erick' LIMIT 1),
    (SELECT id FROM services WHERE name = 'Gardening' LIMIT 1),
    (SELECT id FROM towns WHERE name = 'Salinas' LIMIT 1)
);

-- Assign 'Nails' service to 'Jane' in 'Ponce' and 'Juana Diaz'
INSERT INTO users_services_assc (user_id, service_id, town_id)
VALUES (
    (SELECT id FROM users WHERE first_name = 'Jane' LIMIT 1),
    (SELECT id FROM services WHERE name = 'Nails' LIMIT 1),
    (SELECT id FROM towns WHERE name = 'Ponce' LIMIT 1)
),
(
    (SELECT id FROM users WHERE first_name = 'Jane' LIMIT 1),
    (SELECT id FROM services WHERE name = 'Nails' LIMIT 1),
    (SELECT id FROM towns WHERE name = 'Juana Diaz' LIMIT 1)
);

-- Assign 'Gardening' service to 'Jane' in 'Ponce'
INSERT INTO users_services_assc (user_id, service_id, town_id)
VALUES (
    (SELECT id FROM users WHERE first_name = 'Jane' LIMIT 1),
    (SELECT id FROM services WHERE name = 'Gardening' LIMIT 1),
    (SELECT id FROM towns WHERE name = 'Ponce' LIMIT 1)
);

-- Output confirmation
SELECT 'Tables created and populated successfully' AS Status;
