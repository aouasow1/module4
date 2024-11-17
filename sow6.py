#16.8 Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 16.4.
import sqlalchemy
conn = sqlalchemy.create_engine('sqlite:///books.db')
sql = 'select title from book order by title asc'
rows = conn.execute(sql)
for row in rows:
    print(row)
