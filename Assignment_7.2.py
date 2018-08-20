# Assignment 7.2: Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form: X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values
# and produce an output as shown below.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fhand = open(fname)

total = 0
count = 0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        col = line.find(":")
        substr = line[col+1:]
        substr = substr.lstrip()
        num = float(substr)
        total = total + num
        count = count + 1

average = total / count

print("Average spam confidence:", average)




