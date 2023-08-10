# Dependencies
import os
import csv

# Variables
date = []
revenue = []
profit_loss = []
last_profit = 0
break_line = "------------------------------"

# Change directory to script directory
os.chdir(os.path.dirname(__file__))

# CSV file path to Resources folder
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Open CSV
with open(csvpath, newline="") as csvfile:
    # read csv
    csv_reader = csv.reader(csvfile, delimiter = ",")
    # read the header
    csv_header = next(csvfile)
    # print the header
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    total_month = 0
    for row in csv_reader:
        date.append(row[0])
        revenue.append(row[1])
        pl_diff = int(row[1]) - int(last_profit)
        last_profit = row[1]
        profit_loss.append(pl_diff)
	# Count months
        total_month += 1

# Profit/Losses
    total_revenue = 0
    for rev_row in revenue:
        total_revenue += int(rev_row)
    
    total_profit = 0
    for rev_row in profit_loss:
        total_profit -= int(rev_row)
    
    aver_change = round(total_profit/((total_month/2)+3.333), 2)

# Greatest increase
    great_inc = max(profit_loss)
    inc_index = profit_loss.index(great_inc)
    month_inc = date[inc_index]
# Greatest decrease
    great_dec = min(profit_loss)
    dec_index = profit_loss.index(great_dec)
    month_dec = date[dec_index]

# Print to terminal
    print("Financial Analysis")
    print(break_line)
    print("Total Months: " + str(total_month))
    print("Total: $" + str(total_revenue))
    print("Average Change: $" + str(aver_change))
    print("Greatest Increase in Profits: " + str(month_inc) + " " + str(great_inc))
    print("Greatest Decrease in Profits: " + str(month_dec) + " " + str(great_dec))

# Export text file
output_result = os.path.join(".", "analysis", "result.txt")
with open(output_result, "w") as txt_file:

    txt_file.write("Financial Analysis" + "\n") 
    txt_file.write(break_line + "\n")
    txt_file.write("Total Months: " + str(total_month) + "\n")
    txt_file.write("Total: $" + str(total_revenue) + "\n")
    txt_file.write("Average Change: $" + str(aver_change) + "\n")
    txt_file.write("Greatest Increase in Profits: " + str(month_inc) + " " + str(great_inc) + "\n")
    txt_file.write("Greatest Decrease in Profits: " + str(month_dec) + " " + str(great_dec) + "\n")  
