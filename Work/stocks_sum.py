f = open('/users/claudio/Documents/python/dev/practical-python/Work/Data/portfolio.csv', 'rt')
headers = next(f)
total = 0
for line in f:
    row = line.split(',')
    total = total + int(row[1]) * float(row[2])
print('Total cost', total)