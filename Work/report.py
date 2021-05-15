# report.py
#
# Exercise 2.4
import csv
import fileparse

def read_portfolio(filename):    
    # portfolio = []
    # with open(filename) as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)
    #     for n_row, row in enumerate(rows):        
    #         record = dict(zip(headers, row))
    #         try:
    #             name = record['name']
    #             nshares = int(record['shares'])
    #             price = float(record['price'])
    #             holding = {'name': name, 'shares': nshares, 'price': price}
    #             portfolio.append(holding)
    #         except ValueError:
    #             print(f'Row {n_row}: Bad row: {row}')
    return fileparse.parse_csv(filename, types=[str, int, float])

def read_prices(filename):
    # prices = {}
    # with open(filename) as f:
    #     rows = csv.reader(f)
    #     for row in rows:
    #         try:
    #             prices[row[0]] = float(row[1])
    #         except IndexError:
    #             pass
    return fileparse.parse_csv(filename, types=[str, float], has_headers=False)

def make_report(stocks, prices):
    lines = []
    for st in stocks:
        ln = (st['name'], st['shares'], prices[st['name']], prices[st['name']] - st['price'])
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

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')