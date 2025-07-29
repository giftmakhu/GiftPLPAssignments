#Creating my empty List
my_list = []

#Populating my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#printing/viewing my list
print("CREATING MY LIST: \n",my_list,"\n")

#inserting value 15 in my list
my_list.insert(1,15)

print("INSERTING 15 IN MY LIST: \n",my_list,"\n")

#extending my list with a new new list
my_list.extend([50, 60, 70])

print("EXTENDING MY LIST WITH A NEW LIST: \n",my_list,"\n")

#deleting the last element on the list
my_list.pop()

print("DELETING THE LAST ELEMENT ON MY LIST: \n",my_list,"\n")

#sorting my list in ascending order
my_list.sort()

#finding and printing the index of 30
index_of_30 = my_list.index(30)
print("THE INDEX IF 30 IS: ",index_of_30)
    

