-- Drop foreign key constraints

ALTER TABLE IF EXISTS user_service_association DROP CONSTRAINT IF EXISTS user_service_association_user_id_fkey;
ALTER TABLE IF EXISTS user_service_association DROP CONSTRAINT IF EXISTS user_service_association_service_id_fkey;




-- Drop tables if they exist (for testing purposes)
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS user_service_association;

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
--  Create table for user_service_association
CREATE TABLE user_service_association (
    user_id UUID REFERENCES users(id),
    service_id UUID REFERENCES services(id),
    PRIMARY KEY (user_id, service_id)
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


-- Update users to have associated services
-- Assign 'Gardening' service to 'John'
INSERT INTO user_service_association (user_id, service_id)
VALUES (
    (SELECT id FROM users WHERE first_name = 'John' LIMIT 1), 
    (SELECT id FROM services WHERE name = 'Gardening' LIMIT 1)
);

-- Assign 'Nails' service to 'Jane'
INSERT INTO user_service_association (user_id, service_id)
VALUES (
    (SELECT id FROM users WHERE first_name = 'Jane' LIMIT 1), 
    (SELECT id FROM services WHERE name = 'Nails' LIMIT 1)
);

-- Assign 'Barber' service to 'Erick'
INSERT INTO user_service_association (user_id, service_id)
VALUES (
    (SELECT id FROM users WHERE first_name = 'Erick' LIMIT 1), 
    (SELECT id FROM services WHERE name = 'Barber' LIMIT 1)
);

-- Output confirmation
SELECT 'Tables created and populated successfully' AS Status;
