from PyQt5.QtSql import QSqlDatabase, QSqlQuery

db = QSqlDatabase.addDatabase("QODBC")
db.setDatabaseName("Driver={Sql Server};Server=localhost;Database=School;Uid=sa;Pwd=sa")
db.open()

if db.open():
   print('Opening Successfully')
else:
    print('Did not open')
#实例化一个QSqlQuery对象，然后就行查询操作
#因为获得的结果可能不止一条记录，所以我们称之为结果集。注意这个集合中的记录是从0开始编号的）
#需要说明，当刚执行完query.exec(“select * from student”);这行代码时，query是指向结果集以外的
#我们可以利用query.next()，当第一次执行这句代码时，query便指向了结果集的第一条记录

#具体操作如下：
query = QSqlQuery()
query.exec("select * from courses" )
#判断是否有下一条记录
while query.next():
    cid = query.value(0)
    cname = query.value(1)
    hour = query.value(2)
    credit = query.value(3)
    print('id:' , cid , ' name:' , cname , ' url:' , hour,' credit:',credit)

#最常用query函数的有：
#n = 1
#query.seek(n) #：query指向结果集的第n条记录。
#query.first() #：query指向结果集的第一条记录。
#query.last() #：query指向结果集的最后一条记录。
#query.next() #：query指向下一条记录，每执行一次该函数，便指向相邻的下一条记录。
#query.previous() #：query指向上一条记录，每执行一次该函数，便指向相邻的上一条记录。
#query.record() #：获得现在指向的记录。
#query.size() #：返回查询结果中的记录数。
#query.value(n)#：获得属性的值。其中n表示你查询的第n个属性
