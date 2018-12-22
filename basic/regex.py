import re

# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
    print("YES! We have a match!", str(x))
else:
    print("No match")

# Print a list of all matches:
str = "The rain in Spain"
x = re.findall("ai", str)
print(x)


# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:

str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())
