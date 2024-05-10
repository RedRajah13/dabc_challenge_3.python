# PyBank

import csv
import os

csvpath = "Resources/budget_data.csv"

month_count = 0
total_profit = 0
last_month_profit = 0
net_changes = []
date_col = []

# Open the CSV using the UTF-8 encoding
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        # calculate total num of months in dataset
        month_count += 1

        # net total amt profit/losses over entire period
        total_profit += int(row[1]) # column 1

        # this month profit - last month profit = month change
        # append to list of net changes
        # if first row, no change -> set so (this month) - (this month) = 0
        if (month_count == 1):
            last_month_profit = int(row[1])
        else:
            month_change = int(row[1]) - last_month_profit
            net_changes.append(month_change)
            date_col.append(row[0])

            # reset last month profit
            last_month_profit = int(row[1])

    print("Financial Analysis \n ---------------")
    print(f"Total number of months: {month_count}")
    print(f"Total profit: ${total_profit}")

    # average of monthly changes
    avg_change = int(sum(net_changes) / len(net_changes))
    avg_change = "{:.2f}".format(avg_change)
    print(f"Average monthly change: ${avg_change}")

    # greatest increase in profits (date + amt)
    max_change = max(net_changes)
    max_month_indx = net_changes.index(max_change)
    max_month = date_col[max_month_indx]

    print(f"Greatest increase in profits: {max_month}: ${max_change}")

    # greatest decrease in profits (date + amt)
    min_change = min(net_changes)
    min_month_indx = net_changes.index(min_change)
    min_month = date_col[min_month_indx]

    print(f"Greatest decrease in profits: {min_month}: ${min_change}")

    analysis = f"""Financial Analysis
    ---------------
    Total number of months: {month_count}
    Total profit: ${total_profit}
    Average monthly change: ${avg_change}
    Greatest increase in profits: {max_month}: ${max_change}
    Greatest decrease in profits: {min_month}: ${min_change}
    """

    with(open("PyBank.main.txt", 'w') as f):
        f.write(analysis)