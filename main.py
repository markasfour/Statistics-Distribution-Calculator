import os
import sys
import math

def binomial(n, p):
    print 'X~B(', n, ', ', p, ')'

def hyper_geometric(n, M, N):
    print 'X~H(', n, ', ', M, ', ', N, ')'

def negative_binomial(r, p):
    print 'X~NB(', r, ', ', p, ')'

def poisson(y):
    print 'X~P(', y, ')'

def main(argv):
    if (argv[0].isalpha()):                         #check if first arg is a letter
        argv[0] = argv[0].upper()                   #convert to uppercase
        
        if (argv[0] == 'B'):                        #if binomial
            if (len(argv) > 3):
                print 'Too many arguments'
            elif (argv[1].isdigit() and argv[2].isdigit()):
                binomial(argv[1], argv[2])
            else:
                print 'Please enter numeric values for n and p'
        
        elif (argv[0] == 'H'):                      #if hyper geometric
            if (len(argv) > 4):
                print 'Too many arguments'
            elif (argv[1].isdigit() and argv[2].isdigit() and argv[3].isdigit()):
                hyper_geometric(argv[1], argv[2], argv[3])
            else:
                print 'Please enter numeric values for n, M, and N'

        elif (argv[0] == 'NB'):                      #if negative binomial
            if (len(argv) > 3):
                print 'Too many arguments'
            elif (argv[1].isdigit() and argv[2].isdigit()):
                negative_binomial(argv[1], argv[2])
            else:
                print 'Please enter numeric values for r and p'
 
        elif (argv[0] == 'P'):                      #if Poisson 
            print 'P'
            if (len(argv) > 2):
                print 'Too many arguments'
            elif (argv[1].isdigit()):
                poisson(argv[1])
            else:
                print 'Please enter a numeric value for lambda'
 
        else:                                       #invalid letter argument
            print 'Distribution not recognized'
    else:                                           #invalid first argument
        print 'Please enter distribution as first argument'

if (__name__ == "__main__"):
    main(sys.argv[1:])
