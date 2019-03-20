import bayesian_ab_testing

def test_thompson_sampling():

	wins_a = 350
	wins_b = 32
	trials_a = 1000
	trials_b = 100
	
	var = bayesian_ab_testing.thompson_sampling(wins_a,	trials_a, wins_b, trials_b)
	
	assert isinstance(var, str)
	assert var in ['a','b']
	