def main ():
	# readin the probe.txt file to standard in
	def netflix_read (r):
		s = r.readline()
		# read the movie id which has a ':'
		if s.find(':'):
			a = s.remove(':')
			return int(a)
# read the lines below as customer ids up unitl a new movie id appears
# create a dictionairy where the movie id = key and customer ids = values

	def netflix_predict():
	# read the key (movie title) from the dictionairy created 
	# go through savant-cachemovies.txt and find average movie rating 
	# read  the associated values (customer ids) for the movie and find their average rating
	# for each value, predict a weighted guess (using average customer rating and movie rating)

	#read movie title -> find the average rating for that movie through the cache
	#read customer id and find corresponding avg customer id rating through cache
	# predict a rating based on the above 2 averages. Try using different weights 
	def netflix_calc():

	#run the predictiion against the real value using RMSE.py

	def netflix_write():
		#output movie id followed by predicted ratings instead of customer ids
		#ouptut file to netflix.out
