#!/usr/bin/python
import psycopg2
import sys
import pprint
 
def main():
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

	cursor = conn.cursor()
 
	if len(sys.argv) < 2:
		print 'Incorrect usage. Please use "python histogram.py k1,k2"'
		return
	args = sys.argv[1].strip().split(",")
	k1 = int(args[0])
	k2 = int(args[1])

	sql = 'SELECT * FROM tweetwordcount where count between %s and %s order by count asc'
	data= [k1, k2]
	cursor.execute(sql, data)
	records = cursor.fetchall()
	for record in records:
    		print '(<%s> , %s)'% (record[0], record[1])
 
if __name__ == "__main__":
	main()
