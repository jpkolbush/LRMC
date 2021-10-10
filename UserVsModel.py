from math import log
def findTotProbs(filename):
	#Read results
	f = open('2017results.csv', 'r')
	results = []
	for line in f:
		results.append(line.split(","))
	f.close()

	#read filenames
	g = open(filename, "r")
	modelPred = []
	for line in f:
		modelPred.append(line.split(","))
	g.close()


	totalLogSum = 0
	i = 0
	j = 5
	while i < 64:
		if results[i][j] == "0":
			j -= 1
		teamName = results[i][0]
		k = 0
		found = False
		while k < 64 and not found:
			if modelPred[k][0] == teamName:
				totalLogSum += log(float(modelPred[k][j]))
			k+=1
		if k == 64 and not found:
			print(teamName)
		i+=1

	print("total log sum is " + totalLogSum)

findTotProbs("2017UserProbs.csv")
findTotProbs("538Probs.csv")