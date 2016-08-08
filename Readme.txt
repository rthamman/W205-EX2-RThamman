Intstructions for executing Exercise 2 code. 

Note - 
	I got the application to work using the old AMI. There are a few limitations, such as having a number in file name is not allowed. 

	Also, these steps assumes necessary software components are installed as outlined in Arcitecture.pdf document, section File Dependencies.


1. Checkout/pull down the files from Github. Let's call the directory where the checkout resides as the ex2_root_directory. Note, a pull request has been shared.

2. Database configuration:

	a. login to postgre database using command 'psql -U postgres'

	b. Run database scripts in file '{ex2_root_directory}/db_scripts/db_scripts.sql' to create tcount 	database and tweetwrodcount table


3. Change database connection parameters. Edit the following files to change the database connection settings.
	a.  {ex2_root_directory}/tweetwordcount/src/bolts/wordcount.py


4. Change twitter credentials, if needed. The code will work with the existing credentials in the source files. File to change is {ex2_root_directory}/tweetwordcount/src/spouts/tweets.py


5. Change directory to tweetwordcount and run command 'sparse run' - this will execute the Excercise code to capture twitter feed, parse and store in the database.

6. Terminate the program for sufficient amount of time

7. For running serving scripts, use the following commands.
	a. change directory to {ex2_root_directory}/serving_scripts/
	b. run command 'python finalresults.py {word}'. For example, python finalresults.py the
	c. run command 'python histogram.py {#},{#}. For example, python histogram.py 10,100



