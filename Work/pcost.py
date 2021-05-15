# pcost.py
#
# Exercise 1.27

import csv
import sys
from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    total = 0.0

    for row in portfolio:
        total += row['shares'] * row['price']
    return total    

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost', cost)