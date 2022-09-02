# Open the data file.

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_save, "w") as txt_file:

    file_reader = csv.reader(election_data)

# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.

