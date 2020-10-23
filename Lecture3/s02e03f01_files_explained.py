# read whole file
with open("file_name.csv", "rt") as file:
    file_content = file.read()  # read whole file into variable
    print(file_content[0:50])   # print first 50 characters
    print(file_content.splitlines()[0])
    print(file_content.splitlines()[0].split(",")[0:10])

# mode
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# text/binary
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# read file line by line
with open(r"file_name.csv", "rt") as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()

# file.readline() return emtpy string when reaching end-of-file

# writing to a file
with open(r"file_name.csv", "at") as file:
    file.write("this is text")
