import os, sys, re, math, random
import numpy as np

def boulwareUtilities (rv,Deadline):
	# print "-----Boulware----------"
	ut = []
	beta = 0.2
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


#################Generate values from random reservation values#######################
def tempgenerat(i,Deadline,roundnum,RV):
	temp=[0]
	#print str(i) + "  " + str(RV[roundnum-2])
	t1=0	
	b=0
	t=0
	#print str(roundnum) + " " + str(len(RV))
	for roundno in xrange(1,roundnum+1):

		t+=(np.log(float(roundno)/Deadline))*(np.log(float(roundno)/Deadline))

		# if(RV[0]-RV[roundno]==0 or (RV[0]-i)==0):
		# 	print str(RV[0]) + " " + str(RV[roundno]) + " " + str(i) +" " +str(roundno)

		p=np.log ( float(RV[0]-RV[roundno])/ (RV[0]-i) )
		t1=t1+(np.log(float(roundno)/Deadline))*p
		b=float(t1)/t

		# print str(b) + " " + str(t1) + " " + str(t) + " " + str(float(roundno)/Deadline)

		x = RV[0] + (i-RV[0])*(math.pow(float(roundno)/Deadline,b))

		

		x=float("{0:.4f}".format(x))
		temp.append(x)
	return temp

#############################################################

#############################################################

def getdelayfor4(delay_list,prevdelay):
	p=random.randint(1,5)
	if(p<=2):
		return prevdelay
	elif(p>2 and p<4):
		#increase
		l=[]
		ind=(prevdelay/10)-1
		end=min(ind+1,len(delay_list))
		# print str(ind) + " " + str(end)
		for i in xrange(ind,end):
			l.append(delay_list[i])
		return random.choice(l)
	else:
		#decrease
		l=[]
		ind=(prevdelay/10)-1
		# print ind
		end=max(ind-1,0)
		# print str(end) + " " + str(ind)
		for i in xrange(end,ind+1):
			l.append(delay_list[i])
		return random.choice(l)


def getdelay(delay_list,prevdelay):
	p=random.randint(1,10)
	if(p<=5):
		return prevdelay
	elif(p>5 and p<8):
		#increase
		l=[]
		ind=(prevdelay/5)-1
		end=min(ind+3,len(delay_list))
		# print str(ind) + " " + str(end)
		for i in xrange(ind,end):
			l.append(delay_list[i])
		return random.choice(l)
	else:
		#decrease
		l=[]
		ind=(prevdelay/5)-1
		end=max(ind-3,0)
		# print str(end) + " " + str(ind)
		for i in xrange(end,ind+1):
			l.append(delay_list[i])
		return random.choice(l)

#############################################################

def getmeetingrv(RV,roundnum,UpdateRate,delaylist,Deadline):
	delay_list=[45,40,35,30,25,20,15,10,5]
	# delay_list=[40,30,20,10]
	if(roundnum==0):
		delay=random.choice(delay_list)
		delaylist.append(delay)
		utility=getdelaycost(delay)
		# print str(utility) + " " + str(delay)
		return utility

	elif(roundnum%UpdateRate==0):
		# print "in" 
		delay=getdelay(delay_list,delaylist[len(delaylist)-1])   #### -> 9
		# delay=getdelayfor4(delay_list,delaylist[len(delaylist)-1])    #### -> 4
		delaylist.append(delay)
		# print delay
		utility=getdelaycost(delay)
		# print str(utility) + " "+ str(delay)
		return utility

	else:
		return RV[len(RV)-1]



#############################################################

def getdelaycost(delay):
	
	alpha=1.2
	Value=200
	cost=math.pow(delay,alpha)*2
	maxm=Value-math.pow(5,alpha)*2
	minm=Value-math.pow(45,alpha)*2
	# print str(maxm) + " " + str(minm)
	minm=Value-math.pow(45,alpha)*2
	if(float(Value-cost -minm)/(maxm-minm) ==0):
		return 0.01
	return float("{0:.4f}".format(float(Value-cost -minm)/(maxm-minm)))


#############################################################

