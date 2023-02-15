-- Script that create user and
-- grant privilege

CREATE USER IF NOT EXIST "user_0d_1"@"localhost" IDENTIFED BY "user_0d_1_pwd" ;

GRANT ALL PRIVILEGES ON *.* TO "user_0d_1"@"localhost";
