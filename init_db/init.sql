CREATE USER postgres_admin_user WITH PASSWORD 'admin_password';
CREATE USER postgres_user WITH PASSWORD 'postgres_password';

CREATE DATABASE postgres_db;

GRANT ALL PRIVILEGES ON DATABASE postgres_db TO postgres_admin_user;
GRANT CONNECT ON DATABASE postgres_db TO postgres_user;

\c postgres_db;

GRANT SELECT ON ALL TABLES IN SCHEMA public TO postgres_user;
GRANT INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO postgres_admin_user;