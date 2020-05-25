# python-challenge
Week 3 homework  solution repository 

PyBank:
•  In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
•  Your task is to create a Python script that analyzes the records to calculate each of the following:
•	The total number of months included in the dataset
•	The net total amount of "Profit/Losses" over the entire period
•	The average of the changes in "Profit/Losses" over the entire period
•	The greatest increase in profits (date and amount) over the entire period
•	The greatest decrease in losses (date and amount) over the entire period
•  As an example, your analysis should look similar to the one below:
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
•  In addition, your final script should both print the analysis to the terminal and export a text file with the results.


My PyBank Script Key Takeaways:
•	For the calculated values, I created a “For loop” using nested “range” and “len” function over revenue whereby looping decreases by 1 step. To calculate the average changes in “Profit/loses” over the entire period, the  ith revenue was subtracted from (i+1) revenue as follows: Rev(i+1) – Rev (i). 
•	To find the corresponding months for the calculated values, I used the Python index function
•	To ensure error free printing with decimal precision. I used f strings with curly brackets for calculated values and :.2f to get average into 2 decimal
•	Printing to terminal and writing to text file output followed the sane format. 




PyPoll:

•  In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
•  You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
•	The total number of votes cast
•	A complete list of candidates who received votes
•	The percentage of votes each candidate won
•	The total number of votes each candidate won
•	The winner of the election based on popular vote.
•  As an example, your analysis should look similar to the one below:
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
•  In addition, your final script should both print the analysis to the terminal and export a text file with the results.


My PyPoll Script Key Takeaways:
•	To get votes assigned to unique candidates, I created a “for loop” through the candidates lists and map variables to candidates and their unique vote tally
•	To print unique candidate name and their corresponding %vote and tally. I created a “for loop” with a nested “range” and “len” function over the Unique candidates list
•	To get the winner, I used the “zip” function to pair Unique candidate list with their vote tally, a 2 inputs iterables. The result is an interator of tuples with 2 elements each. I then defined a dictionary of zipped iterator with the “dict” function. The elements of the Unique candidate lists becomes the keys while the elements of the Vote Tally lits are the values. Finally, I used the “get” method to the get the value of the dictionary key for the winner.
•	Printing to terminal and writing to output text file followed the same format with f string and curly brackets together with decimal precision. 




PyBoss Challenge 

In this challenge, you get to be the boss. You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.
Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:
•	Import the employee_data.csv file, which currently holds employee records like the below:
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
•	Then convert and export the data to use the following format instead:
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA
•	In summary, the required conversions are as follows:
o	The Name column should be split into separate First Name and Last Name columns.
o	The DOB data should be re-written into MM/DD/YYYY format.
o	The SSN data should be re-written such that the first five numbers are hidden from view.
o	The State data should be re-written as simple two-letter abbreviations.
•	Special Hint: You may find this link to be helpful—Python Dictionary for State Abbreviations.


My PyPoll Script Key Takeaways:
•	To get through with date formatting, I imported the datetime module. I used the “from datetime import datetime” convention instead of “import datetime” to be able to reference functions without using the datetime dot notation
•	Convert SSN to a string to enable the use of “split” function
•	Used the python US states abbreviation dictionary
•	Convert date format in the file to datetime format first, then convert to format required in the output
•	Finally zipped all individual lists and write the zipped into the output.  
