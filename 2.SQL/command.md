This is the personal summary note about SQL. I've list all the reference, many of the cases are from w3scool. If this is not suitable, and I will set it as private.


### 1. UPDATE and DELETE
```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition; 
```
```
DELETE FROM table_name WHERE condition;
```
The WHERE clause specifies which record(s) that should be updated/delete.       
If omit the WHERE clause, all records in the table will be updated/delete.     
``` mysql
DELETE p1 FROM Person AS p1,
    Person AS p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id 
```

### 2 LIMIT() / ROWNUM
specify the number of records to return.   
```
SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;
```
lc 176 there is the case that only one column and not second salary
```
# Write your MySQL query statement below
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
```
the offset specifies the offset of the first row to return. The offset of the first row is 0, not 1.
```
SELECT * FROM Customers
WHERE ROWNUM <= 3;
```

### 3. MAX/MIN
```
SELECT MIN(column_name)
FROM table_name
WHERE condition; 
```


### 4. COUNT/SUM/AVG
```
SELECT COUNT(ProductID)
FROM Products;
```

### 5. LIKE
The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.   
```
SELECT * FROM Customers
WHERE CustomerName LIKE '%or%';
```

### 6. IN BETWEEN
```
SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');
```
```
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;
```

### 7. change the name of the row
```
SELECT CustomerID AS ID, CustomerName AS Customer
FROM Customers;
```

### 8. JOIN

    - (INNER) JOIN: Returns records that have matching values in both tables
    - LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
    - RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
    - FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table
lc 175
```
SELECT Person.FirstName, Person.LastName, Address.city, Address.state
FROM Person
LEFT JOIN Address ON Person.PersonId = Address.PersonId;
```
lc 181. Employees Earning More Than Their Managers
``` mysql
# Write your MySQL query statement below
SELECT a.Name AS Employee
FROM Employee AS a
JOIN Employee AS b
WHERE a.ManagerId = b.Id and a.Salary > b.Salary
```


### 9. Self JOIN
```
SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID
AND A.City = B.City
ORDER BY A.City;
```

### 10. UNION
```
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;
```

### 10 GROUP BY/ HAVING
The GROUP BY statement groups rows that have the same values into summary rowsk
```
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s); 

```
The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions.
SUM AVG COUNT are aggregate functions.
```
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
```

lc182
```
# Write your MySQL query statement below
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) >1;
```

### 11. EXISTS
test for the existence of any record in a subquery.
```
SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20); 
```

### 12. ANY and ALL 
The ANY and ALL operators are used with a WHERE or HAVING clause.

```
SELECT column_name(s)
FROM table_name
WHERE column_name operator ANY
(SELECT column_name FROM table_name WHERE condition); 

```

### 13. SELECT  SELECT INTO 
The SELECT INTO statement copies data from one table into a new table.
```
SELECT CustomerName, ContactName INTO CustomersBackup2017
FROM Customers; 
```
```
SELECT * FROM table_name;
```

```
# Write your MySQL query statement below
SELECT Name AS  Customers 
FROM Customers
WHERE Customers.Id not in (
 SELECT Orders.CustomerId from Orders    
)
```
### 14. INSERT INTO 
```
INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition; 
```

### 15.CASE 
CASE statement goes through conditions
and returns a value when the first condition is met (like an IF-THEN-ELSE statement). 
```
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END; 
```

### 16. Others
IFNULL(), ISNULL(), COALESCE(), and NVL() Functions    
WHERE column_name IS NULL;     
AND, OR and NOT    

### 17. store a prepared SQL code
```
CREATE PROCEDURE SelectAllCustomers
AS
SELECT * FROM Customers
GO;
```
when need to execute:
```
EXEC SelectAllCustomers;
```

### 18 how to add comment?

-- comment

```SQL
--Select all:
SELECT * FROM table_name;
```
## Reference
1. https://www.w3schools.com/sql/default.asp    
2. https://www.mysqltutorial.org/mysql-limit.aspx   

