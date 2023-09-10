conv_factor = {}                    # declaring or defining a dict
conv_factor['dollar'] = 60          # adding new element to dict
conv_factor['euro'] = 80

print("\n",conv_factor,"\n")                  # printing entire doict

print(conv_factor['dollar'],"\n")        # accessing and printing the value corresponing to the particular key

# for getting all the keys in a dict
print(conv_factor.keys(),"\n")

# list of keys in a dict
print(list(conv_factor.keys()),"\n")
#list func is used to create a list of given parameter

# list of values
print(list(conv_factor.values()),"\n")

# list of items where each item is represented as a tuple -->  (key,vale)
print(list(conv_factor.items()),"\n")

# func on dict
# conv_factor.

# know what a function does
# conv_factor.pop?

# print(conv_factor['yen'])  --> key error since there is no key with that name

#updating a value
conv_factor['dollar'] = 65
print(conv_factor)

conv_factor['yen'] = 50
print(conv_factor)

# deleting an item
del conv_factor['yen']
print(conv_factor)

e = 30

print("Total = ", e*conv_factor['euro'])
