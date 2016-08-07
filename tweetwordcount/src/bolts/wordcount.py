from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counter = Counter()

    def process(self, tup):
        word = tup.values[0]

	
	#update db only after accumulating 100 words
	if len(self.counter) > 100:
        	self.log('Updating to db %d' % ( len(self.counter)))
		for temp_word, temp_count in sorted(self.counter.iteritems()):
			conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
			cur = conn.cursor()
			sql = 'SELECT * from tweetwordcount where word = %s'
			data = [temp_word]
			cur.execute(sql, data)
			if cur.fetchone() is None:
				sql = 'INSERT into tweetwordcount (word, count) values(%s, %s)'
				data = [temp_word, 1]
				cur.execute(sql, data)
			else:
				sql = 'UPDATE tweetwordcount set count = count + %s where word=%s'
				data = [temp_count, temp_word]
				cur.execute(sql, data)
			conn.commit()
		self.counter.clear()
        	self.log('Resetting counter to %d' % ( len(self.counter)))

        # Increment the local count
        self.counter[word] += 1
        self.emit([word, self.counter[word]])

        # Log the count - just to see the topology running
        self.log('Adding to counter %s: %d' % (word, self.counter[word]))

