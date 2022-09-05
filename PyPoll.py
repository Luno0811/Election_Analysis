# Open the data file.

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

file_to_save = os.path.join("analysis", "election_analysis.txt")

# with open(file_to_save, "w") as txt_file:

# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.

