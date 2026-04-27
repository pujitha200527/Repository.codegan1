'''any = [1,"python is a language",[2,"this is 5th class",3],56]
print(any[2])
print(any[2][1])
print(any[2][1][10])
any = [1,"python is a language",67,68,[34,["this is python class"],78,"i'm looking for good bat]",[2,"this is 5th class",3],56]]
print(any [4][1][0][14])
methods
----
1.append()
------
-->this method is used to add new item into list,but it will add in the last index position
syntax--->variable_name.append(item)
eg:
an=[1,2,3,4]
an.append(75)
print(an)
2.extend()
----
-->this method is also used to add new item into list, but this extend add as each position to each index in the list
-->Extend only takes iterables
syntax-->variable_name.extend(item(iterables))
eg:
an=[1,2,3,4]
an.append("python")
an.extend("python")
print(an)
3.pop()
----
-->pop index out of range
-->this is used to delete an item from the list,this pop() remove the value based on the index  position mentioned in the parameters
-->if nothing is mentioned in the parameters,it will remove last index position value
syntax-->variable_name.pop(index position)
eg:
an=[1,2,3,4]
an.pop()
print(an)
4.remove()
----
-->this is also used to delete item from the list, but remove() method will delete value
syntax-->variable_name.remove(value)an=[1,2,3,4]
eg:
an=[1,2,3,4]
an.remove(3)
print(an)
slicing()
----------
-->this is used to get particular part of the list,string or tuple
-->this is work based on index position
syntax-->variable_name[starting index : ending index]
eg:
an=[1,2,3,4]
print(an[2:3])
len()
----------------------
-->method is used to find the number of items present in the list
syntax-->len(variable)
eg:
an=[1,2,3,4]
print(len(an))
'''
an=[1,2,3,4]
print(len(an))



