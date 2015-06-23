# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:59:57 2015

@author: HenryII
"""
# test case one
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#test case two
balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# initialise variables
monthlyInterestRate = annualInterestRate / 12.0
previousBalance = balance
totalPaid = 0
# calculate monthly payments
for month in range(1,13):
    minimumMonthlyPayment = monthlyPaymentRate * previousBalance 
    totalPaid += minimumMonthlyPayment
    previousBalance -= minimumMonthlyPayment
    previousBalance += monthlyInterestRate * previousBalance
    # display monthly payments    
    print "Month: %d" % month
    print "Minimum monthly payment: %.2f" % minimumMonthlyPayment
    print "Remaining balance: %.2f" % previousBalance
    
print "Total paid: %.2f" % totalPaid
print "Remaining balance: %.2f" % previousBalance