# Open the data file.

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

candidate_options = []

candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
        
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

        

for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



# with open(file_to_save, "w") as txt_file:

# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.

