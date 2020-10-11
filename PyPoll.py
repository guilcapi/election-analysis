#The data we need to retrieve.
#1. The total number of votes cast.
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.

#Import datetime class from datetime module
# import datetime as dt
# #Use now() attribute on datetime class to get present time
# now =dt.datetime.now()
# print(f"The time right now is {now}")
# print("The time right now is", now)

# import csv
# print(dir(csv))
# print("")
# print(dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}))
# print("")
# print(dir(str))

# import random
#import numpy

#import csv

#variable wit file location
##file_to_load = 'Resources/election_results.csv'

##Open the election results and read the file
#election_data = open(file_to_load, 'r')

##To do: perform analysis

##Close the file
#election_data.close()

#Open the election results and read the file
#with open(file_to_load) as election_data:

    ##To do: perform analysis
    #print(election_data)

# import csv
# import os

# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources","election_results.csv")

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     #Print file object
#     print(election_data)

# #Create a filename variable to a direct or indirect path
# file_to_save = os.path.join("analysis","election_analysis.txt")
# #Using open() function with "w" mode to write data
# #outfile = open(file_to_save, "w")
# with open(file_to_save, "w") as txt_file:

#     #Write data to file
#     #txt_file.write("Hello World!")
#     #txt_file.write("Arapahoe\nDenver\nJefferson")
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("-------------------------\n")
#     txt_file.write("Arapahoe\n")
#     txt_file.write("Denver\n")
#     txt_file.write("Jefferson")

# #Close the file
# #outfile.close()

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize total vote counter.
total_votes = 0

#Candidate Options
candidate_options = []

#Candidate individual total votes empty dictionary
candidate_votes = {}

#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)
    #print(headers)

    #Print each row in CSV file
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1

        #Print the candidate name for each row
        candidate_name = row [2]

        #If candidate name does not match any existing candidate, then add it to the list
        if candidate_name not in candidate_options:

            #Add candidate name to candidate list.
            candidate_options.append(candidate_name)

            #Begin tracking candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Determine percentage of votes for each candidate by looping through the counts.
#Iterate through the candidate list.
for candidate_name in candidate_votes:
    #Retrieve vote count of each candidate.
    votes = candidate_votes[candidate_name]

    #Calculate percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #To do: print out each candidate's name, vote count, and percentage of votes.
    #Print candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true, set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #set winning candidate equal to the candidate's name.
        winning_candidate  = candidate_name

#To do: print out winning candidate, vote count, and percentage.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)

#3. Print the total votes.
#print(total_votes)

#Print the candidate list.
#print(candidate_options)

#Print candidate vote dictionary.
#print(candidate_votes)





