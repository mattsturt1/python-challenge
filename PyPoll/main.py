
# Modules
from pathlib import Path
import csv
import os

# Set path for file
csvpath = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")
print(csvpath)



# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    total_votes = 0
    data = list(csvreader)
    total_votes = len(data)
    



    votes_for_charles = []
    votes_for_diana = []
    votes_for_raymond = []
    for d in data:
        if d[2] == "Charles Casper Stockham":
            votes_for_charles.append(d)
        elif d[2] == "Diana DeGette":
            votes_for_diana.append(d)
        elif d[2] == "Raymon Anthony Doane":
            votes_for_raymond.append(d)

vote_count_charles = len(votes_for_charles)
vote_count_diana = len(votes_for_diana)
vote_count_raymond = len(votes_for_raymond)

winner = ""
if vote_count_raymond > vote_count_charles and vote_count_raymond > vote_count_diana:
    winner = "Raymon Anthony Doane"
elif vote_count_diana > vote_count_charles and vote_count_diana > vote_count_raymond:
    winner = "Diana DeGette"
elif vote_count_charles > vote_count_diana and vote_count_charles > vote_count_raymond:
    winner = "Charles Casper Stockham"

charles_percent = (vote_count_charles / total_votes) * 100
diana_percent = (vote_count_diana / total_votes) * 100
raymond_percent = (vote_count_raymond / total_votes) * 100

charles_percent_rounded = round(charles_percent, 3)
diana_percent_rounded = round(diana_percent, 3)
raymond_percent_rounded = round(raymond_percent, 3)


print("Election Results")

print("_________________________")


print(f"Charles Casper Stockham : {charles_percent_rounded}% ({vote_count_charles})")
print(f"Diana DeGette : {diana_percent_rounded}% ({vote_count_diana}) ")
print(f"Raymon Anthony Doane : {raymond_percent_rounded}% ({vote_count_raymond}) ")

print("_________________________")

print(f"Winner : {winner}")


# Specify the file to write to
output_path = os.path.join(os.path.dirname(__file__), 'analysis', 'election_analysis.txt')
# Open the file using “write” mode. Specify the variable to hold the contents
with open(output_path, 'w') as textfile:
    # Initialize csv.writer
    # Write the first row (column headers)
    textfile.write(f'Election Results\n')
    textfile.write(f'-------------------------\n')
    
    textfile.write(f"-------------------------\n")
    textfile.write("Election Results")
    textfile.write("_________________________")
    textfile.write(f'Total Votes:  {total_votes}\n')
    textfile.write(f"Charles Casper Stockham : {charles_percent_rounded}% ({vote_count_charles})\n")
    textfile.write(f"Diana DeGette : {diana_percent_rounded}% ({vote_count_diana})\n ")
    textfile.write(f"Raymon Anthony Doane : {raymond_percent_rounded}% ({vote_count_raymond})\n ")
    textfile.write("_________________________\n")
    textfile.write(f"Winner : {winner}\n")




