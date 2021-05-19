# This script covers working with dates and times.

# So far we have worked with data types like: int/str/list. Those data types are always available by default. Python
# offers a lot of functions and data types not available by default. We need to tell python first that we'll be using
# a particular function or data type. Those functions and data types are stored in modules. Modules are packages of code
# written by other programmers. Python comes installed with a lot of modules. One of them is the datetime module
# containing data types for working with dates/times/time zones.
# How do we tell python that we want to use the `datetime` module (or any other module)?
# We import it:
import datetime

# Now we can use all the goodies from the datetime module.
# We can ask python for current datetime
x = datetime.datetime.now()
print(x)

# Lets ask python for type of variable x
print(type(x))

# Python will say <class 'datetime.datetime'>. This means that x holds a value which is an object of class
# datetime.datetime. The name datetime.datetime means that the class `datetime` is in the module `datetime`.
# Later we will work with `datetime.date`/`datetime.time`/`datetime.timedelta`.
# Classes in python define what kind of object we can create while programming. Classes are tightly bound with the idea
# of Object Oriented Programming (OOP). What OOP allow is to create a data type and bind some operations to it.
# Like using the .sort() method on a list.
# OOP will not be covered by this course. But you're more the encouraged to research it on your own.

# Lets get back to datetime
# Printing a date like this gives us quite some details, perhaps too many
print(x)
# The format of a datetime can be changed with .strftime() function (STRing Format TIME)
print(x.strftime("%c"))
# .strftime() accepts a parameter which defines the desired format.
# With .strftime() you can use one of the build in formats like %X or %x.

# Exercise 1 - try out %x and %X and see how they format datetime objects.


# You can define your own format using directives described here:
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

# Exercise 2 - Using python docs display the current datetime in format: '2020-12-15 16:56'

# Objects in python have attributes. Attributes of a datetime object are: year/month/day
# We can access those attributes:
print(x.year)
print(x.day)

# You can find details about the datetime class here https://docs.python.org/3/library/datetime.html#module-datetime

# How to create other datetime object?
# We can use the datetime() constructor.
# A constructor is a special function responsible for creating objects.
# Lets create the datetime of Battle of Grunwald
g = datetime.datetime(1400, 7, 15)
print(g)

# The datatime() constructor has more parameters but they're optional, full description can be found in the docs
# https://docs.python.org/3/library/datetime.html#datetime.datetime (all arguments with a default value are optional)

# Exercise 3 - create a datetime object representing begging datetime of Battle of Grunwald.
# Lets assume the battle started at 15:21.


# Beside using the constructor we can parse strings to create datetime objects
date_time_str = '2018-06-29 08:15:27.243860'
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
print(date_time_obj)
# strptime() accepts 2 parameters: a string with a datetime and a string explaining the format. Directives used for
# parsing are the same directives used for formatting


# Exercise 4 - parse the following datatime string
dt_str = '2020/12/17 14:15'


# The datetime module offers more than just the `datetime` class. There are types to represent:
# - just the date (class datetime.date)
# - just the time (class datetime.time)
# - timedelta to represent a time span (so that we can perform computations on datetimes)
# We can construct those object similar to datetime or deconstruct our datetime into them:

print(f'Date:{date_time_obj.date()}')
print(f'Time:{date_time_obj.time()}')

d = datetime.date(2010, 12, 30)
print(d)

td = datetime.timedelta(hours=1240)
print(f'timedelta is {td}')

# We can also do calculations on dates.
# Lets see how long ago the Battle of Grunwald took place
time_distance = datetime.datetime.now() - g
print(f'The Battle of Grunwald took place {time_distance} ago')
# It probably is not suprising that `time_distance` is of type datetime.timedelta
print(f'type of time_distance if {type(time_distance)}')

# Knowing how to perform computations on dates and time we can compute precisely when someone turns 18.
# if someone would be born right now, he will turn 18:
b = datetime.datetime.now()
print(b + datetime.timedelta(days=18 * 365))
print(b.replace(year=b.year + 18))
# Both method have their drawbacks, the first does not take into account leap years. The latter can result in an error.
# What will happen if you run the code below? (Notice that year 2000 was a leap year and 2018 was not)
# print(datetime.datetime(2000, 2, 29).replace(year=b.year + 18))
# The type `relativedelta` can fix this issue but we will not cover it here.

# When working with datetimes it is important to keep timezones in mind so it's another topic you can research later :)

# Exercise 5 - Write a program which will print the week's numbers and their begin/end dates for 2020
# week 01 - 2020.01.01 - 2020.01.05
# week 02 - 2020.01.06 - 2020.01.12
# ...

# Extend your program so that the current week is marked
# ...
# week 23 - 2020.06.01 - 2020.06.07
# week 24 - 2020.06.08 - 2020.06.14 * current week
# week 25 - 2020.06.15 - 2020.06.21
# ...

# Exercise 6 - Write a program which will display "Saint Salary Days" in DC. (last workday of each month) in 2020.
