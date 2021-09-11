import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="dbociat",
  password="password",
  database="mydatabase"
)
# The database field is added after creating the database

mycursor = mydb.cursor()

# Commented the below program because after the first use it returns an error as the db already exists
"""
Create-database


mycursor.execute("CREATE DATABASE mydatabase")
"""



"""
Create-Table


mycursor.execute("CREATE TABLE students (name VARCHAR(255), country VARCHAR(255))")
"""

"""
ADD Primary key


mycursor.execute("ALTER TABLE students ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
"""

"""
Insert Data

sql = "INSERT INTO students (name, country) VALUES (%s, %s)"
val = [
  ('Daniel', 'Romania'),
  ('Alex', 'Finland'),
  ('Jeff', 'USA')
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
"""

"""
Select Data
"""

mycursor.execute("SELECT * FROM students")

myresult = mycursor.fetchall()

for record in myresult:
  print(record)


