#import dependencies 
import os
import csv
# import datetime module for methods/functions to format date and time. Use the from so as to
#reference functions without using the dateline dot notation
from datetime import datetime
# Set path for file
csvpath = os.path.join(".", "Resources", "employee_data.csv")
EmpID=[]
SplitNames=[]
SplitNam1=[]
SplitNam2=[]
NewDate=[]
Names=[]
# SSN_Old=[]
SSN_New=[]
States=[]
#Define SSN as string in order to use the python split function. 
SSN=""
#A Python Dictionary to translate US States to Two letter codes
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first (skip this part if there is no header)
    # csv_header = next(csvfile)
    next(csvreader)
    # print(f"Header: {csv_header}")
    for row in csvreader:
    #populate/append elements to EmpID and Names lists 
        EmpID.append(row[0])
        Names.append(row[1])
        # Python do not understand the current date format. It needs to be converted into
        #a datetime object using the strptime() method and set it into a variable called "x"
        x= datetime.strptime(row[2], '%Y-%m-%d')
        # Now that pythonn understand date format, I need to convert it back into a string using the
        #strftime() method and set it to variable y. It does the opposite of what strptime() did. 
        y = datetime.strftime(x, '%m/%d/%Y')
        # append new dates to a list called NewDate
        NewDate.append(y)
        # SSN_Old.append(list(row[3]))
        #Add the SSN row[3] strings to SSN in order to use python split function 
        SSN = row[3]
        #Split full name into first and last name and add each to separate lists
        SplitNames= row[1].split(" ")
        SplitNam1.append(SplitNames[0])
        SplitNam2.append(SplitNames[1])
        # Use the us_state_abbreviation dictionary to look up states in row[4] and append to a list
        z= us_state_abbrev[row[4]]
        States.append(z)
        #define a j variable and split the SSN string and append the result to a new  SSN list 
        j= "***-**-" + SSN.split("-")[2]
        SSN_New.append(j)
        # print(SSN)
    # print(f"Emp ID,First Name,Last Name,DOB,SSN,State")
    # Zipped all lists required in the output 
    Emp_zipped=zip(EmpID, SplitNam1, SplitNam2, NewDate, SSN_New, States)
  # Specify the file to write to
output_path = os.path.join(".", "Analysis", "modemployee_data.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:
    # Initialize csv.writercd ..
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
    csvwriter.writerows(Emp_zipped)
