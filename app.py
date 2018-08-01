from flask import Flask, render_template, request # request object in flask helps you get form body
import requests #send http requests 
from datetime import datetime 	# to get timestamp
import datetime
import sqlite3 #to use sqlite functions
#!/usr/bin/python

#from mergesort import merge_sort #has mergesort algorithm

#from test2 import get_bookname

db = 'bible-sqlite.db' #our bible database

#myarray = [] #try track all keys
bible = []
myresults=[]
key = ''
app = Flask(__name__)






@app.route('/results', methods=['GET', 'POST'])
def results():
	myarray = [] 
	searchcount=None
	#get form input	
	def validateinput():	
		error = None
		if request.method == 'POST':
			if (not(request.form['comment']).isdigit()):
				return request.form['comment']
		else:
			error = 'not found'
	comment = validateinput()

	'''if request.method == 'POST':
		#bookkey = request.form['book']
		comment = request.form['comment']
	'''
	#function to connect to database
	def get_connection():
		conn = sqlite3.connect(db)
		return conn

	#initialize db connection
	conn = get_connection()	

	#cursor to parse db
	crs = conn.cursor()	
	
	#sqlite cmds
	def get_tables():
		return crs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")

	def get_table_count():
		return crs.execute("SELECT count (*) FROM sqlite_master WHERE type='table' ;")

	#Get all tables v2
	def get_tables2():
		return crs.execute("SELECT sql FROM sqlite_master where type = 'table'")

	#Get all versions
	def get_versions():
		return crs.execute("SELECT * FROM bible_version_key")

	#Get all bible books
	def get_bible_books():
		return crs.execute("SELECT * FROM key_english")

	#get one bible book
	def get_bible_book_one(bookid):
		#return crs.execute("SELECT * FROM key_english ")
		return crs.execute('SELECT n FROM key_english WHERE b ={}'.format(bookid) );

	def get_booklist():
		for b in get_bible_books():
			booklist.append(b[1])
		return booklist

	#not sure what this does
	def get_cross_reference():
		return crs.execute("SELECT * FROM cross_reference LIMIT 50")

	#mykeyword = "In the beginning"
	#search by keyword
	def search_keyword(keyword):
		if (keyword == 'not found'):
			result = search_id('01001001')
		else:
			result = crs.execute("SELECT * FROM t_kjv where T LIKE '%{}%' ".format(keyword) ) 
		return result 

	#search by id
	def search_id(someid):
		return crs.execute("SELECT * FROM t_kjv where id = '{}' ".format(someid) )

	def print_all2(results):
		for row in results:
			print(row)
	
	#check for nulls in results and print error message	
	def print_all(results):
		for row in results:
			if(row == ''):
				print("NO RESULTS.")
			else:
				print("{} {}:{} '{}' ".format( row[1], row[2], row[3], row[4]) )

	def pop_all(arr):
		for row in arr:
			arr.pop()
		return arr

	pop_all(myarray)

	#exec sqlite3 command/query and assign to var bingo
	bingo = search_keyword(comment)

	#how to xtract results from the sqlite3 query (result assigned to bingo) Use a for each loop py style
	for rows in bingo:
		#print (rows[0]) #(rows[0])#0th item in array happens to be the text. If we just call that.
		key = 0
		key = rows[0]
		book = rows[1]
		chapter = rows[2]
		verse = rows[3]
		feed = rows[4] #text
		myarray.append(rows)#try push result to queue/array

		bible = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy','Joshua', 'Judges','Ruth','1 Samuel','2 Samuel','1 Kings','2 Kings','1 Chronicles','2 Chronicles','Ezra','Nehemiah','Esther','Job','Psalms','Proverbs','Ecclesiastes','Song of Solomon','Isaiah','Jeremiah','Lamentations','Ezekiel','Daniel','Hosea','Joel','Amos','Obadiah','Jonah','Micah', 'Nahum','Habakkuk','Zephaniah','Haggai','Zechariah','Malachi','Matthew','Mark','Luke','John','Acts','Romans','1 Corinthians','2 Corinthians','Galatians','Ephesians','Philippians','Colossians','1 Thesalonians','2 Thesalonians','1 Timothy','2 Timothy','Titus','Philemon','Hebrews','James','1 Peter','2 Peter','1 John','2 John','3 John','Jude','Revealation']
		book = bible[book-1]	#note: array index starts at zero
		searchcount= len(myarray)

	conn.close() #caller must close database connection

	#return has args that will be used on display page
	return render_template('results.html', key = key, feed=feed, book=book,verse=verse, chapter=chapter, myarray=myarray,comment=comment, bible=bible, searchcount=searchcount)


#this gets you to the entire book-chapter-verses, BCV from /results
@app.route('/results_bc', methods=['GET', 'POST'])
def results_bc():	#def results_bc(myid):
	#myid = '01001001'  #the id you'll get from results
	myid = '01001001' 
	book = 0
	
	tester = results()

	#function to connect to database
	def get_connection():
		conn = sqlite3.connect(db)
		return conn

	#initialize db connection
	conn = get_connection()	

	#cursor to parse db
	crs = conn.cursor()	

	#query
	#search by id
	bookresults = crs.execute("SELECT * FROM t_kjv where id = '{}' ".format(myid) )
	
	#bible
	bible = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy','Joshua', 'Judges','Ruth','1 Samuel','2 Samuel','1 Kings','2 Kings','1 Chronicles','2 Chronicles','Ezra','Nehemiah','Esther','Job','Psalms','Proverbs','Ecclesiastes','Song of Solomon','Isaiah','Jeremiah','Lamentations','Ezekiel','Daniel','Hosea','Joel','Amos','Obadiah','Jonah','Micah', 'Nahum','Habakkuk','Zephaniah','Haggai','Zechariah','Malachi','Matthew','Mark','Luke','John','Acts','Romans','1 Corinthians','2 Corinthians','Galatians','Ephesians','Philippians','Colossians','1 Thesalonians','2 Thesalonians','1 Timothy','2 Timothy','Titus','Philemon','Hebrews','James','1 Peter','2 Peter','1 John','2 John','3 John','Jude','Revealation']
	book = bible[book-1]	#note: array index starts at zero
		
	#return has args that will be used on display page
	return render_template('results_bc.html', nr = bookresults, bible=bible, tester=tester)





#this is the index page route and is the root hence the '/'
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
