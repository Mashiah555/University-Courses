# תרגיל 3 - בסיסי נתונים
**שם:** יובל משיח  
**ת.ז:** 329245161  

### 1. מספר הרישוי של הרכב(ים) שעבר את מספר השירותים הגבוה ביותר
```sql
SELECT licensenumber
FROM Treatment
GROUP BY licensenumber
HAVING COUNT(treatmentid) >= ALL (
    SELECT COUNT(treatmentid)
    FROM Treatment
    GROUP BY licensenumber
);
```

### 2. מספרי הרישוי של כל הרכבים שלא עברו אף שירות
```sql
SELECT licensenumber 
FROM Vehicle 
WHERE licensenumber NOT IN (SELECT licensenumber FROM Treatment);
```

### 3. ת.ז. הלקוח ושם הלקוח של כל לקוח עסקי אשר אף אחד מהרכבים שבבעלותו לא עבר שירות
```sql
SELECT C.clientid, C.name 
FROM Client C 
JOIN EnterpriseClient EC ON C.clientid = EC.clientid 
WHERE C.clientid NOT IN (
    SELECT V.clientid 
    FROM Vehicle V 
    JOIN Treatment T ON V.licensenumber = T.licensenumber
);
```

### 4. ת.ז. העובד ושם העובד של העובד שקיבל את הבונוס הגבוה ביותר
```sql
SELECT E.employeeid, E.name 
FROM Employee E 
JOIN Bonus B ON E.employeeid = B.employeeid
WHERE B.amount >= ALL (SELECT amount FROM Bonus);
```

### 5. מספרי הרישוי של רכבים שעברו בדיוק שני שירותים
```sql
SELECT licensenumber 
FROM Treatment 
GROUP BY licensenumber 
HAVING COUNT(treatmentid) = 2;
```

### 6. תאריכים שבהם לא בוצע אף שירות
```sql
SELECT date 
FROM Invoice 
WHERE date NOT IN (SELECT date FROM Treatment);
```

### 7. מבין העובדים שטיפלו ברכבים של לקוח העונה לשם, "זליג", הצג את מספר העובד ושם העובד של העובד שהבונוס שקיבל הוא הנמוך ביותר
```sql
SELECT E.employeeid, E.name
FROM Employee E
JOIN Bonus B ON E.employeeid = B.employeeid
WHERE E.employeeid IN (
    SELECT P.employeeid 
    FROM Participate P
    JOIN Treatment T ON P.treatmentid = T.treatmentid
    JOIN Vehicle V ON T.licensenumber = V.licensenumber
    JOIN Client C ON V.clientid = C.clientid
    WHERE C.name = 'זליג'
)
ORDER BY B.amount ASC
LIMIT 1;
```

### 8. ת.ז. הלקוח ושם הלקוח של לקוחות פרטיים המתגוררים בירושלים
```sql
SELECT C.clientid, C.name 
FROM Client C 
JOIN PrivateClient PC ON C.clientid = PC.clientid
WHERE C.address = 'ירושלים';
```

### 9. ת.ז. הלקוח ושם הלקוח של לקוחות שיש להם יותר ממספר טלפון אחד
```sql
SELECT C.clientid, C.name 
FROM Client C
JOIN ClientPhones CP ON C.clientid = CP.clientid
GROUP BY C.clientid, C.name
HAVING COUNT(CP.phone) > 1;
```

### 10. זוגות של לקוחות החולקים את אותו איש קשר
```sql
SELECT C1.clientid AS client_A_id, C1.name AS client_A_name, 
       C2.clientid AS client_B_id, C2.name AS client_B_name
FROM EnterpriseClient EC1
JOIN Client C1 ON EC1.clientid = C1.clientid
JOIN EnterpriseClient EC2 ON EC1.contactname = EC2.contactname 
                          AND EC1.clientid < EC2.clientid
JOIN Client C2 ON EC2.clientid = C2.clientid;
```

### 11. עדכון מחיר שירות בהתאם למחירי החלקים ששימשו בו (אין פלט)
```sql
UPDATE Treatment 
SET cost = (
    SELECT SUM(S.price * PU.quantity) 
    FROM PartUsed PU 
    JOIN Spare S ON PU.partid = S.partid 
    WHERE PU.treatmentid = Treatment.treatmentid
);
```

### 12. מחיקת חלקים שלא נעשה בהם שימוש בשום שירות (אין פלט)
```sql
DELETE FROM Spare 
WHERE partid NOT IN (SELECT partid FROM PartUsed);
```

### 13. מספרי השירות שבהם נעשה שימוש בחלק מסוג "Brake Pads"
```sql
SELECT PU.treatmentid 
FROM PartUsed PU
JOIN Spare S ON PU.partid = S.partid
WHERE S.name = 'Brake Pads';
```

