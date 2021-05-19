# Exercise 1
# The code below creates a list of integers which specify the length of each word in a certain sentence, but only if the
# word is not the word "the".
# Express the same using list comprehensions
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print(words)
print(word_lengths)
print([len(w) for w in words if w != 'the'])


# Exercise 2
# Using a list comprehension, create a new list called `newlist` out of the list `numbers`, which contains only the
# positive numbers from the list, as integers.
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [n for n in numbers if n > 0]
print(newlist)


# Exercise 3
# Using your code from 06_list.py/Exercise 06 create a function is_prime(). Using this function with list comprehension
# create a list with prime numbers in range 1-1000
def is_prime(n):
    for d in range(2, int(n/2) + 1):
        if n % d == 0:
            return False
    return True


print([n for n in range(1, 1000) if is_prime(n)])

# Exercise 4
# Use a dictionary comprehension to count the length of each word in a sentence. Use this exercise's first sentence as
# input.
# Your dictionary should contain entries:
# lengths["Use"] == 3
# lengths["a"] == 1
# lengths["dictionary"] == 10
# ...
words = 'Use a dictionary comprehension to count the length of each word in a sentence'.split()
print({word: len(word) for word in words})

# Exercise 5
# Using a nested list comprehension create a list with all multiplications of numbers 0-10
print([x*y for x in range(11) for y in range(11)])

# Exercise 6
# Use the zip() function and a dictionary comprehension to create a dictionary which has digits as keys and their
# english names as values
nums = range(1, 11)
names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
print({n: name for n, name in zip(nums, names)})
