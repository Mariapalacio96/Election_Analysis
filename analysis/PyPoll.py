#Import the datatime class from the datime module
import datetime as dt

#Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()

#Print the present time
print("The time right now is ", now)

# Open the election results and read the file
file_to_load = 'Resources/election_results.csv'

# Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assing a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the scv file
    for row in file_reader:
        print(row)

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file
    txt_file.write("Counties in the Election\n----------------------------------------\nArapahoe\nDenver\nJefferson")



# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage pf vptes each candidates won 
# 4. The total number of the election based on popular vote
# 5. The winner of the election based on popular vote.


