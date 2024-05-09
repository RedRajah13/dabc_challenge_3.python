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

    # percentage of votes/candidate
    for key in candidate_votes:
        perc_votes = total_votes / candidate_votes[current_candidate]
        print(perc_votes)

# winner

    print("Election Results \n ---------------")
    print(f"Total number of votes: {total_votes} \n ---------------")            
    for current_candidate in candidate_votes:
        print("{} = {}".format(current_candidate, candidate_votes[current_candidate]))
  
