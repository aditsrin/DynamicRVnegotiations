import os, sys, re, math, random

def boulwareUtilities (rv,Deadline):
	# print "-----Boulware----------"
	ut = []
	beta = 1.2
	beta = float(1)/beta
	for i in range(1,Deadline+1):
		minm = min(i,Deadline)
		time = float(minm)/Deadline
		curr_ut = rv + (1-rv)*(math.pow(time,beta))
		# print "================"
		# print minm
		# print time
		# print beta
		# print "================"
		ut.append(float("{0:.4f}".format(curr_ut)))
	return ut

#############################################################

def GenerateTimUtility( rv,rounds):
	# print "-----ONAC-------"
	l=[]
	l.append(rv);
	for i in range(1,rounds):
		l.append(float((l[i-1]+1)*(l[i-1]+1))/4)
	return l

#############################################################

def getindex(RV,intervals):
	# Utilities=[0.12,0.75]
	# for i in xrange(0,len(Utilities)):
	# 	if(RV==Utilities[i]):
	# 		return i

	low=0
	a=float(1)/intervals
	high=a
	for i in xrange(1,intervals+1):
		if(RV >=low and RV < high ):
			return i-1
		else:
			low=high
			high+=a

############################################################

def getflag(direction,Gridcoords,GridSize):
	flag=0
	if(direction==1):
		if(Gridcoords[0]!=0):
			Gridcoords[0]-=1                 ### Moving North
		if(Gridcoords[1]==GridSize-1):
			flag=3
		elif(Gridcoords[1]==0):
			flag=2
		elif(Gridcoords[0]+1==GridSize-1):
			flag=4
	elif(direction==2):
		if(Gridcoords[1]!=0):
			Gridcoords[1]-=1                 ### Moving West
		if(Gridcoords[0]==0):
			flag=1
		elif(Gridcoords[1]+1==GridSize-1):
			flag==3
		elif(Gridcoords[0]==GridSize-1):
			flag=4

	elif(direction==3):
		if(Gridcoords[1]!=GridSize-1):
			Gridcoords[1]+=1                 ### Moving East
		if(Gridcoords[0]==GridSize-1):
			flag=4
		elif(Gridcoords[0]==0):
			flag=1
		elif(Gridcoords[1]-1==0):
			flag=2
	else:
		if(Gridcoords[0]!=GridSize-1):
			Gridcoords[0]+=1                 ### Moving South
		if(Gridcoords[0]-1==0):
			flag=1
		elif(Gridcoords[1]==GridSize-1):
			flag=3
		elif(Gridcoords[1]==0):
			flag=2
	return flag


def FireRV(RV,roundnum,Deadline,UpdateRate,GridSize,Gridcoords):
	ManPower=[12,10,7,4]
	Utilities=[0.75,0.57,0.321,0.12]
	
	if(roundnum==0):
		# print "---round 1: =="
		# direction=random.randint(1,4)    #  ---> 4
		direction=random.choice([1,4])     #  ---> 2
		### Gridcoords Updation 
		flag=getflag(direction,Gridcoords,GridSize)
		# print "------"
		# print direction
		# print Gridcoords
		# print "------"
		if(flag==0 ):
			return Utilities[direction-1]
			#return getReservationUtility(ManPower[direction-1])

		else:	
			# print "This case: "+str(flag) + " "+ str(ManPower[direction-1] )
			# return getReservationUtility( max (ManPower[flag-1], ManPower[direction-1] )) 
			return max (Utilities[flag-1], Utilities[direction-1] )

	elif(roundnum%UpdateRate==0):
		# print "---update == " + str(roundnum)   
		# direction=random.randint(1,4)
		direction=random.choice([1,4])
		flag=getflag(direction,Gridcoords,GridSize)
		# print "------"
		# print direction
		# print Gridcoords
		# print "------"
		if(flag==0 ):
			# return getReservationUtility(ManPower[direction-1])
			return Utilities[direction-1]

		else:	
			# print "This case: "+str(flag) + " "+ str(ManPower[direction-1] )
			# return getReservationUtility( max (ManPower[flag-1], ManPower[direction-1] ) )
			return max (Utilities[flag-1], Utilities[direction-1] )

	else:
		return RV[len(RV)-1]

# def getclosest():

