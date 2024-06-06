-- Adds MySQL Replica user that manages database replication

CREATE USER 'replica_mysql'@'100.24.235.14' IDENTIFIED WITH mysql_native_password BY 'replica1234';

GRANT REPLICATION SLAVE ON *.* TO 'replica_mysql'@'100.24.235.14';

FLUSH PRIVILEGES;
