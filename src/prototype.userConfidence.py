#!/usr/bin/python
# -*- coding: utf-8 -*-



def normalize(value,zeropoint,onepoint):
	if onepoint==zeropoint:
		return None
	return max(0.0,min(1.0,((value+0.0) - zeropoint)/(onepoint-zeropoint)))
	
def userConfidence(NT,NS,TA,CS,TT,SE):
	print "Touches:",NT
	print "Stops:",NS
	print "Angles:",TA
	print "Speedv:",CS
	print "Time:",TT
	print "Edge:", SE
	
	confidence=normalize(NT,4,1)+normalize(NS,5,0)+normalize(TA,0.3,0.05)+normalize(CS,3.0,0)+normalize(TT,15,1)
	if(TA>0.5):confidence = confidence / 2
	#confidence now is 0..5
	return abs(SE - 0.5 + confidence/10)
	
	
	
test=userConfidence(1, 0, 0.3, 100, 5.3, 1)
print "UC:",test
print "User thinks that this is",
if test<0.1: print "TOTALLY FALSE"
elif test<0.3: print "FALSE"
elif test<0.5: print "MOSTLY FALSE"
elif test<0.7: print "HALF TRUE"
elif test<0.9: print "MOSTLY TRUE"
else: print "TRUE"

