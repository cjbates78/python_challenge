# Dependencies
import os
import csv

#specify the file to read
Budget_csv = os.path.join('C:/Users/Carrie Work/Desktop/python_challenge/pybank/Resources/budget_data.csv')
                          
# create txt file to print to
output_path = os.path.join("pybank.txt")

# Track various financial parameters
total_months = 0
month_of_change = []
profit_loss = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_profit_loss = 0

#csv reader specifies delimiter and variable that holds content
with open(Budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #read the header row first
    csv_header = next(csvreader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(csvreader)
    total_months += 1
    total_profit_loss += int(first_row[1])
    prev_net = int(first_row[1])

        #start loop
    for row in csvreader:
            #add 1 to the count
            total_months += 1

            #add the first element in the total
            total_profit_loss = int(row[1])

            # Track the net change
            net_change = int(row[1]) - prev_net
            prev_net = int(row[1])
            profit_loss += [net_change]
            month_of_change += [row[0]]

            # Calculate the greatest increase
            if net_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = net_change

            # Calculate the greatest decrease
            if net_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = net_change

# Calculate the Average Net Change
net_monthly_avg = sum(profit_loss) / len(profit_loss)

# Generate Output Summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
# Print the output (to terminal)
print(output)

#open and write to output file
f = open("pybank.txt", "w")
f.write(output)
f.close()
           
           
           
           