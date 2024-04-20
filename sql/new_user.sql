-- READ THIS IMPORTANT!!!!!!!!
-- RUN THIS SCRIPT ON YOUR ROOT/SUPER_USER
-- User: demo_dev  password: demo_dev_pwd

-- After this you can use this user's scripts
-- 'user_creates.sql': delete data and populate tables

-- Create user if not exists
DO
$$
BEGIN
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'demo_acces') THEN
    CREATE ROLE demo_acces LOGIN PASSWORD 'demo_acces_pwd';
  END IF;
END
$$;

GRANT USAGE ON SCHEMA public TO demo_acces;

GRANT ALL PRIVILEGES ON DATABASE demo_db TO demo_acces;
GRANT postgres TO demo_acces;

-- Allow visibility for user on tables
REVOKE CONNECT ON DATABASE demo_db FROM PUBLIC;

GRANT ALL
ON DATABASE demo_db
TO demo_acces;

REVOKE ALL
ON ALL TABLES IN SCHEMA public 
FROM PUBLIC;
GRANT SELECT, INSERT, UPDATE, DELETE
ON ALL TABLES IN SCHEMA public 
TO demo_acces;

CREATE USER demo_dev WITH PASSWORD 'demo_dev_pwd';
GRANT demo_acces TO demo_dev;