def meetingrandomRV(random_rv):
	# print "----- "+str(n)+ "  ---------"
	# delay_list=[5,10,15,20,25,30,35,40,45]
	
	alpha=1.2
	delay_list=[45,40,35,30,25,20,15,10,5]
	# delay_list=[40,30,20,10]
	Value=200
	maxm=Value-math.pow(5,alpha)*2
	minm=Value-math.pow(45,alpha)*2
	for i in xrange(0,len(delay_list)):
		cost=math.pow(delay_list[i],alpha)*2
		u=float(Value-cost -minm)/(maxm-minm)
		if(u==0):
			u=0.01
		random_rv.append(float("{0:.4f}".format(u)))

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
		direction=random.randint(1,4)    #  ---> 4
		# direction=random.choice([1,4])     #  ---> 2
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
		direction=random.randint(1,4)
		# direction=random.choice([1,4])
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
##############################
def generatereservationvalue(flag,roundnum,RV):
	if(flag==1):
		if(roundnum==1):
		 	return random.choice([0.1,0.2,0.6,0.9])
		elif(roundnum%(50)==0):
			return random.choice([0.1,0.2,0.6,0.9])
		else:
			return RV[len(RV)-1]

	elif(flag==2):
		if(roundnum==1):
		 	return random.choice([0.1,0.2,0.6,0.9])
		elif(roundnum%(20)==0):
			return random.choice([0.1,0.2,0.6,0.9])
		else:
			return RV[len(RV)-1]
	elif(flag==3):
		if(roundnum==1):
		 	return random.choice([0.1,0.2,0.6,0.9])
		elif(roundnum%(10)==0):
			return random.choice([0.1,0.2,0.6,0.9])
		else:
			return RV[len(RV)-1]
	elif(flag==4):
		if(roundnum==1):
		 	return random.choice([0.1,0.2,0.6,0.9])
		elif(roundnum%(5)==0):
			return random.choice([0.1,0.2,0.6,0.9])
		else:
			return RV[len(RV)-1]

	elif(flag==5):
		if(roundnum==1):
		 	return random.choice([0.1,0.2,0.6,0.9])
		elif(roundnum%(2)==0):
			return random.choice([0.1,0.2,0.6,0.9])
		else:
			return RV[len(RV)-1]
		
	elif(flag==6):
		#l=[0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.6]
		#l=[0.0, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.4]
		l=[  0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.4]
		return l[roundnum-1]

	elif(flag==7):
		l=[0.9,0.1,0.36 ,0.75, 0.75 ,0.12 ,0.75,0.12 ,0.75,0.12]
		# l=[0.2,0.3,0.4,0.5,0.6,0.7]
		return l[(roundnum/2)%2]
# def getclosest():

