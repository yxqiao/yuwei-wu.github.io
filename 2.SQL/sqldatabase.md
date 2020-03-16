### 1. create/drop/backup database
``` mysql
CREATE DATABASE testDB;
DROP DATABASE testDB;
```
create a full back up of an existing SQL database.
``` mysql
BACKUP DATABASE testDB
TO DISK = 'D:\backups\testDB.bak';
```
### 2. alter/drop/create table 
``` mysql
CREATE TABLE TestTable AS
SELECT customername, contactname
FROM customers;
```
TRUNCATE TABLE statement is used to delete the data inside a table, but not the table itself.
``` mysql
DROP TABLE table_name;
TRUNCATE TABLE table_name;
```
``` mysql
ALTER TABLE Customers
ADD Email varchar(255);


ALTER TABLE table_name
DROP COLUMN column_name;
```

### 3. Constraints
``` mysql
CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    ID int NOT NULL UNIQUE,
    LastName varchar(255) NOT NULL,
    PRIMARY KEY (ID)
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
    Age int,
    CHECK (Age>=18)
    City varchar(255) DEFAULT 'Sandnes'
    ....
);

ALTER TABLE Persons
MODIFY Age int NOT NULL;


ALTER TABLE table_name
DROP INDEX index_name;
Personid int NOT NULL AUTO_INCREMENT,

```

```
NOT NULL - Ensures that a column cannot have a NULL value
UNIQUE - Ensures that all values in a column are different
PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
FOREIGN KEY - Uniquely identifies a row/record in another table
CHECK - Ensures that all values in a column satisfies a specific condition
DEFAULT - Sets a default value for a column when no value is specified
INDEX - Used to create and retrieve data from the database very quickly
```

### 4 Date
``` mysql
MySQL comes with the following data types for storing a date or a date/time value in the database:

DATE - format YYYY-MM-DD
DATETIME - format: YYYY-MM-DD HH:MI:SS
TIMESTAMP - format: YYYY-MM-DD HH:MI:SS
YEAR - format YYYY or YY

SELECT * FROM Orders WHERE OrderDate='2008-11-11'
```

Reference:
https://www.w3schools.com/sql/sql_create_db.asp
