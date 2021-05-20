# pcost.py
#
# Exercise 1.27

import sys
from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    total = 0.0

    for row in portfolio:
        total += row.shares * row.price
    return total    

def main(args):
    if len(args) == 2:
        filename = args[1]
    else:
        filename = 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    print('Total cost', cost)
    return

if __name__ == '__main__':
    import sys
    main(sys.argv)