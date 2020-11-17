# Exercise 1

# Use data from https://www.fueleconomy.gov/feg/download.shtml
# Data can be found also in vehicles.csv
# documentation: https://www.fueleconomy.gov/feg/ws/index.shtml#vehicle
# As a starting point we will be interested in columns: year,make,model,comb08**
# ** there are different measures for fuel efficiency the column "comb08" (MPG) should be a good starting point
#    you can find the definition of this column in the documentation

# 1. Load data from the csv files into list of dictionaries (code helper below)
# 2. What are the newest and oldest cars in the csv file?
# 3. Find car models with highest and lower fuel efficiency (use comb08 for fuel efficiency)
# 4. Print and count distinct car makers.
#    tip: do you remember the set() data type?
# 5. Find top 10 models by worst fuel efficiency.
# 6. Find top 10 models by greatest range.
#    Use just one of the range columns described in the documentation.
# 7. Homework: Find the model with best range for each car maker.


# Code helper - how to load csv data in python?
# We could write our own function to read csv data but python offers this functionality out-of-the-box.
# The only thing we need to do is to import the "csv module" and use it.
import csv

with open(r"C:\git\dc_python_basic_s02\vehicles.csv") as file:  # open the file with data
    reader = csv.DictReader(file)                               # use the DictReader to get an reader able to read rows as dictionaries
    rows = []
    for row in reader:                                          # we can use the reader object just like a list of rows
        rows.append(row)                                        # lets read all rows the reader has and add the to the list rows

# `rows` is now a list of dictionaries. Each row from the .csv file is now a dictionary in `rows`
# we can now get the 5-th row:
print(rows[4])

# to get a specific column of the 5-th row:
print(rows[4]["make"])  # gets the manufacturer of the 5-th row

for row in rows[:10]:
    print(row)
print(rows[1]["barrels08"])
