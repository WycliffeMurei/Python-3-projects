import sqlite3
connection = sqlite3.connect('kibet.db')

line = ("INSERT INTO people VALUES("wycliffe","kibet",24)"))
connection.execute(line)

connection.execute("DROP TABLE IF EXIST people")

connection.commit()
connection.close()

#FirstName = str("Enter your Name")
#LastName = str("Enter your last name")
#Age = (("Enter your age"))
#with sqlite3.connect("test_database") as connection :
    #c = connection.cursor()
   # line = "INSERT INTO people Values('" + FirstName  + '",' "" + LastName +'" ,' "" + Age +")"
   # c.execute(line)
   # c.close())



