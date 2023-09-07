import numpy as np
import math
#Input: the lists of prior probabilities, likelihood, and test data
#Output: list of corresponding posterior probabilities
#
def deg(l, size):
    a = 0
    mult = 1
    while a !=size:
        mult = mult*l
        a = a+1
    return mult


def posteriorFunc(priorProb, likhd, data):
    '''
       
       Student implements the function to calculate posterior probabilities here
       
	'''

    size = len(priorProb)


    ordered = []
    posProb = []

    a =0




    for d in data:
        if d == 1:
            num1 = deg(likhd[a], size)
            num2 = num1 * priorProb[a]
            a = a+1
            ordered.append(num2)
        else:
            rev = 1 - likhd[a]
            num1 = deg(rev, size)
            num2 = num1 * priorProb[a]
            a = a + 1
            ordered.append(num2)

    sum = 0

    for o in ordered:
        sum = sum + o

    coef = 1/sum

    for o in ordered:
        num = o*coef
        posProb.append(num)


    return posProb

#Input the lists of prior probabilites, likhd/likelihood, training data, and one test datapoint
#Output: probability that the test datapoint happens
#Note: this function will call posteriorFunc to calculate the posterior probabilites 
def predictionFunc (priorProb, likhd, data, fPoint):
    '''
       
       Student implements the function to calculate predictive probability here
       
	'''

    post = posteriorFunc(priorProb, likhd, data)
    a = 0
    sum = 0

    for p in post:
        sum = (p*likhd[a]) + sum
        a = a+1
    predictProb = sum


    if fPoint == 0:
        predictProb = 1 - sum


    return predictProb