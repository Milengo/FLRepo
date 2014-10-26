import sqlite3
import hashlib

with sqlite3.connect("database.db") as connection:
    c = connection.cursor()
    c.execute("""DROP TABLE tms""")
    c.execute("""CREATE TABLE tms (filename TEXT, filehash TEXT)""")
    filename ='Hello World'
    filehash = hashlib.sha1(filename.encode()).hexdigest()
    print(filehash)
    t = (filename, filehash,)
    c.execute("""INSERT INTO tms VALUES(?,?)""",t )
    connection.commit()

    result = c.execute("""SELECT * FROM tms""").fetchone()
    print(result)