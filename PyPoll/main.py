# Dependencies
import os
import csv

#specify the file to read 
csvpath = os.path.join('PyPoll/Resources/election_data.csv')

# create txt file to print to
output_path = os.path.join("PyPoll.txt")

#create a dictionary to store candidate votes
candidate_count = {}

#parameters
ballots = []
county = []
candidate = []
Charles_casper_Stockham = []
Diana_DeGette = []
Raymon_Anthony_Doane = []
total_ballots = 0
Stockham_ballot_count = 0
DeGette_ballot_count = 0
Doane_ballot_count = 0

#csv reader specifies delimiter and variable that holds content
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header row first
    csv_header = next(csvreader)

    #read each row of data after the header
    for row in csvreader:

        
        
        #find total votes and print
        total_ballots += 1
        
        if row[2] =="Charles Casper Stockham":
            Stockham_ballot_count += 1
        elif row[2]== "Diana DeGette":
            DeGette_ballot_count += 1
        elif row[2] == "Raymon Anthony Doane":
            Doane_ballot_count += 1


#find canidate % of votes
    Stockham_percent =((Stockham_ballot_count / total_ballots) * 100)
    DeGette_percent = ((DeGette_ballot_count / total_ballots) * 100)
    Doane_percent = ((Doane_ballot_count / total_ballots) * 100)

candidate_count = {"Charles Casper Stockham" : Stockham_ballot_count, "Diana DeGette" : DeGette_ballot_count, "Raymon Anthony Doane" : Doane_ballot_count}

#find winner
# taking list of car values in v
v = list(candidate_count.values())
 
# taking list of car keys in v
k = list(candidate_count.keys())
 
winner = (k[v.index(max(v))])

#generate output
output = (
    f"Election Results\n"
    f"---------------------------------------\n"
    f"Total Votes: {total_ballots} \n"
    f"---------------------------------------\n"
    f"Charles Casper Stockham: {Stockham_percent:.2f}% ({Stockham_ballot_count})\n"
    f"Diana DeGette: {DeGette_percent:.2f}% ({DeGette_ballot_count})\n"
    f"Raymon Anthony Doane: {Doane_percent:.2f}% ({Doane_ballot_count})\n"
    f"---------------------------------------\n"
    f"Winner: {winner} \n"
    f"---------------------------------------\n")
#print the output to terminal
print(output)

file = open("pypoll.txt", "w")
file.write(output)
file.close()