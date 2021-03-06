# Lists are very useful. In this scripts we will learn how to slice
# lists.

# We already know how to access items in a list by using their
# indexes
fruits = ["apple", "carrot", "banana", "tomato"]
print(fruits[1])  # will print "carrot" since indexes starts at 0

# Sometimes we might need to access items from the end instead of
# from the beginning like we do with indexes.
# Lists in Python support "negative indexing" allowing us to access
# items from the end
print(fruits[-1])  # index -1 refers to the last item
print(fruits[-2])  # index -2 refers to the second last item, etc...

# Slicing lists is also very useful if we need to extract a sublist.
# We do this by specifying from/to indexes
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# positive |  0  |    1    |    2    |    3    |   4   |    5   |    6   |
#          ---------------------------------------------------------------
# negative | -7  |   -6    |   -5    |   -4    |  -3   |   -2   |   -1   |
fruits_sub_list = fruits[2:5]
print(fruits_sub_list)

# Using slicing we can also get a sublist from the tail using
# negative indexing
print(fruits[-5:-1])  # notice that here "mango" will not be printed
# becuse the "to" index is always exclusive

# If we need a sublist including the last element
print(fruits[-5:])

# To get first the first 5 elements of a list we can do either:
print(fruits[:5])
print(fruits[0:5])

# We can even create a slice of a list containing the whole list.
# Later we will find out why this is useful
print(fruits[:])  # by not specifying from/to we get the whole list

# Can we ask python to return a slice of a list, but only every
# second element? We can:
numbers = list(range(0, 10))
even_from_first_5 = numbers[0:5:2]
print(even_from_first_5)
# numbers[0:5:2] - explanation:
#         | | |
#         start from the index 0
#           | |
#           take elements until index 5 exclusive
#             |
#             take every 2nd (second) item
# The same way we can ask for every 3rd, 4th, ... item.
# The numbers used for slicing are usually named: [from:to:step] or
# [start:stop:step]

# To get every second item from the whole list:
print(numbers[::2])

# We can even ask for items from the end setting step to -1
print(numbers[::-1])  # reversed list
print(numbers[::-2])  # every second item of a reversed list

# Why is this slice empty?
print(numbers[0:3:-1])
# This slice is empty because we set the start to index 0 and the
# step to -1 (going left) but there are no items in the list before
# the 0 element.
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | items
# -------------------------------------------------------
# |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  | indexes
#  start              stop
#  <- direction

# If we set "start" to the right of "stop" we should get an nonempty
# slice with step -1
print(numbers[7:3:-1])
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | items
# -------------------------------------------------------
# |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  | indexes
#                     stop                   start
#                            *     *     *     * <- direction

# We can express the same using negative indexing
print(numbers[-2:3:-1])
# |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | items
# -------------------------------------------------------
# |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  | indexes pos
# | -9  | -8  | -7  | -6  | -5  | -4  | -3  | -2  | -1  | indexes neg
#                     stop                   start
#                            *     *     *     * <- direction

# Reversing lists is very useful because often we will need to
# process a list from the tail.

things_to_do = ["hoover", "iron", "dishes", "walk", "read book", "code"]

print("wrong order of doing things:")
for x in things_to_do:
    print(x)

print("correct order of doing things:")
for x in things_to_do[::-1]:
    print(x)

# Slicing lists might be confusing because of the many possibilities
# it provides. While coding use the interactive shell to remind your
# self how slicing works.

# exercise 1: create a list with months.
# a) print it forwards
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]
print("\n month reversed")
print(months)
# b) print it backwards
print("\n month backwards")
print(months[::-1])
# c) print sublist of winter months
print("\nwinter")
print(months[-2:] + months[:2])
# d) print sublist of summer months reversed
print("\nsummer reversed")
print(months[-4:-9:-1])
# e) print months of II and III quoter
print("\nII and III quoter")
print(months[3:9])
# f) print odd months
print("\nodd months")
print(months[::2])
# g) print even months from march to october
print("\neven months from march to october")
print(months[3:10:2])


# exercise 2: A coder's work is mostly reading existing code. Read
# the commented code below and before running it, try to deduce what
# will be the output of the code. Write it down, run the code, how
# many list slices did you predict correctly?

cities = ["Gdansk", "Gdynia", "Krakow", "Lodz", "Poznan", "Warsaw", "Wroclaw"]
# print(cities[0:2]) # first 2
# print(cities[:]) # whole list
# print(cities[:4]) # first four
# print(cities[-5:]) # all from and including Krakow
# print(cities[::2]) # every second, starting with Gdansk
# print(cities[::-1]) # all reversed
# print(cities[::-3]) # every 3rd from tail: Wroclaw, Lodz, Gdansk
# print(cities[0:1:-3]) # none
# print(cities[-1:1:-1]) # reversed exclusing first 2
# print(cities[-1:-9:-2]) # every second from tail


# exercise 3: Write a program which will ask the user for a number N.
# The program will compute the sum of all even numbers from
# 0 to N.

# Solution
n = int(input("Provide a number"))
s = 0
for i in range(1, n+1):
    if i % 2 == 0:
        s += i
print(s)

# Solution 2
s = 0
for i in range(2, n+1, 2):
    s += i
print(s)

# exercise 5: Write a program which will ask the user for a number N
# and print numbers from 1, 2, 3, 4,... until their sum exceeds N

# Solution
n = int(input("Provide a number"))
s = 0
for i in range(1, 99999):
    print(str(i) + ", ", end="")
    s += i
    if s > n:
        break
