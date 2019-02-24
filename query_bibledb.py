'''
>>> import sqlite3
>>> sqlite3
<module 'sqlite3' from '/usr/lib/python2.7/sqlite3/__init__.pyc'>
>>> db = 'bible-sqlite.db'
>>> conn = sqlite3.connect(db)
>>> c = conn.cursor()
>>> c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
<sqlite3.Cursor object at 0x7f247d9f9ce0>
>>> results = c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
>>> for row in results:
...     print(row)
... 
(u'bible_version_key',)
(u'cross_reference',)
(u'key_english',)
(u't_asv',)
(u't_bbe',)
(u't_dby',)
(u't_kjv',)
(u't_wbt',)
(u't_web',)
(u't_ylt',)
>>> mykeyword = 'now to him'
>>> cmd = "SELECT * from t_kjv where t LIKE '%{}%' ".format(mykeyword)
>>> results = c.execute(cmd)
>>> for row in results:
...     print(row)
... 
(45004004, 45, 4, 4, u'Now to him that worketh is the reward not reckoned of grace, but of debt.')
(45016025, 45, 16, 25, u'Now to him that is of power to stablish you according to my gospel, and the preaching of Jesus Christ, according to the revelation of the mystery, which was kept secret since the world began,')
'''
import sqlite3

db = 'bible-sqlite.db'
#conn = sqlite3.connect(db)
#c = conn.cursor()

def connect_db(db):
	conn = sqlite3.connect(db)#object connecting to db
	return conn

def db_cursor(connect_db(db)):
	c = connect_db(db).cursor()
	return c

myid = '01001001'
cmd = "SELECT * from t_kjv where id = '{}' ".format(myid)
results = db_cursor(conn_obj).execute(cmd)

#myid = '01001001'
#cmd = "SELECT * from t_kjv where id = '{}' ".format(myid)
#results = c.execute(cmd)
for row in results:
	print(row)

'''
cmd = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
results = c.execute(cmd)
for row in results:
	print(row)

mykeyword = 'now to him'
cmd = "SELECT * from t_kjv where t LIKE '%{}%' ".format(mykeyword)
results = c.execute(cmd)
for row in results:
	print(row)

#function to connect to database
def get_connection():
	conn = sqlite3.connect(db)
	return conn

def search_keyword(keyword):
	if (keyword == 'not found'):
		result = search_id('01001001')
	else:
		return = crs.execute("SELECT * FROM t_kjv where T LIKE '%{}%' ".format(keyword) ) 
def print_result(cmd):
	for row in results:
		print(row)
'''

