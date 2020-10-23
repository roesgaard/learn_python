# from https://github.com/CoreyMSchafer/code_snippets/blob/master/List_Comp/comprehensions.py
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)
print([n for n in nums])


# I want 'n*n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)
print([n*n for n in nums])


# I want 'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)
print([n for n in nums if n % 2 == 0])


# I want 'n' for each 'n' in nums if 'n' is_magic_number()
def is_magic_number(x):
    return x in [1, 7, 9, 42]


my_list = []
for n in nums:
    if is_magic_number(n):
        my_list.append(n)
print(my_list)
print([n for n in nums if is_magic_number(n)])


# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)
print([(letter, number) for letter in 'abcd' for number in range(4)])


# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(zip(names, heroes))

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heroes)
my_dict = {}
for name, hero in zip(names, heroes):
    my_dict[name] = hero
print(my_dict)
print({name: hero for name, hero in zip(names, heroes)})


# If name not equal to Peter
print({name: hero for name, hero in zip(names, heroes) if name != "Peter"})


# Set Comprehensions
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)
print({n for n in nums})
