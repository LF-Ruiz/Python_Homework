import csv
import os

file = 'Resources/budget_data.csv'

#create variables:
total_months = 0        
net_total = 0            
increse_months = 0
first_row = 0
starting_point = 0
increase = 0

ave_changes = 0
total_average = 0
dif_value = 0
first_value = 0
greatest_increase = 0
greatest_decrease = 0


with open (file) as budgetdata:
    budgetreader = csv.reader(budgetdata,delimiter=",") #reading file
    next(budgetreader) #get ride of the header
    
    for Budget_row in budgetreader:    #start loop

        #Number of total month
        total_months += 1

        #net total
        net_total += int(Budget_row[1])

        #calculate the increase between months
        increse_months = int(Budget_row[1])
        
        if  first_row == 0:                   #get ride of the first value row (no increase there) and loop through rows  
            starting_point = int(Budget_row[1]) #set the starting point of the increase
            first_row = +1
        else:
            dif_value = (int(Budget_row[1]) - starting_point)
            increase += dif_value
            starting_point = int(Budget_row[1])
            total_average += 1
            
            if first_value == 0:                #get ride of the first value row (no increase there) and loop through rows
                greatest_increase = dif_value
                greatest_decrease = dif_value
                first_value += 1 
            else:
                if dif_value > greatest_increase: #get diferencial of value between months
                    greatest_increase = dif_value # if dif of value is greater than last greater value, then input new value
                    gi_date = Budget_row[0] #get the month the greatest value
                elif dif_value  < greatest_decrease:
                    greatest_decrease = dif_value # if dif of value is less  than last greater decrease, then input new value
                    gd_date = Budget_row[0] #get the month of the minimun value
        
    # average of changes between months    
    if total_average > 0:
        ave_changes = round( (increase / total_average), 2)


    #printing to terminal
        print("Total Months: ", total_months)
        print("Total: $", net_total)
        print("Average Changes: $", ave_changes)
        print("Greatest Increase in Profits: ", gi_date, "($", greatest_increase,")")
        print("Greatest Decrease in Profits: ", gd_date, "($", greatest_decrease,")")

#PyBank_abstract = []
#lines = []
#for line in lines:
Months = ("Total Months:", total_months)
Net =    ("Total: $", net_total)
Average = ("Average Changes: $", ave_changes)
Increse2 = ("Greatest Increase in Profits: ", gi_date, "($", greatest_increase,")")
Decrease2 = ("Greatest Decrease in Profits: ", gd_date, "($", greatest_decrease,")")
#letters = [letter for letter in fish]
#PyBank_abstract = [lines for lines in PyBank_abstract]
#print(PyBank_abstract)
#print(lines)


#output to text file
#cleaned_csv = zip("Pybank solved")
# Set variable for output file
output_file = 'PyBank.txt'

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
#    writer.writerow('PyBank Analysis')
    writer.writerow(Months)
    writer.writerow(Net)
    writer.writerow(Average)
    writer.writerow(Increse2)
    writer.writerow(Decrease2)
   
