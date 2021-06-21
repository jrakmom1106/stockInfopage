#mysqlcon.py
import pymysql

conn = pymysql.connect(host='localhost',port=3308, user='root', password='test0000',db='STOCK_PROJECT',charset='utf8')
curs= conn.cursor()

sql =   'SELECT * FROM company_info WHERE code<100 '
curs.execute(sql)

rows = curs.fetchall()

for row in rows:
    print (type(row),row)

print('기아 가격')

sql =   'SELECT * FROM company_info WHERE code=270 '
curs.execute(sql)

rows = curs.fetchall()

for row in rows:
    print (type(row),row)

'''
#Dict 타입으로 가져오기
curs = conn.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * company_info"
curs.execute(sql)
rows = curs.fetchall()
for row in rows:
    print(row)


#insert example
sql = """
        insert into company_info(title, contents, writer, wdate)
        values(%s,%s,%s,now())
      """
curs.execute(sql,('제목임','내용임','작성자임'))
conn.commit()

#update example
sql = """
        update guestbook
        set title = '제목을 수정합니다'
        where id=1
      """
curs.execute(sql)
conn.commit()

#delete example
sql="delete from guestbook where id=%s"
curs.execute(sql,1)
conn.commit()
'''