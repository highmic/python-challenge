import os
import csv
# Set path for file
csvpath = os.path.join(".", "Resources", "election_data.csv")
#Create list and variables 
#Canlist is the list of candidates list populated with row 2
#Unique_Can is the list of unique candidates name from Canlist
#Vote_Tally is the count of how many times a name appears in the Canlist which is the total votes per candidate
#PerVote is the list of percentages of votes of each candidate 
Canlist=[]
Unique_Can=[]
Vote_Tally=[]
PerVote=[]
# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first (skip this part if there is no header)
    # csv_header = next(csvfile)
    next(csvreader)
    # print(f"Header: {csv_header}")
    print("Election Results")
    print("---------------------")
    totalvotes=0
    for row in csvreader:
    #total votes is the no of line items in the file, assuming no null value:
        totalvotes = totalvotes + 1
    #append candidates to candidates list
        Canlist.append(row[2])
    #Create a loop through the candidate list and set 
    #variables i,j and k to assign votes count to unique candidates 
    # map variables to candidates and vote-tally 
    for i in set(Canlist):
        Unique_Can.append(i)
        j = Canlist.count(i)
        Vote_Tally.append(j)
        k=((Canlist.count(i)/totalvotes))*100
        PerVote.append(k)
    # Create a loop through Unique_Can list to print and map candidates name with votes and % votes
    # to ensure precison to 3 decimal places for % vote set to :.3f 
    print(f"Total Votes: {totalvotes}")
    print("-----------------------")
    for i in range(len(Unique_Can)):
        print(f"{Unique_Can[i]} :{PerVote[i]:.3f}% ({Vote_Tally[i]})")
    print("----------------------")
    #Use the zip function to pair Unique_Can list with Vote_Tally list, a 2 input iterables
    #the result is an iterator of tuples with 2 elements each
    zipped=zip(Unique_Can,Vote_Tally)
    # Build a dictionary of the zipped iterators with the dict function. The elements of Unique_Can
    # becomes the dictionary keys and elements of Vote_Tally as the values 
    dict_winner=dict(zipped)
    # To print winner name use the dict name key with the get function while max ensures the name is the highest votes
    print(f"Winner: {(max(dict_winner, key=dict_winner.get))}")
    print("----------------------")
    # Use the same arguments as the print to write output to text file
    output_path = os.path.join(".", "Analysis", "PyPoll.txt")
    # output_path = os.path.join(".", "Analysis", "Pypoll.txt")
    with open(output_path, 'w') as txtfile:
        txtfile.write("-----------------------\n")
        txtfile.write(f"Election Results\n")
        txtfile.write("-----------------------\n")
        txtfile.write(f"Total Votes:{totalvotes}\n")
        txtfile.write("-----------------------\n")
        for i in range(len(Unique_Can)):
            txtfile.write(f"{Unique_Can[i]} :{PerVote[i]:.3f}% ({Vote_Tally[i]})\n")
        txtfile.write("------------------------\n")
        txtfile.write(f"Winner: {(max(dict_winner, key=dict_winner.get))}\n")
        txtfile.write("------------------------\n")