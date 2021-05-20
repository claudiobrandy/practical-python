# report.py
#
# Exercise 2.4

import fileparse
import stock

def read_portfolio(filename): 
    with open(filename) as lines:   
        return fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):
    with open(filename) as lines:
        return fileparse.parse_csv(lines, types=[str,float], has_headers=False)

def make_report(stocks, prices):
    lines = []
    for st in stocks:
        ln = (st.name, st.shares, prices[st.name], prices[st.name] - st.price)
        lines.append(ln)
    return lines

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')
    for name, shares, price, change in report:
        pric = '$' + str(price)
        print(f'{name:>10s} {shares:>10d} {pric:>10s} {change:>10.2f}')
    return

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, dict(prices))
    print_report(report)
    return

def main(args):
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} ' 'portfile pricefile')    
    else:
        portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
    return

if __name__ == '__main__':
    import sys
    main(sys.argv)