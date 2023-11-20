import os
import csv

# path for the CSV file in PyBankc

csv_file = r'Resources\budget_data.csv'

#lists to store data. 

profit = []
monthly_changes = []
date = []

# PyBank's variables
 
count = 0
total_profit = 0
total_profit_change = 0
initial_profit = 0

# Open and read csv

with open(csv_file) as f:
    csvreader = csv.reader(f, delimiter = ",")
# for Header row 
    csv_header = next(csvreader)

# Read through each row after header
    for row in csvreader:   
       
# count of months in this dataset
      count = count + 1 
      date.append(row[0])

# Append the profit information & calculate the total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

     
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

# monthly changes in a list
      monthly_changes.append(monthly_change_profits)

      total_profit_change = total_profit_change + monthly_change_profits
      initial_profit = final_profit

# average change in profits
      average_profit_change = (total_profit_change/monthly_change_profits)
      
# highest and lowest variations in Profit/Loss
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)
# Indexing highest and lowest variations in Profit/Loss 
      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
# Financial Analysis:

    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total Months: {count}")
    print(f"Total : ${total_profit}")
    print(f"Average Change: ${average_profit_change}")
    print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase_profits})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_profits})")
    
# Exporting text file with the analysis/results
with open('Analysis/Financial_Analysis.txt', 'w') as finalf:
  
    finalf.write("Financial Analysis"+ "\n")
    finalf.write("----------------------------------------------------------\n")
    finalf.write(f"Total Months: {count} \n")
    finalf.write(f"Total: ${total_profit} \n")
    finalf.write(f"Average Change: ${average_profit_change} \n")
    finalf.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase_profits}) \n")
    finalf.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_profits}) \n")
   