def main(A_utility_space,B_utility_space,Deadline):
	All_UpdateRates = [2,5,10,20,50]
	for UpdateRate in All_UpdateRates:

		print "------ " + str(UpdateRate)  +  " -------"

		Averageutility_A = 0.0
		Averageutility_B = 0.0

		disagree = 0  
		for iterations in xrange(1,101):
			rv = 0

			closest_val = lambda num,collection:min(collection,key=lambda x:abs(x-num))   #####  --> compute closest value

			A_utilites = list(A_utility_space.values())
			B_utilites = list(B_utility_space.values())

			# A = boulwareUtilities(rv,Deadline)            ###### -> Boulware
			# A = GenerateTimUtility(rv,Deadline)         ###### -> ONAC
			# A.reverse()
			# print A

			# UpdateRate = 2
			meetingrandom_rv=[]
			meetingrandomRV(meetingrandom_rv)
			random_rv=meetingrandom_rv
			delaylist=[]

			RV=[0]
			
			# random_rv=[0.12,0.75]
			# random_rv=[0.12,0.321,0.57,0.75]
			
			means_offers=[]
			gamma=[]
			new_gamma=[]
			new_probability=[]
			new_belief_plots=[]

			intervals = len(random_rv)

			x=[]
			for i in xrange(1,Deadline+1):
				x.append(i)

			x_belief=[]
			for i in xrange(0,Deadline+1):
				x_belief.append(i)

			for i in xrange(0,intervals):
				gamma.append(0)
				new_gamma.append(0)
				new_belief_plots.append([0])
				new_probability.append(float("{0:.4f}".format(float(1)/intervals)))
				new_belief_plots[i][0]=new_probability[i]

			total = 0

			Utilities=[]
			actual_utility=[]
			new_WeightedUtility=[]

			offers=[]
			mean1_RV=0

			for rv in random_rv:
				# Utilities.append(GenerateTimUtility(rv,Deadline))     ######   ----> Tims
				Utilities.append(boulwareUtilities(rv,Deadline))        ######   -----> Boulware

			# print Utilities[1]
			# break

			GridSize=100

			# Gridcoords=[GridSize/2 ,GridSize/2]



			Gridcoords=[GridSize/2 +random.choice([-4,0,4]),GridSize/2+random.choice([-4,0,4])]

			B_old_bid = 'k'

			agree = -1

			for roundnum in range(1,Deadline+1):
				# roundnum = i

				# RV.append(float("{0:.4f}".format(generatereservationvalue(7,roundnum-1,RV)) ))

				# RV.append( float( "{0:.4f}".format( FireRV(RV,roundnum-1,Deadline,UpdateRate,GridSize,Gridcoords) ) ) )     #### RV -> update Fire
				RV.append(float("{0:.4f}".format( getmeetingrv(RV,roundnum-1,UpdateRate,delaylist,Deadline) ) ) )           ##### RV -> meeting domain

				# A = GenerateTimUtility(RV[-1],Deadline)         ###### -> ONAC
				A = boulwareUtilities(RV[-1],Deadline)            ###### -> Boulware
				A.reverse()
				
				# utility_RV=GenerateTimUtility(RV[roundnum-1],Deadline)              ###### -> Tims
				utility_RV=boulwareUtilities(RV[roundnum-1],Deadline)             ###### -> Boulware

				temp_offers=[]
				
				# print "--------"
				for i in random_rv:
					
					#print str(i) + "  " + str(RV[0]) + " " +str(roundnum)
					temp_offers.append(tempgenerat(i,Deadline,roundnum,RV))
				
					# offers.append(offers(i,Deadline,roundnum,RV))

				# print temp_offers
				# print "--------"
				mean_RV=np.mean(RV)
				means1=[]
				for i in xrange(0,intervals):
					means1.append(np.mean(temp_offers[i]))

				# if(roundnum%UpdateRate==0):
				# 	print offers[bla]
				offers=temp_offers
				means_offers=means1

				# if(roundnum%UpdateRate==0):
				# 	print offers[bla]
				##################### Calculate Gamma value ####################

				#print "#####################"
				for i in xrange(0,len(offers)):

					variation=0
					d1=0
					d2=0
					for j in xrange(0,len(offers[i])):
						variation += (RV[j] - mean_RV) * (offers[i][j]-means_offers[i])
						d1+=math.pow((RV[j] - mean_RV),2)
						d2+=math.pow((offers[i][j]-means_offers[i]),2)
					denominator=math.sqrt(d1*d2)
					#if(roundnum>=1):
					gamma[i] = float("{0:.4f}".format(float(variation)/denominator))
					new_gamma[i]=float(gamma[i]+1)/2
						
				########################################################" 
				

				##################### Updating weights using Bayesian technique ########################################
			
				#if(roundnum>=1):

				new_total=0
				for i in xrange(0,len(new_probability)):
					new_probability[i]=new_probability[i]*new_gamma[i]
					# print "------"
					# print new_probability[i]
					# print "------"
					new_total+=new_probability[i]
					
					
				for i in xrange(0,len(new_probability)):
					new_probability[i]=float("{0:.4f}".format(new_probability[i]/new_total))
					if(new_probability[i]<=0.0002):
						new_probability[i]=0.0002
					if(new_probability[i]>=0.9998):
						new_probability[i]=0.9998
					new_belief_plots[i].append(new_probability[i])


				#############################################################

				new_CombinedUtility=0
				for i in xrange(0,len(new_probability)):
					new_CombinedUtility+=new_probability[i]*Utilities[i][len(Utilities[i])-roundnum]
				
				new_WeightedUtility.append(new_CombinedUtility)

				# B = counter_weighted_utility
				

				# print RV[-1]
				# B = boulwareUtilities(RV[-1],Deadline)
				# B.reverse()

				# print len(counter_weighted_utility) , roundnum
				# print roundnum
				A_ut = closest_val(A[roundnum-1],A_utilites)
				if(A_ut <= A_utility_space[B_old_bid] ):
					# print "A accepts bid by agent B with utility: " , A_utility_space[B_old_bid] ,B_old_bid 
					# print "B's utility: " , B_utility_space[B_old_bid]  , " A's utility: " , A_utility_space[B_old_bid]
					Averageutility_A += A_utility_space[B_old_bid]
					Averageutility_B += B_utility_space[B_old_bid]
					agree = 1
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

				B_ut = new_WeightedUtility[roundnum-1]
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
					agree = 1
					break

				else:
					keys = [key for key, value in B_utility_space.iteritems() if value == B_ut]
					B_bid = random.choice(keys)
					B_old_bid=B_bid
					# print "bid sent to agent A: " , B_bid

			# print counter_weighted_utility
			# print B
			# print len(counter_weighted_utility) , len(B)
		if(agree==-1):
			disagree +=1
		Averageutility_A = Averageutility_A / 100
		Averageutility_B = Averageutility_B / 100
 
		print "A's average utility: " , Averageutility_A , " B's average utility: " , Averageutility_B
		print "Disagreements are: " , disagree

if __name__ == '__main__':

	# [0.01, 0.142, 0.2804, 0.415, 0.5451, 0.6701, 0.7889, 0.8999, 1.0]

	B_utility_space = {'a' : 0.01 , 'b' : 0.142 , 'c' : 0.2804 , 'd' : 0.3 , 'e' : 0.415 , 'f' : 0.5451 , 'g' : 0.6701 , 'h' : 0.7 , 'i' : 0.7889 , 'j' : 0.899 , 'k' : 1.0 };

	A_utility_space = {'a' : 0.99 , 'b' : 0.858 , 'c' : 0.7196 , 'd' : 0.7 , 'e' : 0.585 , 'f' : 0.454 , 'g' : 0.329 , 'h' : 0.3 , 'i' : 0.211 , 'j' : 0.1009 , 'k' : 0.0 };

	main(A_utility_space,B_utility_space,100)



