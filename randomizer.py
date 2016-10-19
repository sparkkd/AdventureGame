from random import uniform

#Returns a boolean with the given probability of being true
def Chance(probability = 0.5):
	rand = uniform(0,1)
	
	if rand > probability:
		return False		
	else:
		return True
		