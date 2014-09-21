import pickle
	# readin the probe.txt file to standard in
def netflix_read (r):
	index = 0
	s = r.readlines()
	numlines = len(s)
	netflix_dict = {}
	movid = 0

	while index < numlines:	# read the movie id which has a ':'
	
		if ':' in s[index]:
			movid = int(s[index].replace(':','').rstrip())
			index += 1
			custid = []	
		custid.append(s[index].rstrip()) # read the lines below as customer ids up unitl a new movie id appears	
		netflix_dict[movid] = custid # create a dictionairy where the movie id = key and customer ids = values
		index += 1

	return (netflix_dict)

		
	
def netflix_predict():

	with open('/u/prat0318/netflix-tests/savant-cacheMovies.txt','r') as f: #This accesses the average movie rating file created by savant
		j = f.readlines()
	avgmovie_dict = {}
	for i in j:
		j1 = i.split()
		avgmovie_dict[int(j1[0])] = float(j1[1]) #populate a dictionairy with movie id and average rating 		



	f = open('/u/prat0318/netflix-tests/ctd446-userAverageRating.txt')
	r = f.read()
	tmp = r.split(',')
	tmp[0] = tmp[0].replace('{', '')
	tmp[-1] = tmp[1].replace('}', '')
	avguser_dict = {}
	for i in tmp:
		tmp2 = i.split(':')
		tmp2[0] = tmp2[0].replace('"', '')
		tmp2[1] = tmp2[1].replace('"', '')
		custID = int(tmp2[0].replace(' ', ''))
		rating = float(tmp2[1].replace(' ', ''))
		avguser_dict[custID] = rating

	# with open('/u/prat0318/netflix-tests/savant-cacheUsers.txt','r') as f: # This accesses the average user rating file created by savant
	# 	k = f.readlines()

	# avguser_dict = {}
	# for m in k:
	# 	k1 = m.split()
	# 	k11 = k1[0].strip('\x00') #This was added to remove the trailing characters at the end of the text file
	# 	k12 = k1[1].strip('\x00')
	# 	avguser_dict[int(k11)] = float(k12) # Populated dictionairy with customer id and average customer rating



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
