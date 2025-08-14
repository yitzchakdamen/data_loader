mysql --user=user --password sql
password


CREATE TABLE data  (ID  INT NOT NULL , first_name VARCHAR(120) NOT NULL, last_name VARCHAR(120), PRIMARY KEY (ID));

INSERT INTO data (ID ,first_name ,last_name) VALUES(001, "Yitzchak", "Damen");
INSERT INTO data (ID ,first_name ,last_name) VALUES(002, "Rivky", "Damen");
INSERT INTO data (ID ,first_name ,last_name) VALUES(003, "Chaim", "Shlezinger");
INSERT INTO data (ID ,first_name ,last_name) VALUES(004, "idan", "shani");

SELECT * FROM data;
