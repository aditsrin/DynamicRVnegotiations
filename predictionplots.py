import numpy.polynomial.polynomial as poly
import matplotlib
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

import numpy as np

if __name__ == '__main__':

	# PerBR = [84,90,90,85,71]
	# PerC = [88 ,89,91,89,84]
	# # PerE = [80 , 85,79,74,84]
	# l = [91, 89, 89, 90, 92]

	PerBR=[0.2331,0.234708,0.23079,0.199254,0.258823,0.31486,0.303138,0.306079,0.315225,0.303703]
	PerC=[0.210679,0.228532,0.225402,0.21354,0.24873,0.3194,0.32575,0.3001,0.2985,0.3039]
	# E=[0.227461,0.232184,0.228086,0.21603,0.24873,0.322677,0.362455,0.2861,0.2885,0.3039]
	l=[0.11762,0.055067,0.15542,0.09279,0.0302,0.3024,0.315,0.3024,0.2961,0.00712]




	x_axis=[]
	my_xticks=[]
	UpdateRate=[2,5,10,20,50]
	# Intervals=[4,2]
	Intervals = [9]

	for i in xrange(1,len(PerC)+1):
		x_axis.append(i)
	for i in xrange(0,len(Intervals)):
		for j in xrange(0,len(UpdateRate)):
			tup=(Intervals[i],UpdateRate[j])
			my_xticks.append(tup)

	

	plt.figure('smoothness')
	font = {'weight' : 'bold','size'   : 20 }
	plt.xticks(x_axis,my_xticks)
	plt.yticks(fontsize=14,fontweight='bold')
	plt.xticks(fontsize=13,fontweight='bold')

	legend_properties = {'weight':'bold', 'size':15}

	lineBR,=plt.plot(x_axis,PerBR, marker='o', linestyle='--', color='r', linewidth=6, markersize=12)
	lineC, =plt.plot(x_axis,PerC, marker='^', linestyle='-.', color='g', linewidth=7, markersize=12)
	# lineE, =plt.plot(x_axis,PerE, marker='s', linestyle=':', color='b', linewidth=7, markersize=12)
	linel, =plt.plot(x_axis,l, marker='d', linestyle='-', color='m', linewidth=2, markersize=12)
	

	# plt.legend([lineBR,lineC,lineE,linel],["Bayesian","Counter","Exponential","LSTM"],loc=0,ncol=1, handlelength=4,prop=legend_properties)
	plt.legend([lineBR,lineC,linel],["Bayesian","Counter","LSTM"],loc=0,ncol=1, handlelength=4,prop=legend_properties)
	plt.xlabel("Hypothesis,UpdateRate",**font)
	plt.ylabel("Number of times Misclassified",**font)

	print np.mean(PerBR)
	print np.mean(PerC)
	# print np.mean(PerE)
	print np.mean(l)
	plt.savefig('predictionfr100.pdf', format='pdf', dpi=1000)
