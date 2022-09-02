# Open the data file.

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)


# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.

