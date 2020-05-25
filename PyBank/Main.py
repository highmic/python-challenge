#import dependencies
import os
import csv
# Set path for file
csvpath = os.path.join(".", "Resources", "budget_data.csv")
# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first (skip this part if there is no header)
    # csv_header = next(csvfile)
    next(csvreader)
    # print(f"Header: {csv_header}")
    #Define empty lists and append calculated variables into lists
    Revenue=[]
    RevChange = []
    MonthlyChange=[]
    Months=[]
    # Set initial values for calculated variables 
    GreatRev_Inc=0
    GreatRev_Dec=0
    Average_Change=0
    total=0
    months=0
    # Read through each row of data after the header
    for row in csvreader:
        #calculate total profit/loss by adding values in row[1]
        total=total+int(row[1])
        months=months+1
        Months.append(row[0])
        Revenue.append(int(row[1]))
    #Create "for loop" to loop through Revenue range and each time decreses by 1 step...
    for i in range(len(Revenue)-1):
        # j is the change in revenue, which is ith revenue subtract from next revenue
        j=Revenue[i+1]-Revenue[i]
        # append j to MonthlyChange list
        MonthlyChange.append(j)
        #calculate the average of the changes in revenue with sum of all values in the
        #MonthlyChange list divided by the count using the python len function
        Average_Change=sum(MonthlyChange)/len(MonthlyChange)
        #Find the greatest increase/decrease in revenue increase with the python max/min function
        #find the corressponding index position of the greatest inc/dec using python index function
        GreatRev_Inc=max(MonthlyChange)
        k=MonthlyChange.index(GreatRev_Inc) + 1
        GreatRev_Dec=min(MonthlyChange)
        l=MonthlyChange.index(GreatRev_Dec) + 1
    # print results by using the print f strings and curly brackets to prevent concatenation errors
    # use the .2f to esnure avergae printed pricely to 2 decimal places as shown in the instructions 
    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${str(total)}")
    print(f"Average Change:${Average_Change:.2f}")
    print(f"Greatest Increase in Profits:{Months[k]} (${GreatRev_Inc})")
    print(f"Greatest Decrease in Profits:{Months[l]} (${GreatRev_Dec})")
    #setthe output path correctly 
    output_path = os.path.join(".", "Analysis", "Pybank.txt")
    #use the same format used for printing above and add \n string to ensure items print to a new line
    with open(output_path, 'w') as txtfile:
        txtfile.write(f"Financial Analysis\n")
        txtfile.write("----------------------\n")
        txtfile.write(f"Total Months:{months}\n")
        txtfile.write(f"Total: ${str(total)}\n")
        txtfile.write(f"Average Change:${Average_Change:.2f}\n")
        txtfile.write(f"Greatest Increase in Profits:{Months[k]} (${GreatRev_Inc})\n")
        txtfile.write(f"Greatest Decrease in Profits:{Months[l]} (${GreatRev_Dec})\n")
  