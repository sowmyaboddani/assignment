#collection of datatypes
##list--> used to store ordered collection of datatypes in a single variable , [], mutable(changable,allows duplicates)
thelist1=[True,False,True,False,True] #homogeneous--> same data type 
thelist=[True,398.65,"amazing!!",365,77=="77",365] #heterogeneous--> different data types
print("thelist=",thelist)
print("type of list=",type(thelist))

#indexing--> (positive indexing,negative indexing)
print("indexing 2 in list=",thelist[2])
print("indexing 5 in list=",thelist[-5])

#updating 
thelist[3]="right"
print("updating list using list[]=value =",thelist)

#appending (value added at the end, .add not possible)
thelist.append("unique")
print("appending list using list.append(value)=",thelist)
 
#inserting
thelist.insert(-3,"365")
print("inserting list using list.insert()=",thelist)

#extending
thelist.extend(thelist1)
print("extending the list=",thelist)

#deleting remove pop
del thelist[-3]
print("deleting index of -3 from the list=",thelist)

thelist.remove(False)
print("removing the value 'False' from the list=",thelist)

thelist.pop(-2)
print("popping the index of -2 from the list=",thelist)

del thelist
print(thelist)


##tuple-->used to store ordered collection of datatypes ,(),immutable(no change), allows(indexing,duplicates,del without index) 
thetuple1=("alpha","colab","assign") #homogeneous
thetuple=(True,"string",987.76,439,439) #heterogeneous
print("thetuple=",thetuple)
print("type(thetuple)=",type(thetuple))

#indexing
print("thetuple[1]=",thetuple[1])
print("thetuple[-3]=",thetuple[-3])

#deleting
del thetuple
print(thetuple)


##dictionary-->consists of keys and the values,{},mutable,duplicates excluded
thedict1={"hi":"helllo"}
thedict={"empnumb":"1058BCDO",
         "empname":"sowmya","empname":"sowmya",
         "empposition":"python developer",
         "empdepartment":"data science"}
print("thedict=",thedict)
print("type of thedict=",type(thedict))

#indexing
print("indexing dictionary=",thedict["empname"][-2])

#update
thedict["empfloor"]="third floor"
print("updating dictionary=",thedict)

del thedict
print(thedict)


##set--> unordered collection of data , {} , mutable , no duplicates
theset = {"str","dd",34,34,False,True,1,0}
print("theset=",theset)
print("type of theset=",type(theset))

#adding
theset.add("true")
print("adding in set=",theset)

set1 = {"str",34,1,False}
set2={"str1",908,True,0}
print("set1=",set1)
print("set2=",set2)

#union
set3=set1.union(set2)
print("union of set=",set3)

#pipe line symbol
set4=set1|set2|theset
print("union of set using | =",set4)

#intersection
set5=set1.intersection(set3)
print("intersection of set =",set5)

#ambersand
set6=set1&set3&set3
print("intersection of set using & =",set6)

#operators
seta=100
setb=100
print("seta!=setb =",seta!=setb)
print("seta==setb =",seta==setb)
print("seta>=setb =",seta>=setb)

#clear
theset.clear()
print(theset)
