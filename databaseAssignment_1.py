
import sqlite3

conn = sqlite3.connect('database_1.db') #creating a database

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txt(ID INTEGER PRIMARY KEY AUTOINCREMENT, \  
                col_fExt TEXT)")  
    conn.commit()

conn = sqlite3.connect('database_1.db')


fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
#loops through all the files to find the files that have a .txt extension
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            #creates new tuple with only the .txt files
            cur.execute("INSERT INTO tbl_txt (col_fExt) VALUES (?)", (x,))
            print(x)

conn.close()            
