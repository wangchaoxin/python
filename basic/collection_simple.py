# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# 1 list
thislist = ["apple", "banana", "cherry"]
print(thislist)
# access items
print(thislist[1])
# change the item value
thislist[1] = "blackcurrant"
# loop in a list
for x in thislist:
    print(x)
# Check if Item Exists
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
# List Length
print(len(thislist))
# Add Items
thislist.append("orange")
# add an item at the specified index
thislist.insert(1, "orange")
# Remove Item
thislist.remove("banana")
# pop iterm
thislist.pop()
# remote at specified index
del thislist[0]
# The list() Constructor
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets

# 2 tuple 不可改变的
# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
thistuple[1]
thistuple[1] = "blackcurrant"
for x in thistuple:
    print(x)
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
print(len(thistuple))
# 可以删除整个元组，不可以删除元素
del thistuple
thistuple = tuple(("apple", "banana", "cherry"))

# set
# A set is a collection which is unordered and unindexed
thisset = {"apple", "banana", "cherry"}
# 不可以通过index访问，可以通过in访问
for x in thisset:
    print(x)
if 'apple' in thisset:
    pass
# Add Items
thisset.add("orange")
# Add multiple items to a set, using the update() method:
thisset.update(["orange", "mango", "grapes"])
print(len(thisset))
# 如果元素不存在remove会抛出异常，discard不会抛出异常
thisset.remove("banana")
thisset.discard("banana")
thisset.clear()
del thisset
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets

# 3 dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model")
thisdict["year"] = 2018
# Print all key names in the dictionary, one by one:
for x in thisdict:
    print(x)
# Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])
# You can also use the values() function to return values of a dictionary:
for x in thisdict.values():
    print(x)
# Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
    print(x, y)
# Check if "model" is present in the dictionary:
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
print(len(thisdict))
# Adding Items
thisdict["color"] = "red"
# Removing Items
thisdict.pop("model")
del thisdict["model"]
# remove all
thisdict.clear()
del thisdict
# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary:
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
