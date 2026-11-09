from db import run_query_select, run_update_query

# כמה לקוחות יש בטבלה ?
result1 = run_query_select("""SELECT COUNT(*)
                              FROM ecomm;""")
print(result1)

# מהו גיל הלקוח הממוצע ?
result2 = run_query_select("""SELECT AVG(age)
                              FROM ecomm;""")
print(result2)

# כמה לקוחות גברים יש ? וכמה נשים ?
result3 = run_query_select("""SELECT gender, COUNT(*)
                              FROM ecomm
                              GROUP BY gender;""")
print(result3)

# כמה מוצרים בממוצע רוכשים הגברים ? כמה הנשים ?
result4 = run_query_select("""SELECT gender, AVG("items purchased")
                              FROM ecomm
                              GROUP BY gender;""")
print(result4)

# כמה חברים יש בכל סוג של- membership ?
result5 = run_query_select("""SELECT DISTINCT "membership type"
                              FROM ecomm;""")
print(result5)

# כמה לקוחות גרים ב- York new ?
result6 = run_query_select("""SELECT COUNT(*)
                              FROM ecomm
                              WHERE city = 'New York';""")
print(result6)

# כמה לקוחות יש בכל עיר )בסדר יורד מהגדול לקטן( ?
result7 = run_query_select("""SELECT city, COUNT(*) as amount_of_customers
                              FROM ecomm
                              GROUP BY city
                              ORDER BY amount_of_customers DESC;""")
print(result7)

# כמה סה"כ שלמו הגברים )Spend Total ? )כמה הנשים?
result8 = run_query_select("""SELECT gender, SUM("total spend")
                              FROM ecomm
                              GROUP BY gender;""")
print(result8)

# מי הלקוח שקנה הכי הרבה מוצרים? מי הלקוח שקנה הכי פחות מוצרים?
# הלקוח שקנה הכי הרבה
result9 = run_query_select("""SELECT *
                              FROM ecomm
                              ORDER BY "items purchased" DESC
                              LIMIT 1;""")
print(result9)

# הלקוח שקנה הכי פחות
result10 = run_query_select("""SELECT *
                               FROM ecomm
                               ORDER BY "items purchased"
                               LIMIT 1;""")
print(result10)
