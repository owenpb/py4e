# Assignment 9.4: Write a program to read through the mbox-short.txt and figure out who has the sent the greatest
# number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person
# who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the
# number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

fname = input("Enter file:")
if len(fname) < 1: fname = "mbox-short.txt"
fhand = open(fname)

counts = dict()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        name = words[1]
        counts[name] = counts.get(name, 0) + 1

bigcount = None
bigname = None

for name, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigname = name

print(bigname, bigcount)