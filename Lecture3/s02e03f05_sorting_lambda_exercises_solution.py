# Exercise 1
# Sort the list by ascending order
list1 = [500, 1.5, 1000, 1.198, 400, 3.13, 40000, 999, 2, 5, 17]
print(sorted(list1))

# Exercise 2
# Sort the list from Exercise 1 by the number of characters in each number (500 has 3 characters, 1.5 has 3 characters
# too).
print(sorted(list1, key=lambda x: len(str(x))))

# Exercise 3
# list2 contains simulated number of total Covid-19 cases by different models by May 4th in Denmark. Knowing that on May
# 4th there were 9670 cases of Covid-19 in Denmark sort the models from most to least accurate.
list2 = [("modelA", 12780), ("modelB", 8100), ("modelC", 5601), ("modelD", 25589), ("modelA", 11378), ("modelA", 74496)]
print(sorted(list2, key=lambda x: abs(9670 - x[1])))

# Exercise 4
# Sort the list containing student names and their grades by grades descending.
s_grades = [("Mark", 5), ("Joanna", 6), ("Bob", 4), ("Jessie", 2), ("Tim", 4), ("Mark", 5)]
print(sorted(s_grades, key=lambda x: x[1], reverse=True))

# Exercise 5
# Sort the list from exercise 4 by grades descending. If two students have the same grade they should be sorted in
# alphabetical order (this exercise requires sorting by 2 keys, feel free to google for help)
print(sorted(s_grades, key=lambda x: (x[1], x[0]), reverse=True))
