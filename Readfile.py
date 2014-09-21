import math
#def netflix_predict():
	# read the key (movie title) from the dictionairy created
	# go through savant-cachemovies.txt and find average movie rating 
	# read  the associated values (customer ids) for the movie and find their average rating
	# for each value, predict a weighted guess (using average customer rating and movie rating)

	#read movie title -> find the average rating for that movie through the cache
	#read customer id and find corresponding avg customer id rating through cache
	# predict a rating based on the above 2 averages. Try using different weights 	
def rmse(a,p):
	assert (len(a) == len(p))
	sum1 = 0
	for i in range(len(a)):
		sum1 += (a[i] - p[i])**2
	mean = sum1/len(a)
	r = math.sqrt(mean)
	return r

def main():

	index = 0

	r = open('/u/downing/cs/netflix/probe.txt','r')
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
	# print (netflix_dict)


	# return (netflix_dict)
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
	# print (avguser_dict[30878])


	predict_dict={}
	with open('/u/prat0318/netflix-tests/cct667-ProbeCacheAnswers.txt','r') as f: #This accesses the average movie rating file created by savant
		j = f.readlines()

	for q in j:
		q1 = q.split()
		movID = int(q1[0])
		cusID = int(q1[1])
		rat = int(q1[2])
		if (movID in predict_dict.keys()):
			predict_dict[movID][cusID] = rat
		else:
			predict_dict[movID] = {cusID : rat}

	# print (predict_dict)	
		# """if (movID in predict_dict.keys()):
		# 	predict_dict[movID].append([cusID, rat])
		# else:
		# 	predict_dict[movID] = [[cusID, rat]]"""


	m = 0
	c = 0
	w1 = 0.5
	w2 = 0.5
	a = []
	p = []

	print (predict_dict[9999])
	# for x in netflix_dict.keys():
	# 	if x in avgmovie_dict.keys():
	# 		m = avgmovie_dict[int(x)]
	# 	else:
	# 		m = 3
	# 	for y in netflix_dict[x]:
	# 		if y in avguser_dict.keys():
	# 			c = avguser_dict[int(y)]
	# 		else:
	# 			c = 3	
	# 		prediction = w1*c + w2*m		
	# 		a.append(prediction) 
	# 		for x1 in (predict_dict[x].keys()):
	# 			p.append(predict_dict[x][x1])

	# print(len(p))
	# print(len(a))
	
	rmse(a,p)

main()
	# with open('/u/prat0318/netflix-tests/savant-cacheUsers.txt','r') as f:
	# 	k = f.readlines()
	# avguser_dict = {}
	# for m in k:
	# 	k1 = m.split()
	# 	k11 = k1[0].strip('\x00')
	# 	k12 = k1[1].strip('\x00')
	# 	# print (k11, k12)
	# 	avguser_dict[int(k11)] = float(k12)		
	# print (avguser_dict)
# 	avgmovie = '/u/prat0318/netflix-tests/savant-cacheMovies.txt'
# 	avgmovie_dict = {}
# 	with open(avgmovie,'wb') as f:
# 		pickle.dump(avgmovie_dict, f)
# 	with open(avgmovie,'rb') as f:
# 		print (pickle.load(f))
	
	 

