-- כמה לקוחות יש בטבלה ?
SELECT COUNT(*)
FROM ecomm;

-- מהו גיל הלקוח הממוצע ?
SELECT AVG(age)
FROM ecomm;

-- כמה לקוחות גברים יש ? וכמה נשים ?
SELECT gender, COUNT(*)
FROM ecomm
GROUP BY gender;

-- כמה מוצרים בממוצע רוכשים הגברים ? כמה הנשים ?
SELECT gender, AVG("items purchased")
FROM ecomm
GROUP BY gender;

-- כמה חברים יש בכל סוג של- membership ?
SELECT DISTINCT "membership type"
FROM ecomm;

-- כמה לקוחות גרים ב- York new ?
SELECT COUNT(*)
FROM ecomm
WHERE city = 'New York';

-- כמה לקוחות יש בכל עיר )בסדר יורד מהגדול לקטן( ?
SELECT city, COUNT(*) as amount_of_customers
FROM ecomm
GROUP BY city
ORDER BY amount_of_customers DESC;

-- כמה סה"כ שלמו הגברים )Spend Total ? )כמה הנשים?
SELECT gender, SUM("total spend")
FROM ecomm
GROUP BY gender;

-- מי הלקוח שקנה הכי הרבה מוצרים? מי הלקוח שקנה הכי פחות מוצרים?
-- הלקוח שקנה הכי הרבה
SELECT *
FROM ecomm
ORDER BY "items purchased" DESC
LIMIT 1;
-- הלקוח שקנה הכי פחות
SELECT *
FROM ecomm
ORDER BY "items purchased"
LIMIT 1;