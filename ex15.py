
# open and read file from python Shell
# create a file object
file = open("ex15_sample.txt", "r")
# read the content
print file.read()

# read the first 4 characters
file = open("ex15_sample.txt", "r")
print file.read(4)
file.close()


