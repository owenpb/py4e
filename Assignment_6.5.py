
# Assignment 6.5:  Write code using find() and string slicing (see section 6.10) to extract the number at the end of
# the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

# Find index of the colon
start = text.find(':')

# Store the string beginning with whitespace and ending with the number
substr = text[start+1:]

# Remove the whitespace to the left of the number
num = substr.lstrip()

fnum = float(num)

print(fnum)

