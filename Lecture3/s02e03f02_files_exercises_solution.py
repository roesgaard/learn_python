# Exercise 1
# Read the contents of one of the python files (.py) used for previous exercises.
# Display the first 10 lines.
# Display the last 10 lines.
with open(r'test.py', 'rt') as file:
    lines = file.readlines()
    for l in lines[:10]:
        print(l, end='')
    for l in lines[-10:]:
        print(l, end='')

# Exercise 2
# Open a file with mode=Create and save the string "files in python are so easy, what do we need a teacher for?" to it.
# Keep in mind that if you run the solution more than once you'll get an error.
with open(r'out.txt', 'xt') as file:
    file.write("files in python are so easy, what do we need a teacher for?")

# Exercise 3
# Download and save https://www.gutenberg.org/files/1342/1342-0.txt to a .txt file. Read the files content and count
# occurrences of the letter 'a'.
with open(r'C:\temp\1342-0.txt', 'rt', encoding='utf-8') as file:
    content = file.read()
    print(content.count('a'))

# Exercise 4
# Use the book downloaded in exercise 3 and save its lines in reversed order to a file "reversed_lines_jane.txt".
# Use the book downloaded in exercise 3 and save its content in reversed order to a file "reversed_completely_jane.txt".
with open(r'C:\stuff\1342-0.txt', 'rt', encoding='utf-8') as file:
    content = file.read()
    with open('reversed_lines_jane.txt', 'wt', encoding='utf-8') as reversed_lines_jane:
        reversed_lines_jane.write('\n'.join(reversed(content.splitlines())))
    with open('reversed_completely_jane.txt', 'wt', encoding='utf-8') as reversed_completly:
        reversed_completly.write(''.join(reversed(content)))
