# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
#The total number of votes cast


#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.


#%%
import os
import csv

csvpath = os.path.join("C:/Users/17703/Shreya/PyPoll/election_data.csv")

#Initializing Values of the variables and lists
totalVotes = 0
candidates = []
voteCount = []
winnerVoteCount = 0
winner = str

#Reading data from the file election_data.csv
with open(csvpath, 'r', newline='') as csvfile:        
    
    csvreader = csv.reader(csvfile, delimiter=',')
    #Reading header data in csv_header
    csv_header = next(csvreader)

    #Looping through each data record in the file
    for row in csvreader:
        
        #Incrementing vote counter for each record
        totalVotes = totalVotes + 1

        #Creating a list of distinct candidates 
        if(row[2] not in candidates):
            candidates.append(row[2])
            voteCount.append(0)
        
        
        #Getting the Index in candidate list 
        candidateIndex = candidates.index(row[2])
        
        #Using the same Index to increment count of votes for the candidate
        voteCount[candidateIndex] += 1

    #Printing output on console
    print(f"\nElection Results\n-------------------------------------------")
    print(f"Total votes: {totalVotes}")
    print("-------------------------------------------")
    
    for x in range(len(candidates)):
        votePercent = round((voteCount[x]/totalVotes)*100,3)
        print(f"{candidates[x]}: {votePercent}% ({voteCount[x]})")
        
        if (winnerVoteCount<voteCount[x]):
            winnerVoteCount = voteCount[x]
            winner = candidates[x]
    
print("-------------------------------------------")
print(f"Winner: {winner}")
print("-------------------------------------------")

file = open('output.txt','w')

#Writing output to the file    
file.write("Election Results")
file.write("\n-------------------------------------------")
file.write("\nTotal votes:" + str(totalVotes))
file.write("\n-------------------------------------------")
    

file.write("\n" + str(candidates[x]) +" : " + str(votePercent) 
                + "% ("+ str(voteCount[x]) + ")")
file.write("\n-------------------------------------------")
file.write("\nWinner: " + str(winner))
file.write("\n-------------------------------------------")


#%%



#%%



#%%



#%%



#%%



#%%



