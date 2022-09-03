import pymysql

coala_db = pymysql.connect(host='hagalsa.cafe24.com', # write the ip address of the server
                           user='hagalsa', # write the username of the db you are trying to connect with
                           password='son2020^^', # write the password of that user
                           db='hagalsa', # write the db name which you are trying to access to
                           charset='utf8') # the characterset of the db
# connecting to the server




cursor = coala_db.cursor(pymysql.cursors.DictCursor) 
# defining the cursor functiom

sql = "insert into test (name, age) values (%s, %s)" 
# inserting selected files into the list 'test'

cursor.execute(sql, ('hello', '1234')) 
# executing the insert function 




coala_db.commit() # saving the changes




sql = "select name, age from test where name=(%s)" 
# extracting the wanted information

cursor.execute(sql,('hello')) 
# executing the code with the data tag hello for the name

student_info = cursor.fetchall() 
# inputing the data fetched by the cursor into a variable 'student_info'

print(student_info) 
# printing the inputed data from 'student_info'




delay(1000)




sql = "delete from test where name=(%s)" 
# making a function for deleting the inserted data

cursor.execute =(sql,('hello')) 
# executing the function




sql = "select name, age from test where name=(%s)" 
# extracting the wanted information

cursor.execute(sql,('hello')) 
# executing the code with the data tag hello for the name

student_info = cursor.fetchall() 
# inputing the data fetched by the cursor into a variable 'student_info'

print(student_info) 
# printing the inputed data from 'student_info' whether to check the deletion was successful
