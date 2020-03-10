import random
import numpy as np
from scipy.stats import ttest_1samp
import pandas as pd

if __name__ == '__main__':

	ages = [32,34,29,29,22,39,38,37,38,36,30,26,22,22]
	print ages
	ages_mean = np.mean(ages)
	ttest , pval = ttest_1samp(ages,29)
	print pval

	df = pd.read_csv("Bayesian/BayesianBoulwareFire2.csv")
	saved_column = df.column_name
	print saved_column

	# y1=[]
	# y2=[]
	# y3=[]
	# for i in xrange(0,100):
	# 	a = random.randint(1,1000)
	# 	y1.append(a)
	# 	y2.append(a*2)
	# 	y3.append(a*3)

	# mu1, sigma1 = 20, np.sqrt(10) # mean and standard deviation
	# s1 = np.random.normal(mu1, sigma1, 100)
	# mu2, sigma2 = 15, np.sqrt(5) # mean and standard deviation
	# s2 = np.random.normal(mu1, sigma1, 100)

	# s1= np.asarray(s1).reshape(-1)
	# s2= np.asarray(s2).reshape(-1)
	# whole = np.array([s1,s2])
	# print s2
	# PValue_B = np.asarray(PValue_B).reshape(-1)
	#whole = np.array([PValue_A, PValue_B])
	#np.savetxt("BayesianBoulwareFire4.csv", whole.transpose(), delimiter=" ")
	# print y1 , y2 , y3

	# y1 = np.asarray(y1).reshape(-1)
	# y2 = np.asarray(y2).reshape(-1)
	# y3 = np.asarray(y3).reshape(-1)

	# whole = np.array([y1,y2,y3])
	# np.savetxt("D_FuncData.csv", whole.transpose(), delimiter=" ")
	#print whole
