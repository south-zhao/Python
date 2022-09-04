import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='db')


cursor = db.cursor()

sql = "select * from grade where math > 80"

cursor.execute(sql)

results = cursor.fetchall()

for i in results:
    print(i)
    print(type(i))

# 执行sql语句
db.commit()

# 关闭数据库连接
db.close()



























