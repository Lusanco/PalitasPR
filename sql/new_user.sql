-- READ THIS IMPORTANT!!!!!!!!
-- RUN THIS SCRIPT ON YOUR ROOT/SUPER_USER

-- After this you can use this user's scripts
-- 'user_creates.sql': delete data and populate tables

-- Create user if not exists
DO
$$
BEGIN
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'demo_dev') THEN
    CREATE ROLE demo_dev LOGIN PASSWORD 'demo_dev_pwd';
  END IF;
END
$$;

GRANT USAGE ON SCHEMA public TO demo_dev;

GRANT ALL PRIVILEGES ON DATABASE demo_db TO demo_dev;

-- Alternatively (if 'demo_dev' belongs to a specific role)
-- GRANT role_name TO pepe;  -- Replace 'role_name' with the actual role


-- Allow visibility for user on tables
REVOKE CONNECT ON DATABASE demo_db FROM PUBLIC;

GRANT CONNECT
ON DATABASE demo_db
TO demo_dev;

REVOKE ALL
ON ALL TABLES IN SCHEMA public 
FROM PUBLIC;
GRANT SELECT, INSERT, UPDATE, DELETE
ON ALL TABLES IN SCHEMA public 
TO demo_dev;

CREATE USER alfre WITH PASSWORD 'alfre_pwd';
GRANT demo_dev TO alfre;
