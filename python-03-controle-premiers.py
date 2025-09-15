import math
import numpy

def premier(n):

    a,b= 0,0

    for i in range (int(n**(1/2))):
        a+=1
        print(a)
        if (n%a)==0 and a !=1 :
            print(n,"n'est pas premier")
            break
        else:
            print(a,n)
            print(n,"est  premier")
            



