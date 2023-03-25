CREATE USER 'seantywork'@'%' IDENTIFIED BY 'youdonthavetoknow';

GRANT ALL PRIVILEGES ON *.* TO 'seantywork'@'%';

CREATE DATABASE test;

USE test;

CREATE TABLE counter (user VARCHAR(255), count INT);

INSERT INTO counter(user, count) values('youdonthavetoknow',0);

CREATE TABLE words_alpha (IDX INT, WORD VARCHAR(255));


LOAD DATA INFILE '/var/lib/mysql-files/words_alpha.csv'
INTO TABLE words_alpha
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

COMMIT;

