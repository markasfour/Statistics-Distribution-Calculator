# Statistics-Distribution-Calculator
Binomial, Hyper Geometric, Negative Binomial, and Poisson Distribution Calculator

## Instructions
To use this statistics distribution calculate you must have Python version 2.7.9 or later.

To use the binomial distribution calculator, enter the flags `b` or `B`, the number of independent trials `n`, the probability of success `p`, and optionally the number of successes in the `n` trials `x`.
Example command line:
	python main.py b 25 .05 3

To use the hyper geometric distribution calculator, enter the flags `h` or `H`, the sample size `n`, the number of successes `M`, the finite population size `N`, and optionally the number of success in the sample `x`.
Example command line:
	python main.py h 10 8 20 2

To use the negative binomial distribution calculator, enter the flags `nb` or `NB`, the number of successes `r`, the probability of success `p`, optionally the number of failures, and optionally the total number of trials `n`.
Example command line:
	python main.py nb 1 .2 2 3

To use the Poisson distribution calculator, enter the flags `p` or `P`, the parameter `lambda`, and optionally the number of successes `x`.
Example command line:
	python main.py p 2.4 4

## Features
* Returns expected value `E(X)`
* Returns variance `V(X)`
* Returns standard deviation `SD(X)`
* If applicable, returns `P(X = x)`
* If applicable, returns `P(X <= x)`
* If applicable, returns `P(X < x)`
* If applicable, returns `P(X >= x)`
* If applicable, returns `P(X > x)`

