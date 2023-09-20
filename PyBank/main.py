# Created by: Gabriel Adriano
# Created for: Monash Bootcamp 2023
# Module 3 Challenge - PyBank

# import modules

import csv
import os

# set file path

csvpath = os.path.join('Resources', 'budget_data.csv')

# open csv file
with open(csvpath, encoding = 'utf') as csvfile:
    # read csv file
    csvreader = csv.reader(csvfile, delimiter = ',')
    # skip header
    next(csvreader)
    # skip first month from for loop
    budget_data = [next(csvreader)]
    # set initial amount of profit/loss
    nett_amount = int(budget_data[0][1])
    # create empty list to hold values
    amount_change = []
    # variable to hold value to compute amount variation
    previous_amount = nett_amount

    for row in csvreader:
        # Total months
        budget_data.append(row)
        # Nett profits/losses
        nett_amount = nett_amount + int(row[1]) 
        # Changes in profits/losses
        amount_change.append(int(row[1]) - previous_amount)
        # Average change of profits/losses
        previous_amount = int(row[1])

# greatest increase/decrease in profits over the entire period.
greatest_increase_profit = amount_change.index(max(amount_change))
greatest_decrease_profit = amount_change.index(min(amount_change))

# output information
output = f"""
Financial Analysis

----------------------------

Total Months: {len(budget_data)}

Total: ${nett_amount}

Average Change: ${round(sum(amount_change)/(len(amount_change)),2)}

Greatest Increase in Profits: {budget_data[greatest_increase_profit+1][0]} (${max(amount_change)})

Greatest Decrease in Profits: {budget_data[greatest_decrease_profit+1][0]} (${min(amount_change)})
"""

# creates the required directory if it does not exist

output_directory = 'Analysis'
os.makedirs(output_directory, exist_ok=True)

# display to terminal
print(output)

# export to file
csvpath = os.path.join('Analysis', 'Financial_Analysis.txt')
with open(csvpath, 'w') as textfile:
    textfile.write(output)
