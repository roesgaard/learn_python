# Exercise 1

# Use data from https://www.fueleconomy.gov/feg/download.shtml
# Data can be found also in vehicles.csv
# documentation: https://www.fueleconomy.gov/feg/ws/index.shtml#vehicle
# As a starting point we will be interested in columns: year,make,model,comb08**
# ** there are different measures for fuel efficiency the column "comb08" (MPG) should be a good starting point
#    you can find the definition of this column in the documentation

# 1. Load data from the csv files into list of dictionaries (code helper below)
import csv

def to_str(row):
    return f'{row["year"]:4} {row["make"]:10} {row["model"]:35} {row["comb08"]:5}'


with open(r"C:\git\dc_python_basic_s02\vehicles.csv") as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]
# 2. What are the newest and oldest cars in the csv file?
for row in sorted(rows, key=lambda x: x['year'])[:5]:
    print(to_str(row))
for row in sorted(rows, key=lambda x: x['year'], reverse=True)[:5]:
    print(to_str(row))


# 3. Find car models with highest and lower fuel efficiency (use comb08 for fuel efficiency)
worst_car = sorted(rows, key=lambda x: x['comb08'])[0]
print(f"worst Miles Per Gallon results {to_str(worst_car)}")

best_car = sorted(rows, key=lambda x: x['comb08'], reverse=True)[0]
print(f"best Miles Per Gallon results  {to_str(best_car)}")

# 4. Count and print distinct car makers.
#    tip: do you remember the set() data type?
s = set()
for row in rows:
    s.add(row['make'])
print(f'There are {len(s)} different car manufacturers')

# The same using set comprehension
makers = {row['make'] for row in rows}
print(f'There are {len(makers)} different car manufacturers')

# 5. Find top 10 models by worst fuel efficiency.
print("worst Miles Per Gallon results")
for row in sorted(rows, key=lambda x: x['comb08'])[:10]:
    print(to_str(row))

print("best Miles Per Gallon results")
for row in sorted(rows, key=lambda x: x['comb08'], reverse=True)[:10]:
    print(to_str(row))

# 6. Find top 10 models by greatest range.
#    Use just one of the range columns described in the documentation.
print("best range")
for row in sorted(rows, key=lambda x: x['rangeHwyA'], reverse=True)[:10]:
    print(to_str(row))

# 7. Homework: Find the model with best range for each car maker.
for maker in makers:
    only_this_makes_cars = [row for row in rows if row['make'] == maker]
    print(f'best range for {maker}')
    for row in sorted(only_this_makes_cars, key=lambda x: x['rangeHwyA'], reverse=True)[:10]:
        print(to_str(row))

# Code helper - how to load csv data in python?


