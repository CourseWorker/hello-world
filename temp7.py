# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 16:27:30 2015

@author: HenryII
"""
# test case one
balance = 3329
annualInterestRate = 0.2
#test case two
balance = 4773
annualInterestRate = 0.2
#test case three
balance = 3926
annualInterestRate = 0.2
       
# initialise variables
monthlyInterestRate = annualInterestRate / 12.0
previousBalance = balance
minimumMonthlyPayment = 10

# calculate lowsest payment
while True: 
    for month in range(1,13):
        previousBalance -= minimumMonthlyPayment
        previousBalance += monthlyInterestRate * previousBalance 
    if previousBalance <= 0:
        break
    else:
        previousBalance = balance
        minimumMonthlyPayment += 10
        
print "Lowest Payment: %.2f" % minimumMonthlyPayment