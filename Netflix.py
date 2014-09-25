import math
import sys
netflix_dict = {}
avgmovie_dict = {}
avguser_dict = {}
predict_dict = {}

def rmse(a,p):
	assert (len(a) == len(p))
	s = sum(map(lambda x,y : (x-y)**2, a,p))
	return (math.sqrt(s/len(a)))

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
	with open('/u/prat0318/netflix-tests/savant-cacheActual.txt','r') as f: #This accesses the average movie rating file created by savant
		j = eval(f.read())
	for w in j.keys():
		predict_dict[w] = j[w]
	return (predict_dict)

def netflix_solve():
	netflix_read('/u/downing/cs/netflix/probe.txt') #/u/downing/cs/netflix/probe.txt
	netflix_moviecache('/u/prat0318/netflix-tests/savant-cacheMovies.txt')
	netflix_usercache('/u/prat0318/netflix-tests/savant-cacheUsers.txt')
	netflix_panswers('/u/prat0318/netflix-tests/savant-cacheActual.txt')
	
	s1 = 0
	for x2 in avgmovie_dict.values():
		s1 += x2
	total_avg = (s1/len(avgmovie_dict))

	m = 0
	c = 0
	w1 = 0.473
	a = []
	p = []


	for x in netflix_dict.keys(): # read the key (movie title) from the dictionairy created
		# print (x,':') 
		try:
			m = avgmovie_dict[int(x)] 	# go through savant-cachemovies.txt and find average movie rating 
		except KeyError:
			m = total_avg
		for y in netflix_dict[x]:
			try:
				c = avguser_dict[int(y)] 	# read  the associated values (customer ids) for the movie and find their average rating
			except KeyError:
				c = total_avg
			prediction =  total_avg + w1*(m-total_avg) + (1-w1)*(c-total_avg) 	# for each value, predict a weighted guess (using average customer rating and movie rating)	
			a.append(prediction) 
			# print (prediction)
			rating = predict_dict[str(x) + " " + str(y)]
			p.append(rating)
	print (rmse(a,p))

netflix_solve()