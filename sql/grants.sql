-- Grant ownership of demo_db to demo_dev
ALTER DATABASE demo_db OWNER TO demo_dev;

-- Grant specific privileges on tables
GRANT SELECT ON TABLE users TO demo_dev;
GRANT INSERT, UPDATE, DELETE ON TABLE tasks TO demo_dev;
GRANT SELECT ON TABLE user_service_assoc TO demo_dev;
GRANT INSERT, UPDATE, DELETE ON TABLE user_service_assoc TO demo_dev;
GRANT SELECT ON TABLE reviews TO demo_dev;
GRANT INSERT, UPDATE, DELETE ON TABLE reviews TO demo_dev;
GRANT SELECT ON TABLE services TO demo_dev;
GRANT INSERT, UPDATE, DELETE ON TABLE services TO demo_dev;
GRANT SELECT ON TABLE towns TO demo_dev;
GRANT INSERT, UPDATE, DELETE ON TABLE towns TO demo_dev;
GRANT SELECT ON TABLE tasks TO demo_dev;
GRANT INSERT, UPDATE, DELETE ON TABLE tasks TO demo_dev;
