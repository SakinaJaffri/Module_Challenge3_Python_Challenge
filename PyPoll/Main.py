import csv
import os

# Define file Path:
csv_file = r'Resources\election_data.csv'

# Define PyPoll's variables:
Candidates = {}
my_list =[]
statements = []

# Open and read csv
with open (csv_file, 'r') as f:
    csv_read = csv.reader(f, delimiter = ',')
    next (csv_read)
# to calculate The total number of votes cast   
    for reader in csv_read: 
        if not reader[2] in Candidates.keys():
            Candidates[reader[2]] = 1
        else: 
            Candidates[reader[2]] += 1

    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {sum(Candidates.values())}")
    print("------------------------")


# for calculating The percentage of votes each candidate won & total number of votes each candidate won:

    for num_candidates in Candidates:
        vote_percent = round(Candidates[num_candidates] / sum(Candidates.values()) * 100,3)
        print(f"{num_candidates}: {vote_percent}% ({Candidates[num_candidates]})")
        my_list.append(Candidates[num_candidates])

        statements.append(num_candidates + ":" + str(vote_percent) + "%" + "("+str(Candidates[num_candidates])+")")

    winner_name = list(Candidates.keys())[list(Candidates.values()).index(max(my_list))]


# printing winner name:
print("------------------------")
print(f"Winner: {winner_name}")

print("------------------------")

# Exporting  text file with the analysis/results
with open('Analysis\Election_Results.txt', 'w') as finalf:
    finalf.write("Election Results \n")
    finalf.write("------------------------\n")
    finalf.write(f"Total Votes: {sum(Candidates.values())}\n")
    for i in statements:
        finalf.write(f"{i}\n")

    finalf.write("------------------------\n")
    finalf.write(f"Winner: {winner_name}\n")
    finalf.write("------------------------")
