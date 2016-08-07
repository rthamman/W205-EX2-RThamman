#!/usr/bin/python
import psycopg2
import sys
import pprint
 
def main():
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

	cursor = conn.cursor()
 
	if len(sys.argv) == 1:
		#list all words with cont in alphabetic order
		sql = 'SELECT * FROM tweetwordcount order by word asc'
		cursor.execute(sql)
		records = cursor.fetchall()
		for record in records:
    			print '(<%s> , %s)'% (record[0], record[1])
	else :
		word = sys.argv[1]
		sql = 'SELECT count FROM tweetwordcount where word=%s'
		data = [word]
		cursor.execute(sql, data)
		records = cursor.fetchone()
		print 'Total number of occurences of "%s": %d'% (word, records[0])
 
if __name__ == "__main__":
	main()
