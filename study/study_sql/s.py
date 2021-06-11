import pymysql

db = pymysql.connect('localhost', 'root', '123456', 'python04')

cursor = db.cursor()

cursor.execute("select * from student")

data = cursor.fetchone()

print(f'Database version :{data}')

db.close()
