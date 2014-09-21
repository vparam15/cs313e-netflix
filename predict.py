def main():
	predict_dict={}
	with open('/u/prat0318/netflix-tests/cct667-ProbeCacheAnswers.txt','r') as f: #This accesses the average movie rating file created by savant
		j = f.readlines()

	for q in j:
		q1 = q.split()
		movID = int(q1[0])
		cusID = int(q1[1])
		rat = int(q1[2])
		if (movID in predict_dict.keys()):
			predict_dict[movID].append([cusID, rat])
		else:
			predict_dict[movID] = [[cusID, rat]]

	print (predict_dict[1].index('30878'))

main()