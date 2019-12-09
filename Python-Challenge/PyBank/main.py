# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
# Import the necessary dependencies for os.path.join()
# Import necessary dependencies import csv 
 

import os
import csv 
 
# Track parameters

total = 0
totalmonths = 0
previous = 0
change = 0
Rev_change =[]
average_change = 0
greatest_increase = 0
greatest_decrease = 999999999


# Read in a .csv file 

csvpath = os.path.join("C:/Github/Shreya/Python/PyBank/PyBank_data.csv")


# Open the csv file and read:
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')     
    csv_header=next(csvfile)
    type(csvreader)     


    for row in csvreader:

        # track the total months
        totalmonths = totalmonths + 1

        # track the total 
        total = total + (int(row[1]))


        # track the change between two months
        change = int(row[1]) - previous
        previous = int(row[1])
        
        #add changes in new list
        Rev_change.append(change)
        
        # Calculate the Average Revenue Change
        average_change = round(sum(Rev_change)/totalmonths)


        #find the greatest increase in revenue
        if (change > greatest_increase):
            highest_Inc_Month = row[0]
            highest_Inc_Rev = change 

        #find the greatest decrease in revenue
        if (change < greatest_decrease):
            lowest_Dec_Month = row[0]
            lowest_Dec_Rev = change

#create varible to hold finanical analysis results and use f-strings for formatting
Results = (
f"Financial Analysis \n"
f"---------------------------- \n"
f"Total Months: {totalmonths} \n"
f"Total Revenue: ${total} \n"
f"Average Revenue Change: ${average_change} \n"
f"Greatest Increase in Revenue: {highest_Inc_Month} (${highest_Inc_Rev}) \n"
f"Greatest Decrease in Revenue: {lowest_Dec_Month} (${lowest_Dec_Rev}) \n")
print(Results)

#write a text file in order to export results to text file

output_txt = os.path.join("C:/Users/17703/Shreya/PyBank/Py_Bank.txt")

with open(output_txt, 'w') as txtfile:
    txt_writer = txtfile.write(Results)


#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



