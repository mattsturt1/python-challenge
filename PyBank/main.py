# Modules
import os
import csv

# Set path for file
csvpath = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")


data = ''

x = int()

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    running_total = 0
    data = list(csvreader)
    total_months = len(data) 
    # print(total_months)

    for x in csvreader:
        running_total = running_total + int(x[1])
        

# data = list(csvreader)   

total = 0
for d in data:
    total += int(d[1])
# print(total)  

months = [d[0] for d in data]
num_months = len(months)
# print(num_months)

 
profits = [d[1] for d in data] 

profits_int = [int(x) for x in profits]


# print(profits_int)


 
profit_diff = [profits_int[i] - profits_int[i-1] for i in range(1,num_months)] 

average_diff = sum(profit_diff) / (num_months - 1)
# print(f"${average_diff:,.2f}")

smallest_difference = min(profit_diff), 
largest_difference = max(profit_diff)

small_month = 0 
large_month = 0 


small_month = int(profit_diff.index(min(profit_diff)))
large_month = int(profit_diff.index(max(profit_diff)))
# print(small_month) 
# print(large_month)

small_month_print  =  months[small_month + 1]
large_month_print = months[large_month + 1]



print("Financial Analysis")

print("------------------------")

print(f"Total Months : {total_months}")
print(f"Total : ${running_total}")
print(f"Average Change : ${average_diff:,.2f} ")
print(f"Greatest Increase in Profits: {large_month_print}(${largest_difference})")
print(f"Greatest Decrease in Profits: {small_month_print}(${smallest_difference})")


# Specify the file to write to
output_path = os.path.join(os.path.dirname(__file__), "analysis", "election_analysis.txt")
# Open the file using “write” mode. Specify the variable to hold the contents
with open(output_path, 'w') as textfile:
    # Initialize csv.writer
    # Write the first row (column headers)
    textfile.write(f"Financial Analysis")
    textfile.write(f"-------------------------\n")
    textfile.write(f"Total : ${running_total}\n")
    textfile.write(f"Average Change : ${average_diff:,.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {large_month_print}(${largest_difference})\n")
    textfile.write(f"Greatest Decrease in Profits: {small_month_print}(${smallest_difference})\n")
    textfile.write(f"-------------------------\n")





  
    


