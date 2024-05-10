# PyPoll

import csv
import os

CSV_PATH = "Resources/election_data.csv"

total_votes = 0
candidates = []
candidate_votes = {}

# Open the CSV using the UTF-8 encoding
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        # total number of votes
        total_votes += 1

        current_candidate = row[2]

        # list of candidates
        if current_candidate not in candidates:
            candidates.append(current_candidate)

        # number of votes/candidate
        if current_candidate in candidate_votes.keys():
            candidate_votes[current_candidate] +=1
        else:
            candidate_votes[current_candidate] = 1

    # winner (learned from Xpert)
    max_key = max(candidate_votes, key=lambda k: candidate_votes[k])
    max_votes = max(candidate_votes.values())

    # percentage of votes/candidate + analysis
    print("Election Results \n ---------------")
    print(f"Total number of votes: {total_votes} \n ---------------")            
    for current_candidate in candidate_votes:
        perc_num = candidate_votes[current_candidate] / total_votes
        perc_votes = "{:.3%}".format(perc_num)
        print("{}: {} ({})".format(current_candidate, perc_votes, candidate_votes[current_candidate]))
    print(f"--------------- \nWinner: {max_key} \n ---------------")



    analysis = f"""Election Results 
    ---------------
    Total number of votes: 369711
    ---------------
    Charles Casper Stockham: 23.049% (85213)
    Diana DeGette: 73.812% (272892)
    Raymon Anthony Doane: 3.139% (11606)
    ---------------
    Winner: Diana DeGette
    ---------------"""

with(open("PyPoll.main.txt", "w") as f):
    f.write(analysis)