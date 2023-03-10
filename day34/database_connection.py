import pymysql
db=pymysql.connect(host="localhost",user="root",passwd="SA@bah1999",db="db1")
curs1=db.cursor()
#this below query for table creation
#sql="create table person(id int,name varchar(20))"     #this query for table creation
#this below query for value insertion
sql="""insert into person values                        
(1,'sabah'),
(2,'sulaim'),
(3,'safwan'),
(4,'nadeem')"""
#this below query for table selection
sql="select*from person"
curs1.execute(sql)                                          #for execution of this sql query
rows=curs1.fetchall()                                      #fetchall() is used to fetch entire record in the table
#rows=curs1.fetchone()                                       #fetchone() is used for fetch first record in the table
# print("ID NAME")
# if rows:
#     print(rows[0],rows[1])

for i in rows:
   print(i[0],i[1])
db.commit()
db.close()
