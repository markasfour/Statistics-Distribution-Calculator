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
    return float(math.factorial(n) / math.factorial(r) / math.factorial(n-r))

def bin_calc(n, p, x):                              #binomial calculation
    return nCr(n, x) * (p ** x) * ((1 - p) ** (n - x))

def hg_calc(n, M, N, x):                            #hyper geometric calculation
    return (nCr(M, x) * nCr((N - M), (n - x))) / nCr(N, n)

def nb_calc(r, p, x):                               #negative binomial calculation
    return nCr((x + r - 1), (r - 1)) * (p ** r) * ((1 - p) ** x)

def p_calc(y, x):                                   #Poisson calculation
    return (math.exp(-y) * (y ** x)) / math.factorial(x)

def binomial(argv):
    n = float(argv[0])
    p = float(argv[1])
    calculate = False
    if (len(argv) == 3):
        if (isnumber(argv[2])):
            x = float(argv[2])
            calculate = True
        else:
            print 'Please enter numeric value for x'
    print 'X~B(', n, ', ', p, ')'
    expected = n * p
    print 'E(X) = ', expected
    variance = n * p * (1 - p)
    print 'V(X) = ', variance
    sd = math.sqrt(variance)
    print 'SD(X) = ', sd
    
    if (calculate):
        ans = 0.0
        ans_LE = 0.0
        ans_L = 0.0
        ans_GE = 0.0
        ans_G = 0.0

        ans = bin_calc(n, p, x)        
        print 'P(X =', x, ') =', ans                #P(X = x)
        
        if (x <= n / 2):
            for i in range (0, int(x) + 1):
                ans_LE += bin_calc(n, p, i)
        else:
            for i in range (int(x) + 1, int(n) + 1):
                ans_LE += bin_calc(n, p, i)
                ans_LE = 1 - ans
        print 'P(X <=', x, ') =', ans_LE            #P(X <= x)

        if (x <= n / 2):
            for i in range (0, int(x)):
                ans_L += bin_calc(n, p, i)
        else:
            for i in range (int(x), int(n) + 1):
                ans_L += bin_calc(n, p, i)
                ans_L = 1 - ans
        print 'P(X <', x, ') =', ans_L              #P(X < x)

        ans_GE = 1 - ans_L
        print 'P(X >=', x, ') =', ans_GE            #P(X >= x)

        ans_G = 1 - ans_LE
        print 'P(X >', x, ') =', ans_G              #P(X > x)

def hyper_geometric(argv):
    n = float(argv[0])
    M = float(argv[1])
    N = float(argv[2])
    calculate = False
    if (len(argv) == 4):
        if (isnumber(argv[3])):
            x = float(argv[3])
            calculate = True
        else:
            print 'Please enter numeric value for x'
    print 'X~H(', n, ', ', M, ', ', N, ')'
    expected = n * (M / N) 
    print 'E(X) = ', expected
    variance = ((n * M) / N) * (1 - (M / N)) * ((N - n) / (N - 1))
    print 'V(X) = ', variance
    sd = math.sqrt(variance)
    print 'SD(X) = ', sd
    
    if (calculate):
        ans = 0.0
        ans_LE = 0.0
        ans_L = 0.0
        ans_GE = 0.0
        ans_G = 0.0

        ans = hg_calc(n, M, N, x)        
        print 'P(X =', x, ') =', ans                #P(X = x)
        
        if (x <= n / 2):
            for i in range (0, int(x) + 1):
                ans_LE += hg_calc(n, M, N, i)
        else:
            for i in range (int(x) + 1, int(n) + 1):
                ans_LE += hg_calc(n, M, N, i)
                ans_LE = 1 - ans
        print 'P(X <=', x, ') =', ans_LE            #P(X <= x)

        if (x <= n / 2):
            for i in range (0, int(x)):
                ans_L += hg_calc(n, M, N, i)
        else:
            for i in range (int(x), int(n) + 1):
                ans_L += hg_calc(n, M, N, i)
                ans_L = 1 - ans
        print 'P(X <', x, ') =', ans_L              #P(X < x)

        ans_GE = 1 - ans_L
        print 'P(X >=', x, ') =', ans_GE            #P(X >= x)

        ans_G = 1 - ans_LE
        print 'P(X >', x, ') =', ans_G              #P(X > x)

