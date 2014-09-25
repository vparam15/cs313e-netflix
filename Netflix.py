import math
netflix_dict = {}
avgmovie_dict = {}
avguser_dict = {}
predict_dict = {}
def rmse(a,p):
	assert (len(a) == len(p))
	sum1 = 0
	for i in range(len(a)):
		sum1 += (a[i] - p[i])**2
	mean = sum1/len(a)
	r = math.sqrt(mean)
	return (r)

def netflix_read (r1):
	r = open(r1,'r')	# readin the probe.txt file to standard in
	index = 0
	s = r.readlines()
	numlines = len(s)
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



def netflix_moviecache(r2):
	with open(r2,'r') as f: #This accesses the average movie rating file created by savant
		j = eval(f.read())
	for i in j.keys():
		avgmovie_dict[int(i)] = float(j[i]) #populate a dictionairy with movie id and average rating 		
	return (avgmovie_dict)

def netflix_usercache(r3):	
	f = open(r3,'r')
	r = eval(f.read())
	for u in r.keys():
		avguser_dict[int(u)] = float(r[u])
	return (avguser_dict)

def netflix_panswers(r4):
	with open(r4,'r') as f: #This accesses the average movie rating file created by savant
		j = f.readlines()

	for q in j:
		q1 = q.split()
		movID, cusID, rat = int(q1[0]),int(q1[1]),int(q1[2])
		if (movID in predict_dict.keys()):
			predict_dict[movID][cusID] = rat
		else:
			predict_dict[movID] = {cusID : rat}
	return (predict_dict)

def main():
	netflix_read('/u/downing/cs/netflix/probe.txt')
	netflix_moviecache('/u/prat0318/netflix-tests/savant-cacheMovies.txt')
	netflix_usercache('/u/prat0318/netflix-tests/savant-cacheUsers.txt')
	netflix_panswers('/u/prat0318/netflix-tests/cct667-ProbeCacheAnswers.txt')
	
	m = 0
	c = 0
	w1 = 0.5
	a = []
	p = []


	for x in netflix_dict.keys():
		try:
			m = avgmovie_dict[int(x)]
		except KeyError:
			m = 3.7
		for y in netflix_dict[x]:
			try:
				c = avguser_dict[int(y)]
			except KeyError:
				c = 3.7
			prediction = 3.7 + w1*(m-3.7) + (1-w1)*(c-3.7)	
			a.append(prediction) 
		for x1 in (predict_dict[x].keys()):
			p.append(predict_dict[x][x1])
	print (rmse(a,p))

main()	

	# with open('/u/prat0318/netflix-tests/savant-cacheUsers.txt','r') as f: # This accesses the average user rating file created by savant
	# 	k = f.readlines()+

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
# def netflix_calc():

# 	#run the predictiion against the real value using RMSE.py

# def netflix_write():
		#output movie id followed by predicted ratings instead of customer ids
		#ouptut file to netflix.out
