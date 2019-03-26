# Calculate the bayesian_AB function and return the option with greater probability
import sys
from scipy.special import beta

def calculate_ab(alpha_A,beta_A,alpha_B,beta_B):
    prefer_b_probability=0.0
    for i in range(alpha_B):
        num=beta(alpha_A+i,(beta_B+beta_A))
        den=(beta_B+i)*beta(1+i,beta_B)*beta(alpha_A,beta_A)
        result=num/den
        prefer_b_probability+=result
    return prefer_b_probability


if __name__ == '__main__':

    # wins (aka clicks) in A experiments = first command line argument
    wA = int(sys.argv[1])
    # total number of A experiments (aka trials) = second command line argument
    tA = int(sys.argv[2])
    # wins in B experiments = third command line argument
    wB = int(sys.argv[3])
    # total number of B experiments = fourth command line argument
    tB  = int(sys.argv[4])

    aA=wA
    bA=tA-wA
    aB=wB
    bB=tB-wB

    if(calculate_ab(aA,bA,aB,bB)>=0.5):
        print('Experiment B has the best conversion rate')
    else:
        print('Experiment A has the best conversion rate')
