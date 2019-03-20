# Calculate the bayesian_AB function and return the option with gretaer probability

from scipy.special import beta

def calculate_ab(alpha_A,beta_A,alpha_B,beta_B):
  prefer_b_probability=0.0
  for i in range(alpha_B):
    num=beta(alpha_A+i,(beta_B+beta_A))
    den=(beta_B+i)*beta(1+i,beta_B)*beta(alpha_A,beta_A)
    result=num/den
    prefer_b_probability+=result
  return prefer_b_probability

if(calculate_ab(aA,bA,aB,bB)>=0.5):
  return b
else:
  return a
