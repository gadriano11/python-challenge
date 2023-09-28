# Created by: Gabriel Adriano
# Created for: Monash Bootcamp 2023
# Module 3 Challenge - PyPoll

# import modules

import csv
import os

# set file path

csvpath = os.path.join('Resources', 'election_data.csv')

# open csv file
with open(csvpath, encoding = 'utf') as csvfile:
    # read csv file
    csvreader = csv.reader(csvfile, delimiter = ',')
    # skip header
    header = next(csvreader)

    # compute for total number of votes cast
    total_votes = []
    for row in csvreader:
        total_votes.append(row[2])
    total_vote_count = len(total_votes)

    # create a list of candidates
    candidate_list = []
    existing_candidate = set()
    for name in total_votes:
        if name not in existing_candidate:
            existing_candidate.add(name)
            candidate_list.append(name)

    # candidates votes
    candidate_votes = []
    for candidate in candidate_list:
        candidate_votes.append(total_votes.count(candidate))
    
    # percentage of votes per candidate
    percent_vote = []
    for i in range(len(candidate_list)):
        percent_vote.append(round(((candidate_votes[i]/total_vote_count)*100),3))
    
    # winner
    winning_candidate = candidate_votes.index(max(candidate_votes))
    winner = candidate_list[winning_candidate]

        
# output information
output = f"""
Election Results

-------------------------

Total Votes: {total_vote_count}

-------------------------

"""
for i in range(len(candidate_list)):
    output += f"{candidate_list[i]}: {percent_vote[i]}% ({candidate_votes[i]})\n"
    output += f"\n"
output += f"""
-------------------------

Winner: {winner}

-------------------------

"""

# creates the required directory if it does not exist - ok

output_directory = 'Analysis'
os.makedirs(output_directory, exist_ok=True)

# display to terminal - ok
print(output)

# export to file - ok
csvpath = os.path.join('Analysis', 'Election_Results.txt')
with open(csvpath, 'w') as textfile:
    textfile.write(output)
