import csv
import os

file = 'Resources/budget_data.csv'

#create variables:
#total_months = []        #total of months
net_total = []           # net tota 
changes_pf = []
ave_changes = []
greatest_increase = []
greatest_decrease = []


with open (file) as budgetdata:
    budgetreader = csv.reader(budgetdata,delimiter=",")
    colums =  next(budgetreader)
#    firstrow = next(budgetreader)
    #print(colums)
    #print(firstrow)
#    def total_months():
#        length = len(total_months)
    #total = 0.0
    #for number in numbers:
    #    total += number
#        print (length)
#    total_months
    
    sortedlist = sorted(budgetreader, key=lambda row: row[0], reverse = True)
    a = len(sortedlist)
    print ("Total Months:",a)
#for row in budgetreader:

    
#    total_months = len(colums)
#    print(total_months)

#total_months +=
    for colunm [1]  in budgetreader:
        net_total = 0
        net_total = net_total + colunm [1]
    
    print(net_total)
