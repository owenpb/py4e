# Assignment 10.2: Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day
# for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon. Once you have accumulated the counts for each hour, print out the counts, sorted
# by hour as shown below.


name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if line.startswith('From '):
        line = line.split()
        fulltime = line[5]  # Time will always be fifth element of the list of words
        times = fulltime.split(':')
        hour = times[0]
        counts[hour] = counts.get(hour, 0) + 1

lst = list()
for k, v in counts.items():
    lst.append((k, v))

lst.sort()

for k, v in lst:
    print(k, v)

