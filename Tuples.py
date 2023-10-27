ice_cream_flavours = ("vanilla","chocolate","butterscotch","strawberry")
print(ice_cream_flavours)

for flavour in ice_cream_flavours:
    print(flavour)
print(ice_cream_flavours[2])        # item at index 2

# a tuple one made does not support, change, modify, new insretion or deletion of an item
# tuples are immutable

del ice_cream_flavours              # delete the entire tuple

toy = (1,2,3,4)
print(len(toy))                     # length of the tuple toy

print(toy.count(2))                 # count the occurence of particular item

toy = (1,2,3,4,5,6,1,4,2,3)
'''
Changes the tuple.
Kills the previous existing one.
'''

print(toy.index(2))

rainbow = ("violet","indigo","blue","green","yellow","orange","red")
print(rainbow)