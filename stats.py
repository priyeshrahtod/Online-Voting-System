import MySQLdb as m

db = m.connect(host = "localhost", user="root", passwd="mysql98", db="election")
cur = db.cursor()

cur.execute("Create table countvotes (name varchar(50), count int)")
cur.execute("commit;")
cur.execute("Insert into countvotes(name,count) Values('Shiv Sena',0)")
cur.execute("commit;")
cur.execute("Insert into countvotes(name,count) Values('Bhartiya Janata Party',0)")
cur.execute("commit;")
cur.execute("Insert into countvotes(name,count) Values('Indian National Congress',0)")
cur.execute("commit;")
cur.execute("Insert into countvotes(name,count) Values('Maharashtra Navnirman Sena',0)")
cur.execute("commit;")
cur.execute("Insert into countvotes(name,count) Values('Nationalist Congress Party',0)")
cur.execute("commit;")
cur.execute("Insert into countvotes(name,count) Values('Bahujan Samaj Party',0)")
cur.execute("commit;")
