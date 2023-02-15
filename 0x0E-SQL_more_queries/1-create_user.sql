-- Script that create user and
-- grant privilege

CREATE USER IF NOT EXISTS "user_0d_1"@"localhost" IDENTIFED BY "user_0d_1_pwd" ;

-- Privileges 

GRANT ALL PRIVILEGES ON *.* TO "user_0d_1"@"localhost";
FLUSH PRIVILEGES;