### 14. עבור כל שירות, הצג: מספר שירות, ת.ז עובד, שם עובד, קוד חלק ותיאור חלק
```sql
SELECT T.treatmentid, E.employeeid, E.name AS employee_name, S.partid, S.name AS part_name
FROM Treatment T
JOIN Participate P ON T.treatmentid = P.treatmentid
JOIN Employee E ON P.employeeid = E.employeeid
JOIN PartUsed PU ON T.treatmentid = PU.treatmentid
JOIN Spare S ON PU.partid = S.partid;
```

### 15. ת.ז. העובד ושם העובד של עובדים שקיבלו בונוס עבור שירות שמחירו מעל 2000 ש"ח
```sql
SELECT DISTINCT E.employeeid, E.name 
FROM Employee E
JOIN Bonus B ON E.employeeid = B.employeeid
JOIN Treatment T ON B.treatmentid = T.treatmentid
WHERE T.cost > 2000;
```

### 16. הצג עבור לקוחות עסקיים את ת.ז. הלקוח, ושם הלקוח
```sql
SELECT C.clientid, C.name 
FROM Client C 
JOIN EnterpriseClient EC ON C.clientid = EC.clientid;
```

### 17. ת.ז. הלקוח ושם הלקוח של הלקוח שביצע את מספר השירותים הגבוה ביותר
```sql
SELECT C.clientid, C.name 
FROM Client C
JOIN Vehicle V ON C.clientid = V.clientid
JOIN Treatment T ON V.licensenumber = T.licensenumber
GROUP BY C.clientid, C.name
HAVING COUNT(T.treatmentid) >= ALL (
    SELECT COUNT(T2.treatmentid) 
    FROM Vehicle V2 
    JOIN Treatment T2 ON V2.licensenumber = T2.licensenumber 
    GROUP BY V2.clientid
);
```

### 18. עבור כל יצרן רכב, הצג את ת.ז. הלקוחות ושמות הלקוחות המחזיקים ברכב מאותו יצרן
```sql
SELECT V.manufacturer, C.clientid, C.name 
FROM Vehicle V
JOIN Client C ON V.clientid = C.clientid
ORDER BY V.manufacturer;
```

### 19. מספרי השירות שבהם השתתפו יותר משני עובדים
```sql
SELECT treatmentid 
FROM Participate 
GROUP BY treatmentid 
HAVING COUNT(employeeid) > 2;
```

### 20. עבור כל לקוח, הצג את מספר הלקוח, שם הלקוח והחשבונית בעלת הסכום הגבוה ביותר ששילם
```sql
SELECT C.clientid, C.name, MAX(I.totalcost) AS max_invoice_amount
FROM Client C
JOIN Vehicle V ON C.clientid = V.clientid
JOIN Treatment T ON V.licensenumber = T.licensenumber
JOIN Invoice I ON T.treatmentid = I.treatmentid
GROUP BY C.clientid, C.name;
```

### 21. מספר פריט שהוחלף בכל הרכבים שטופלו בתאריך 1.1.2025
```sql
SELECT S.partid 
FROM Spare S
WHERE NOT EXISTS (
    SELECT T.treatmentid 
    FROM Treatment T 
    WHERE T.date = '2025-01-01' 
      AND NOT EXISTS (
          SELECT * 
          FROM PartUsed PU 
          WHERE PU.partid = S.partid 
            AND PU.treatmentid = T.treatmentid
      )
);
```

### 22. תעודת הזהות ושם העובד שטיפל בכל רכבי הלקוח X
```sql
SELECT E.employeeid, E.name 
FROM Employee E
WHERE NOT EXISTS (
    SELECT V.licensenumber 
    FROM Vehicle V 
    WHERE V.clientid = 'X' 
      AND NOT EXISTS (
          SELECT * 
          FROM Treatment T 
          JOIN Participate P ON T.treatmentid = P.treatmentid 
          WHERE P.employeeid = E.employeeid 
            AND T.licensenumber = V.licensenumber
      )
);
```

### 23. תעודת הזהות ושם העובד שטיפל בכל רכבי אחד הלקוחות
```sql
SELECT E.employeeid, E.name 
FROM Employee E
WHERE EXISTS (
    SELECT C.clientid 
    FROM Client C
    WHERE NOT EXISTS (
        SELECT V.licensenumber 
        FROM Vehicle V 
        WHERE V.clientid = C.clientid 
          AND NOT EXISTS (
              SELECT * 
              FROM Treatment T 
              JOIN Participate P ON T.treatmentid = P.treatmentid 
              WHERE P.employeeid = E.employeeid 
                AND T.licensenumber = V.licensenumber
          )
    )
);
```