def main(A_utility_space,B_utility_space,Deadline):
	All_UpdateRates = [2,5,10,20,50]
	for UpdateRate in All_UpdateRates:

		print "------ " + str(UpdateRate)  +  " -------"

		Averageutility_A = 0.0
		Averageutility_B = 0.0

		for iterations in xrange(1,101):
			rv = 0

			closest_val = lambda num,collection:min(collection,key=lambda x:abs(x-num))   #####  --> compute closest value

			A_utilites = list(A_utility_space.values())
			B_utilites = list(B_utility_space.values())

			A = GenerateTimUtility(rv,Deadline)
			# A = boulwareUtilities(rv,Deadline)
			A.reverse()
			# print A

			# UpdateRate = 2
			RV=[0]
			random_rv=[0.12,0.75]

			counter = []
			exponential_weights = []
			exponential_belief_plots = []
			exponential_probabilities = []
			exponential_weighted_utility=[]

			intervals = len(random_rv)

			x=[]
			for i in xrange(1,Deadline+1):
				x.append(i)

			x_belief=[]
			for i in xrange(0,Deadline+1):
				x_belief.append(i)

			for i in xrange(0,intervals):
				exponential_belief_plots.append([0])
				exponential_weights.append(0)
				counter.append(0)
				exponential_probabilities.append(float(1)/intervals)

			total = 0

			Utilities=[]
			actual_utility=[]
			new_WeightedUtility=[]

			for rv in random_rv:
				# Utilities.append(GenerateTimUtility(rv,Deadline))     ######   ----> Tims
				Utilities.append(boulwareUtilities(rv,Deadline))        ######   -----> Boulware

			# print Utilities[1]
			# break

			GridSize=20

			# Gridcoords=[GridSize/2 ,GridSize/2]



			Gridcoords=[GridSize/2 +random.choice([-4,0,4]),GridSize/2+random.choice([-4,0,4])]

			B_old_bid = 'k'

			for roundnum in range(1,Deadline+1):
				# roundnum = i

				RV.append( float( "{0:.4f}".format( FireRV(RV,roundnum-1,Deadline,UpdateRate,GridSize,Gridcoords) ) ) )     #### RV -> update Fire

				ind=getindex(RV[roundnum],intervals)
				# print RV[roundnum]
				# print ind
				counter[ind]+=1
				# print exponential

				summation=0
				for i in xrange(0,len(exponential_weights)):
					exponential_weights[i]=math.pow(2,counter[i])
					summation+=exponential_weights[i]

				# print "--------"
				# print exponential_weights
				for i in xrange(0,len(exponential_weights)):
					exponential_weights[i]=float(exponential_weights[i])/summation
					exponential_weights[i]=float("{0:.4f}".format(exponential_weights[i]))
					exponential_belief_plots[i].append(exponential_weights[i])
					exponential_probabilities[i]=exponential_weights[i]

				exponential_combined_utility=0
				
				for i in xrange(0,len(exponential_probabilities)):	
					exponential_combined_utility+=exponential_probabilities[i]*Utilities[i][len(Utilities[i])-roundnum]
					
				exponential_weighted_utility.append(float("{0:.4f}".format(exponential_combined_utility)) )


				#############################################################

				# B = exponential_weighted_utility
				

				# print RV[-1]
				# B = boulwareUtilities(RV[-1],Deadline)
				# B.reverse()

				# print len(exponential_weighted_utility) , roundnum

				A_ut = closest_val(A[roundnum],A_utilites)
				if(A_ut <= A_utility_space[B_old_bid] ):
					# print "A accepts bid by agent B with utility: " , A_utility_space[B_old_bid] ,B_old_bid 
					# print "B's utility: " , B_utility_space[B_old_bid]  , " A's utility: " , A_utility_space[B_old_bid]
					Averageutility_A += A_utility_space[B_old_bid]
					Averageutility_B += B_utility_space[B_old_bid]
					break
				# print A_ut
				keys = [key for key, value in A_utility_space.iteritems() if value == A_ut]
				A_bid = random.choice(keys)
				A_ut = B_utility_space[A_bid]      ##### -> opponents propsed utility (agent A)

				# print "bid sent to agent B: " , A_bid

				# keys = [key for key, value in utility_space.iteritems() if value == A_ut]
				# print keys
				# break
				# B_ut = closest_val(B[roundnum],B_utilites)

				B_ut = exponential_weighted_utility[roundnum-1]
				B_ut = closest_val(B_ut,B_utilites)

				
				if A_ut >= B_ut:
					# print 'Accepted at', roundnum, A_ut
					acceptB_ut = A_ut
					keys = [key for key, value in B_utility_space.iteritems() if value == A_ut]
					# B_old_bid= random.choice(keys)
					# print "B acceptis bid by agent A with utility: ", B_utility_space[A_bid] , A_bid
					# print "B's utility: " , B_utility_space[A_bid]  , " A's utility: " , A_utility_space[A_bid]
					Averageutility_A += A_utility_space[A_bid]
					Averageutility_B += B_utility_space[A_bid]
					break

				else:
					keys = [key for key, value in B_utility_space.iteritems() if value == B_ut]
					B_bid = random.choice(keys)
					B_old_bid=B_bid
					# print "bid sent to agent A: " , B_bid

			# print exponential_weighted_utility
			# print B
			# print len(exponential_weighted_utility) , len(B)
		Averageutility_A = Averageutility_A / 100
		Averageutility_B = Averageutility_B / 100
 
		print "A's average utility: " , Averageutility_A , " B's average utility: " , Averageutility_B

if __name__ == '__main__':

	B_utility_space = {'a' : 0.0 , 'b' : 0.1 , 'c' : 0.2 , 'd' : 0.3 , 'e' : 0.4 , 'f' : 0.5 , 'g' : 0.6 , 'h' : 0.7 , 'i' : 0.8 , 'j' : 0.9 , 'k' : 1.0 };

	A_utility_space = {'a' : 1.0 , 'b' : 0.9 , 'c' : 0.8 , 'd' : 0.7 , 'e' : 0.6 , 'f' : 0.5 , 'g' : 0.4 , 'h' : 0.3 , 'i' : 0.2 , 'j' : 0.1 , 'k' : 0.0 };

	main(A_utility_space,B_utility_space,100)



