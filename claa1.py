#collection of datatypes
#list--> used to store ordered collection of datatypes in a single variable , [], mutable(changable,allows duplicates)
thelist1=[True,False,True,False,True] #homogeneous-- same data type 
thelist=[True,398.65,"amazing!!",365,77=="77",365] #heterogeneous-- different data types
print(thelist)
print(type(thelist))

#indexing
thelist=[True,398.65,"amazing!!",365,77=="77",365] 
print(thelist[2])
print(thelist[-5])

#updating
thelist=[True,398.65,"amazing!!",365,77=="77",365] 
thelist[3]="right"
print(thelist)

#appending (value added at the end, .add not possible)
thelist=[True,398.65,"amazing!!",365,77=="77",365] 
thelist.append("unique")
print(thelist)
 
#inserting
thelist.insert(-3,"365")
print(thelist)

#concatinating
thelist=[True,398.65,"amazing!!",365,77=="77",365] 
thelist1=[False,"gratitude"]
print(thelist,thelist1)

#extending
thelist=[True,398.65,"amazing!!",365,77=="77",365]
thelist.extend(thelist1)
print(thelist)

#deleting remove pop
del thelist[-3]
print(thelist)
thelist.remove(False)
print(thelist)
thelist.pop(-2)
print(thelist)
