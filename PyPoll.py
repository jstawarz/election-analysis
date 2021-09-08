# The data we need to retrieve.
#1. The total number of votes cast.
#2. A complete list of candidate who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#. The winner of the election.

#add our dependencies
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Open the election results and read the file
with open(file_to_load) as election_data:
    #Print the file object.
    print(election_data)

    #Create a filename variable to a direct or indirect path to the file
    file_to_save = os.path.join("analysis", "election_analysis.txt")
    #Using the open() fuction with the "w" mode we will write data to the file
    open(file_to_save, "w")

    #Create a filename variable to a direct or indirect path to the file.
    file_to_save = os.path.join("analysis", "election_analysis.txt")

    #Using the with statement open the file as a text file.
    with open(file_to_save, "w") as txt_file:

        #Write three counties to the file.
        txt_file.write("Counties in the Election\n-------------------------\n")
        txt_file.write("Arapahoe\nDenver\nJefferson")

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #to do: read and analyze the data here
    file_reader = csv.reader(election_data)

    #Read and Print the header row in the CSV file.
    headers = next(file_reader)
    print(headers)
    