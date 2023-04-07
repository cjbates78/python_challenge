# Dependencies
import os
import csv

#specify the file to read 
csvpath = os.path.join("election_data.csv")


#csv reader specifies delimiter and variable that holds content
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

 #read the header row first
    csv_header = next(csvreader)
#Print Header
    print("Election Results")
    print("-------------------------------------------------------")

#set inital value of counter to zero
    rowcount = sum(1 for row in csvreader)


#find total votes and print
    total_votes = rowcount
    print("Total Votes: " + total_votes)
    print("-------------------------------------------------------")

#Loop thru and find canidates and count votes
   
canidate_votes = [2] in csvreader
Stockham_votes = []
DeGette_votes = []
Doane_votes = []
for votes in canidate_votes:
    if canidate_votes =="Charles Casper Stockham":
        Stockham_votes.append (+1)
    elif canidate_votes =="Diana DeGette":
        DeGette_votes.append (+1)
    elif canidate_votes == "Raymon Anthony Doane":
        Doane_votes.append (+1)


#find canidate % of votes
Stockham_percent = ((Stockham_votes / total_votes) * 100)
DeGette_percent = ((DeGette_votes / total_votes) * 100)
Doane_percent = ((Doane_votes / total_votes) * 100)


# print name: percent (total) x 3
print("Charles Casper Stockham:" + Stockham_percent + "(" + Stockham_votes + ")")
print("Diana DeGette:" + DeGette_percent + "(" + DeGette_votes +")")
print("Raymon Anthony Doane: " + Doane_percent + "(" + Doane_votes + ")")
print("-------------------------------------------------------")

#find winner
winner = max(canidate_votes)
#print "Winner: " name
print("-------------------------------------------------------")

# create txt file to print to
output_path = os.path.join("PyPoll.txt")
file = open("PyPoll.txt", "w")
file.close()