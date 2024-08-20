# Python program to connect
# to mysql database


import mysql.connector


# Connecting from the server
conn = mysql.connector.connect(user = 'kibet',
                               password ='kibet',
							host = 'localhost',
							database = 'shine')

print(conn)

# Disconnecting from the server
conn.close()