def negative_binomial(argv):
    r = float(argv[0])
    p = float(argv[1])
    calculate = False
    calculate2 = False
    if (len(argv) == 3 or len(argv) == 4):
        if (isnumber(argv[2])):
            x = float(argv[2])
            calculate = True
        else:
            print 'Please enter numeric value for x'
    print 'X~NB(', r, ', ', p, ')'
    expected = (r * (1 - p)) / p
    print 'E(X) = ', expected
    variance = expected / p
    print 'V(X) = ', variance
    sd = math.sqrt(variance)
    print 'SD(X) = ', sd

    if (calculate):
        ans = nb_calc(r, p, x)
        print 'P(X =', x, ') =', ans 
        if (len(argv) == 4):
            ans_LE = 0.0
            ans_L = 0.0
            ans_GE = 0.0
            ans_G = 0.0
            if (isnumber(argv[3])):
                n = float(argv[3])
                calculate2 = True
            else:
                print 'Please enter numeric value for n'
            if (calculate2):
                if (x <= n / 2):
                    for i in range (0, int(x) + 1):
                        ans_LE += nb_calc(r, p, i)
                else:
                    for i in range (int(x) + 1, int(n) + 1):
                        ans_LE += nb_calc(r, p, i)
                        ans_LE = 1 - ans
                print 'P(X <=', x, ') =', ans_LE            #P(X <= x)

                if (x <= n / 2):
                    for i in range (0, int(x)):
                        ans_L += nb_calc(r, p, i)
                else:
                    for i in range (int(x), int(n) + 1):
                        ans_L += nb_calc(r, p, i)
                        ans_L = 1 - ans
                print 'P(X <', x, ') =', ans_L              #P(X < x)

                ans_GE = 1 - ans_L
                print 'P(X >=', x, ') =', ans_GE            #P(X >= x)

                ans_G = 1 - ans_LE
                print 'P(X >', x, ') =', ans_G              #P(X > x)


def poisson(argv):
    y = float(argv[0])
    calculate = False
    calculate2 = False
    if (len(argv) == 2 or len(argv) == 3):
        if (isnumber(argv[1])):
            x = float(argv[1])
            calculate = True
        else:
            print 'Please enter numeric value for x'
    print 'X~P(', y, ')'
    expected = y
    print 'E(X) = ', expected
    variance = y
    print 'V(X) = ', variance
    sd = math.sqrt(variance)
    print 'SD(X) = ', sd
    if (calculate):
        ans = p_calc(y, x) 
        print 'P(X =', x, ') =', ans 
        if (len(argv) == 3):
            ans_LE = 0.0
            ans_L = 0.0
            ans_GE = 0.0
            ans_G = 0.0
            if (isnumber(argv[2])):
                n = float(argv[2])
                calculate2 = True
            else:
                print 'Please enter numeric value for n'
            if (calculate2):
                if (x <= n / 2):
                    for i in range (0, int(x) + 1):
                        ans_LE += p_calc(y, i)
                else:
                    for i in range (int(x) + 1, int(n) + 1):
                        ans_LE += p_calc(y, i)
                        ans_LE = 1 - ans
                print 'P(X <=', x, ') =', ans_LE            #P(X <= x)

                if (x <= n / 2):
                    for i in range (0, int(x)):
                        ans_L += p_calc(y, i)
                else:
                    for i in range (int(x), int(n) + 1):
                        ans_L += p_calc(y, i)
                        ans_L = 1 - ans
                print 'P(X <', x, ') =', ans_L              #P(X < x)

                ans_GE = 1 - ans_L
                print 'P(X >=', x, ') =', ans_GE            #P(X >= x)

                ans_G = 1 - ans_LE
                print 'P(X >', x, ') =', ans_G              #P(X > x)


def main(argv):
    if (argv[0].isalpha()):                         #check if first arg is a letter
        argv[0] = argv[0].upper()                   #convert to uppercase
        
        if (argv[0] == 'B'):                        #if binomial
            if (len(argv) > 4 or len(argv) < 3):
                print 'Invalid number of arguments'
            elif (isnumber(argv[1]) and isnumber(argv[2])):
                binomial(argv[1:])
            else:
                print 'Please enter numeric values for n and p'
        
        elif (argv[0] == 'H'):                      #if hyper geometric
            if (len(argv) > 5 or len(argv) < 4):
                print 'Invalid number of arguments'
            elif (isnumber(argv[1]) and isnumber(argv[2]) and isnumber(argv[3])):
                hyper_geometric(argv[1:])
            else:
                print 'Please enter numeric values for n, M, and N'

        elif (argv[0] == 'NB'):                      #if negative binomial
            if (len(argv) > 5 or len(argv) < 3):
                print 'Invalid number of arguments'
            elif (isnumber(argv[1]) and isnumber(argv[2])):
                negative_binomial(argv[1:])
            else:
                print 'Please enter numeric values for r and p'
 
        elif (argv[0] == 'P'):                      #if Poisson 
            print 'P'
            if (len(argv) > 4 or len(argv) < 2):
                print 'Invalid number of arguments'
            elif (isnumber(argv[1])):
                poisson(argv[1:])
            else:
                print 'Please enter a numeric value for lambda'
 
        else:                                       #invalid letter argument
            print 'Distribution not recognized'
    else:                                           #invalid first argument
        print 'Please enter distribution as first argument'

if (__name__ == "__main__"):
    main(sys.argv[1:])
