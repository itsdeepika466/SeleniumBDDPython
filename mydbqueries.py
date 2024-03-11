insert_query="insert into student values(106,'DEF')"
update_qyuery="update student set sname = 'Deep' where sid=105"
del_query="delete from student where sid =104"

import mysql.connector
try:
  con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
  curs=con.cursor()
  curs.execute(insert_query)
  con.commit()
  con.close()
except:
  print("connetion unsuccessful")

print("Finished")