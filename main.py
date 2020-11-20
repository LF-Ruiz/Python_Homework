import csv
import os

election_data  = 'Resources\election_data.csv'
#output = 'PyPoll.txt'

# Define the function and have it accept the 'results' as its sole parameter
#        def percentages(results):
    # For readability, it can help to assign your values to variables with descriptive names
#            voter_id = int(results[0])
#            county = str(results[1])
#            candidate = list(results[2])


#Create variables
total_votes = 0
candidates = {}
percentages = {}
votes_percent = 0
first_value = 0
winner = 0
winner_name = ""
results = ""
Header = "Election Results"
Separation = "------------------"

with open (election_data) as data:
    data_reader = csv.reader(data, delimiter= ",")
    next(data_reader)

    for row in data_reader:
        total_votes += 1
        if row[2] in candidates: 
            candidates[row[2]] = candidates[row[2]] + 1
        else:
            candidates[row[2]] = 1
    votes_count = "Total Votes: " + str(total_votes)
    print(Header)
    print(Separation)
    print(votes_count)
    print(Separation)
    for key in candidates:
        if candidates[key] not in percentages:
            percentages[key] = round(((candidates[key] / total_votes) * 100), 3)
    
#        percentage1 = round(("candidate / total_votes),2
#        if row[2] 
#            candidates = [name=row[2], votes+=1]
        #candidates si el valor no esta repetido me lo integre en la lista
#        pypoll_dict[voting_data[0]] = voting_data[2]

    with open("PyPoll.txt","w") as output:
        output.write(Header)
        output.write("\n")
        output.write(Separation)
        output.write("\n")
        output.write(votes_count)
        output.write("\n")
        output.write(Separation)
        output.write("\n")


        for key in candidates:
            print(key, percentages[key],"% (",candidates[key], ")"  )
            if first_value == 0:
                winner = candidates[key]
                winner_name = key
                first_value += 1
            else:
                if candidates[key] > winner:
                    winner = candidates[key]
                    winner_name = key  
        
            result = key + " " + str(percentages[key]) + "% (" + str(candidates[key]) + ")"
            output.write(result)
            output.write("\n")   
        winner_print = "Winner: " + winner_name
        print(Separation)
        print(winner_print)
        output.write(Separation)
        output.write("\n")
        output.write(winner_print)
        output.write("\n")

            


    # votes percent can be found by dividing the the votes for a candidate  by the total votes and multiplying by 100
#            votes_percent = (candidate / total_votes) * 100


#print(total_votes)
#print(candidates)
#print(percentages)  