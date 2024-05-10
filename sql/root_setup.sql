-- Drop tables if they exist (for testing purposes)
DROP TABLE IF EXISTS user_service_assoc;
DROP TABLE IF EXISTS request_towns;
DROP TABLE If EXISTS promo_towns;
DROP Table IF EXISTS promotions;
DROP Table IF EXISTS requests;
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS towns;
-- Create Extension for encryption
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Create table for User
CREATE TABLE users (
    id VARCHAR(50) PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR(50),
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    verified BOOLEAN DEFAULT false,
    verification_token VARCHAR(128) UNIQUE,
    password VARCHAR(255) NOT NULL,
    profile_pic VARCHAR(150),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create table for Service
CREATE TABLE services (
    id Serial PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

--  Create Table for reviews
CREATE TABLE reviews (
    id VARCHAR(50) PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR(50),
    description Text NOT NULL,
    rating NUMERIC(2, 1) CHECK (rating >= 1 AND rating <= 5),
    pictures varchar(255),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Create table for tasks
CREATE TABLE tasks (
    id VARCHAR(50) PRIMARY KEY DEFAULT gen_random_uuid()::VARCHAR(50),
    provider_id varchar(50) REFERENCES users(id) ON DELETE CASCADE NOT NULL,
    receiver_id varchar(50) REFERENCES users(id) ON DELETE CASCADE NOT NULL,
    service_id INT REFERENCES services(id) ON DELETE CASCADE NOT NULL,
    description Text NOT NULL,
    status VARCHAR(10) DEFAULT 'open' CHECK(status in ('open', 'closed', 'pending')),
    review_id varchar(50) REFERENCES reviews(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_review_id_status CHECK ((status != 'closed' and review_id IS NULL) or
    (status = 'closed'))
);

-- Create table for towns
CREATE TABLE towns (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

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

-- Insert sample data into users table with simulated email addresses
INSERT INTO users (id, first_name, last_name, email, password, verified)
VALUES
    (gen_random_uuid(), 'John', 'Doe', 'jd123@gmail.com', crypt('pwd1', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Jane', 'Smith', 'jane006@gmail.com', crypt('pwd1', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Luis', 'Santiago', 'bestbeast@gmail.com', crypt('pwd3', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Hector', 'Torres', 'hector.torres@gmail.com', crypt('pwd4', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Angelica', 'Diaz', 'angelicadiaz09@gmail.com', crypt('pwd5', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Erick', 'Santiago', 'ericksan_san@gmail.com', crypt('pwd6', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Maria', 'Garcia', 'maria1990@gmail.com', crypt('pwd7', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Carlos', 'Martinez', 'carlos.martinez@gmail.com', crypt('pwd8', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Sofia', 'Rodriguez', 'sofia.rodri@gmail.com', crypt('pwd9', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Daniel', 'Lopez', 'daniellopezPR@gmail.com', crypt('pwd10', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Laura', 'Hernandez', 'lauritaPR@gmail.com', crypt('pwd11', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Pedro', 'Gonzalez', 'pedro.gonzalez@gmail.com', crypt('pwd12', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Ana', 'Perez', 'ana.perez@gmail.com', crypt('pwd13', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Javier', 'Sanchez', 'javier.sanchez@gmail.com', crypt('pwd14', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Marta', 'Lopez', 'marta.lopez@gmail.com', crypt('pwd15', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Gabriel', 'Rivera', 'gabriel.rivera@gmail.com', crypt('pwd16', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Veronica', 'Gomez', 'veronica.gomez@gmail.com', crypt('pwd17', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Miguel', 'Diaz', 'miguel.diaz@gmail.com', crypt('pwd18', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Julia', 'Fernandez', 'julia.fernandez@gmail.com', crypt('pwd19', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Roberto', 'Ramirez', 'roberto.ramirez@gmail.com', crypt('pwd20', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Alice', 'Brown', 'alice.brown@outlook.com', crypt('pwd21', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'David', 'Wilson', 'david.wilson@outlook.com', crypt('pwd22', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Emma', 'Jones', 'emma.jones@outlook.com', crypt('pwd23', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'James', 'Taylor', 'james.taylor@outlook.com', crypt('pwd24', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Olivia', 'Davis', 'olivia787@outlook.com', crypt('pwd25', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Michael', 'Evans', 'michael_office@outlook.com', crypt('pwd26', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Sophia', 'Clark', 'sophia.clark@outlook.com', crypt('pwd27', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Alexander', 'Thomas', 'alexander.thomas@outlook.com', crypt('pwd28', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Ava', 'White', 'ava.white@outlook.com', crypt('pwd29', gen_salt('bf', 12)), true),
    (gen_random_uuid(), 'Matthew', 'Walker', 'matthew.walker@outlook.com', crypt('pwd30', gen_salt('bf', 12)), true);
-- Insert sample data into services table
INSERT INTO services (name)
VALUES
    ('Nails'),
    ('Gardening'),
    ('Barber'),
    ('Hairstyling'),
    ('Pet Sitting'),
    ('Car Washing'),
    ('Baking'),
    ('Plumbing'),
    ('Electrical Service'),
    ('House Cleaning'),
    ('Pet Grooming'),
    ('Landscaping'),
    ('Event Decorator'),
    ('DJ'),
    ('Catering'),
    ('Auto Body Painting'),
    ('Painter');

-- Insert sample data into towns table
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
    ('Peñuelas'),
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
INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Nightclubs and Weddings','I create a personalized timeline that reflects your taste, ensuring a smooth transition from ceremony to reception and unforgettable dance floor moments for you and your guests. I also make video recordings!'
FROM users u
JOIN services s ON s.name = 'DJ'
WHERE u.first_name = 'John' AND u.last_name = 'Doe';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Special Gardening Offer',
'Transform your garden with our expert gardening service. We offer a variety of designs tailored to your preferences.'
FROM users u
JOIN services s ON s.name = 'Gardening'
WHERE u.first_name = 'Jane' AND u.last_name = 'Smith';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Urban DJ',
'Get the latest mix trends and hits. If you are looking to get your clients invested in your business, give them the entertainment they deserve.'
FROM users u
JOIN services s ON s.name = 'DJ'
WHERE u.first_name = 'Hector' AND u.last_name = 'Torres';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'New Styles Modern',
'Latest hair trends with our professional service. Look stunning for your special day! Our stylists excel in special occasion hair styling, from elegant updos to glamorous curls,ensuring you shine at weddings, proms, and more'
FROM users u
JOIN services s ON s.name = 'Hairstyling'
WHERE u.first_name = 'Olivia' AND u.last_name = 'Davis';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Best Styles in Town', 'Discover your ideal hair style with our personalized consultations. Our stylists will assess your hair type, face shape, and lifestyle to recommend the perfect cut and style for you.'
FROM users u
JOIN services s ON s.name = 'Hairstyling'
WHERE u.first_name = 'Marta' AND u.last_name = 'Lopez';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Nail Art Extravaganza', 'Treat yourself to stunning nail art designs. Our expert nail technicians will transform your nails into works of art!'
FROM users u
JOIN services s ON s.name = 'Nails'
WHERE u.first_name = 'Maria' AND u.last_name = 'Garcia';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Spotless Cleaning Service', 'Experience the joy of a spotless home! Our cleaning experts will handle all your cleaning needs with meticulous care.'
FROM users u
JOIN services s ON s.name = 'House Cleaning'
WHERE u.first_name = 'Sofia' AND u.last_name = 'Rodriguez';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Pet Paradise Retreat', 'Your pets home away from home! We provide personalized pet sitting services to ensure your furry friends are happy and cared for.'
FROM users u
JOIN services s ON s.name = 'Pet Sitting'
WHERE u.first_name = 'Angelica' AND u.last_name = 'Diaz';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Premium Car Wash & Detailing', 'Revitalize your vehicle with our premium car wash and detailing services. We will make your car shine inside and out!'
FROM users u
JOIN services s ON s.name = 'Car Washing'
WHERE u.first_name = 'Erick' AND u.last_name = 'Santiago';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Landscaping Masterpieces', 'Transform your outdoor space into a lush paradise. Our landscaping experts specialize in creating beautiful and functional landscapes.'
FROM users u
JOIN services s ON s.name = 'Landscaping'
WHERE u.first_name = 'Gabriel' AND u.last_name = 'Rivera';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Expert Plumbing Solutions', 'Need plumbing repairs or installations? We offer reliable plumbing services tailored to your needs.'
FROM users u
JOIN services s ON s.name = 'Plumbing'
WHERE u.first_name = 'Carlos' AND u.last_name = 'Martinez';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Gourmet Catering Experience', 'Indulge in a gourmet feast prepared by our talented chefs. Our catering services will make your event unforgettable.'
FROM users u
JOIN services s ON s.name = 'Catering'
WHERE u.first_name = 'Laura' AND u.last_name = 'Hernandez';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Ultimate Party DJ', 'Set the dance floor on fire with our energetic DJ services.
We will create the perfect ambiance for your event!'
FROM users u
JOIN services s ON s.name = 'DJ'
WHERE u.first_name = 'Javier' AND u.last_name = 'Sanchez';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Professional Electrical Solutions', 'Need electrical repairs or installations? Our experts deliver safe and efficient electrical services.'
FROM users u
JOIN services s ON s.name = 'Electrical Service'
WHERE u.first_name = 'Daniel' AND u.last_name = 'Lopez';

INSERT INTO promotions (user_id, service_id, title, description)
SELECT u.id, s.id, 'Artistic Painting Services', 'Transform your space with our artistic painting services. Our painters bring creativity and precision to every project.'
FROM users u
JOIN services s ON s.name = 'Painter'
WHERE u.first_name = 'Roberto' AND u.last_name = 'Ramirez';
-- End of inserts for promos ---------------

-- Insert requests for each user and their preferred services

-- Jhon Doe
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Birthday Party DJ', 'Looking for a DJ for my upcoming birthday party.'
FROM users u
JOIN services s ON s.name = 'DJ'
WHERE u.first_name = 'John' AND u.last_name = 'Doe';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Corporate Event DJ', 'Seeking a DJ for our companys annual event.'
FROM users u
JOIN services s ON s.name = 'DJ'
WHERE u.first_name = 'John' AND u.last_name = 'Doe';

-- Jane Smith
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Backyard Garden Design', 'Want to enhance my backyard with a custom garden design.'
FROM users u
JOIN services s ON s.name = 'Gardening'
WHERE u.first_name = 'Jane' AND u.last_name = 'Smith';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Front Yard Landscaping', 'Looking for landscaping ideas for my front yard.'
FROM users u
JOIN services s ON s.name = 'Landscaping'
WHERE u.first_name = 'Jane' AND u.last_name = 'Smith';

-- Luis Santiago
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Home Deep Cleaning', 'Need thorough cleaning service for my home.'
FROM users u
JOIN services s ON s.name = 'House Cleaning'
WHERE u.first_name = 'Luis' AND u.last_name = 'Santiago';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Weekly Cleaning Service', 'Interested in regular weekly cleaning assistance.'
FROM users u
JOIN services s ON s.name = 'House Cleaning'
WHERE u.first_name = 'Luis' AND u.last_name = 'Santiago';

-- Hector Torres
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Plumbing Repair', 'Need immediate plumbing repair services.'
FROM users u
JOIN services s ON s.name = 'Plumbing'
WHERE u.first_name = 'Hector' AND u.last_name = 'Torres';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Electrical Troubleshooting', 'Experiencing electrical issues at home, need assistance.'
FROM users u
JOIN services s ON s.name = 'Electrical Service'
WHERE u.first_name = 'Hector' AND u.last_name = 'Torres';

-- Angelica Diaz
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Pet Sitting', 'Looking for a reliable pet sitter for my cat.'
FROM users u
JOIN services s ON s.name = 'Pet Sitting'
WHERE u.first_name = 'Angelica' AND u.last_name = 'Diaz';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Pet Grooming', 'Need grooming service for my dog.'
FROM users u
JOIN services s ON s.name = 'Pet Grooming'
WHERE u.first_name = 'Angelica' AND u.last_name = 'Diaz';

-- Erick Santiago
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Car Wash', 'Looking for professional car washing service.'
FROM users u
JOIN services s ON s.name = 'Car Washing'
WHERE u.first_name = 'Erick' AND u.last_name = 'Santiago';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Auto Body Painting', 'Need auto body painting for my vehicle.'
FROM users u
JOIN services s ON s.name = 'Auto Body Painting'
WHERE u.first_name = 'Erick' AND u.last_name = 'Santiago';

-- Maria Garcia
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Baking Service', 'Looking for custom cake baking service.'
FROM users u
JOIN services s ON s.name = 'Baking'
WHERE u.first_name = 'Maria' AND u.last_name = 'Garcia';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Event Catering', 'Require catering service for upcoming event.'
FROM users u
JOIN services s ON s.name = 'Catering'
WHERE u.first_name = 'Maria' AND u.last_name = 'Garcia';

-- Carlos Martinez
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Haircut and Shave', 'In need of a haircut and shave.'
FROM users u
JOIN services s ON s.name = 'Barber'
WHERE u.first_name = 'Carlos' AND u.last_name = 'Martinez';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Hairstyling for Event', 'Seeking hairstyling service for special event.'
FROM users u
JOIN services s ON s.name = 'Hairstyling'
WHERE u.first_name = 'Carlos' AND u.last_name = 'Martinez';

-- Sofia Rodriguez
INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Interior Painting', 'Looking for interior painting services.'
FROM users u
JOIN services s ON s.name = 'Painter'
WHERE u.first_name = 'Sofia' AND u.last_name = 'Rodriguez';

INSERT INTO requests (user_id, service_id, title, description)
SELECT u.id, s.id, 'Event Decoration', 'Need help with event decoration.'
FROM users u
JOIN services s ON s.name = 'Event Decorator'
WHERE u.first_name = 'Sofia' AND u.last_name = 'Rodriguez';

-- End of requests inserts ---------


-- Insert promotions into promo_towns

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('San Juan', 'Carolina', 'Bayamon', 'Santurce', 'Guaynabo')
WHERE p.title = 'Nightclubs and Weddings' AND u.first_name = 'John' AND u.last_name = 'Doe' AND s.name = 'DJ';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Ponce', 'Juana Diaz')
WHERE p.title = 'Expert Plumbing Solutions' AND u.first_name = 'Carlos' AND u.last_name = 'Martinez' AND s.name = 'Plumbing';

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
WHERE p.title = 'Special Gardening Offer' AND u.first_name = 'Jane' AND u.last_name = 'Smith' AND s.name = 'Gardening';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('San Juan', 'Carolina', 'Guaynabo', 'Santurce', 'Bayamon')
WHERE p.title = 'Urban DJ' AND u.first_name = 'Hector' AND u.last_name = 'Torres' AND s.name = 'DJ';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('San Juan', 'Carolina', 'Bayamon', 'Santurce', 'Guaynabo')
WHERE p.title = 'New Styles Modern' AND u.first_name = 'Olivia' AND u.last_name = 'Davis' AND s.name = 'Hairstyling';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Aibonito', 'Cayey', 'Guayama')
WHERE p.title = 'Best Styles in Town' AND u.first_name = 'Marta' AND u.last_name = 'Lopez' AND s.name = 'Hairstyling';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Carolina')
WHERE p.title = 'Nail Art Extravaganza' AND u.first_name = 'Maria' AND u.last_name = 'Garcia' AND s.name = 'Nails';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Fajardo')
WHERE p.title = 'Spotless Cleaning Service' AND u.first_name = 'Sofia' AND u.last_name = 'Rodriguez' AND s.name = 'House Cleaning';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Cabo Rojo', 'Hormigueros')
WHERE p.title = 'Pet Paradise Retreat' AND u.first_name = 'Angelica' AND u.last_name = 'Diaz' AND s.name = 'Pet Sitting';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Carolina', 'San Juan', 'Guaynabo', 'Bayamon', 'Santurce')
WHERE p.title = 'Premium Car Wash & Detailing' AND u.first_name = 'Erick' AND u.last_name = 'Santiago' AND s.name = 'Car Washing';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Carolina', 'Guaynabo')
WHERE p.title = 'Professional Electrical Solutions' AND u.first_name = 'Daniel' AND u.last_name = 'Lopez' AND s.name = 'Electrical Service';

INSERT INTO promo_towns (promo_id, town_id)
SELECT p.id, t.id
FROM promotions p
JOIN users u ON p.user_id = u.id
JOIN services s ON p.service_id = s.id
JOIN towns t ON t.name IN ('Santurce', 'Bayamon')
WHERE p.title = 'Artistic Painting Services' AND u.first_name = 'Roberto' AND u.last_name = 'Ramirez' AND s.name = 'Painter';

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

-- Insert into request_towns for John Doe's Corporate Event DJ request (Specify the town)
INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Bayamon'
WHERE r.title = 'Corporate Event DJ'
AND u.first_name = 'John'
AND u.last_name = 'Doe';

-- Insert Requests into Request_town for Jane Smith's requests
INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Aguadilla'
WHERE r.title = 'Backyard Garden Design'
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
WHERE r.title = 'Home Deep Cleaning'
AND u.first_name = 'Luis'
AND u.last_name = 'Santiago';

INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Aibonito'
WHERE r.title = 'Weekly Cleaning Service'
AND u.first_name = 'Luis'
AND u.last_name = 'Santiago';

-- Insert Requests into Request_town for Hector Torres's requests
INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'San German'
WHERE r.title = 'Plumbing Repair'
AND u.first_name = 'Hector'
AND u.last_name = 'Torres';

INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Rincon'
WHERE r.title = 'Electrical Troubleshooting'
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
WHERE r.title = 'Car Wash'
AND u.first_name = 'Erick'
AND u.last_name = 'Santiago';

INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Carolina'
WHERE r.title = 'Auto Body Painting'
AND u.first_name = 'Erick'
AND u.last_name = 'Santiago';

-- Insert Requests into Request_town for Maria Garcia's requests
INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Caguas'
WHERE r.title = 'Baking Service'
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
WHERE r.title = 'Haircut and Shave'
AND u.first_name = 'Carlos'
AND u.last_name = 'Martinez';

INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'San Juan'
WHERE r.title = 'Hairstyling for Event'
AND u.first_name = 'Carlos'
AND u.last_name = 'Martinez';

-- Insert Requests into Request_town for Sofia Rodriguez's requests
INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Ponce'
WHERE r.title = 'Interior Painting'
AND u.first_name = 'Sofia'
AND u.last_name = 'Rodriguez';

INSERT INTO request_towns (request_id, town_id)
SELECT r.id, t.id
FROM requests r
JOIN users u ON r.user_id = u.id
JOIN services s ON r.service_id = s.id
JOIN towns t ON t.name = 'Bayamon'
WHERE r.title = 'Event Decoration'
AND u.first_name = 'Sofia'
AND u.last_name = 'Rodriguez';


-- Output confirmation
SELECT 'Tables created and populated successfully' AS Status;
