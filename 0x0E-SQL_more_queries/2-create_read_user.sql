-- creating a user that only SELECT
CREATE IF NOT EXISTS DATABASE hbtn_0d_2;
CREATE IF NOT EXISTS USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
ALTER USER 'user_0d_2'@'localhost' IDENTIFIED BY 'uesr_0d_2_pwd';
FLUSH PRIVILEGES;
GRANT ONLY SELECT ON 'htbn_0d_2' 
