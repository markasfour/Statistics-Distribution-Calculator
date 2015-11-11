import os
import sys
import math

def isnumber(x):                                    #check if x is a number
    try:
        float(x)
        return True
    except ValueError:
        return False

def nCr(n, r):                                      #n Choose r
    return math.factorial(n) / math.factorial(r) / math.factorial(n-r)

def binomial(n, p):
    print 'X~B(', n, ', ', p, ')'
    expected = n * p
    print 'E(X) = ', expected
    variance = n * p * (1 - p)
    print 'V(X) = ', variance
    sd = math.sqrt(variance)
    print 'SD(X) = ', sd

def hyper_geometric(n, M, N):
    print 'X~H(', n, ', ', M, ', ', N, ')'
    expected = n * (M / N) 
    print 'E(X) = ', expected
    variance = ((n * M) / N) * (1 - (M / N)) * ((N - n) / (N - 1))
    print 'V(X) = ', variance
    sd = math.sqrt(variance)
    print 'SD(X) = ', sd

def negative_binomial(r, p):
    print 'X~NB(', r, ', ', p, ')'
    expected = (r * (1 - p)) / p
    print 'E(X) = ', expected
    variance = expected / p
    print 'V(X) = ', variance
    sd = math.sqrt(variance)
    print 'SD(X) = ', sd

def poisson(y):
    print 'X~P(', y, ')'
    expected = y
    print 'E(X) = ', expected
    variance = y
    print 'V(X) = ', variance
    sd = math.sqrt(variance)
    print 'SD(X) = ', sd

def main(argv):
    if (argv[0].isalpha()):                         #check if first arg is a letter
        argv[0] = argv[0].upper()                   #convert to uppercase
        
        if (argv[0] == 'B'):                        #if binomial
            if (len(argv) > 3):
                print 'Too many arguments'
            elif (isnumber(argv[1]) and isnumber(argv[2])):
                binomial(float(argv[1]), float(argv[2]))
            else:
                print 'Please enter numeric values for n and p'
        
        elif (argv[0] == 'H'):                      #if hyper geometric
            if (len(argv) > 4):
                print 'Too many arguments'
            elif (isnumber(argv[1]) and isnumber(argv[2]) and isnumber(argv[3])):
                hyper_geometric(float(argv[1]), float(argv[2]), float(argv[3]))
            else:
                print 'Please enter numeric values for n, M, and N'

        elif (argv[0] == 'NB'):                      #if negative binomial
            if (len(argv) > 3):
                print 'Too many arguments'
            elif (isnumber(argv[1]) and isnumber(argv[2])):
                negative_binomial(float(argv[1]), float(argv[2]))
            else:
                print 'Please enter numeric values for r and p'
 
        elif (argv[0] == 'P'):                      #if Poisson 
            print 'P'
            if (len(argv) > 2):
                print 'Too many arguments'
            elif (isnumber(argv[1])):
                poisson(float(argv[1]))
            else:
                print 'Please enter a numeric value for lambda'
 
        else:                                       #invalid letter argument
            print 'Distribution not recognized'
    else:                                           #invalid first argument
        print 'Please enter distribution as first argument'

if (__name__ == "__main__"):
    main(sys.argv[1:])
