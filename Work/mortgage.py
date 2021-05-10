# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
month = 1
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if extra_payment_start_month <= month <= extra_payment_end_month:
        payment = 2684.11 + extra_payment
    else:
        payment = 2684.11
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print(month, round(total_paid, 2), round(principal,2))
    month = month + 1

if principal < 0:
    total_paid = total_paid + principal
print('Total paid', round(total_paid, 2))
print('Months', month - 1)