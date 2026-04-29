'''
Tuple
-----
-->tuple is a collection of different data types that represent by() and the items in the tuple is separeted by  comma..
eg:
so = (1,"python",[7,8],(5,0),1)
print(so[1])

so=(1,3,4,5)
any=(2,6,7)
print(so+any)
Dictionary
----------
--->Dict is a collection of key : value pair, where keys are immutable such as (strings, integer, and tuple) and value are any data type this is represented by{}
eg:
my={"Name": "Puji",1 : 3,(1,2): 6,"Name" : "palli"}
print(my)
Methods
-------
1.key()
-------
-->This is method is used to access only keys in the dictionary
syntax->dict.keys()
eg:
my={"Name": "puji",1 : 3,(1,2): 6}
print(my.keys())
2.value()
--------
--->this is used to acces only values in the dictionary
syntax->dict.values()
eg:
my={"Name": "puji",1 : 3,(1,2): 6}
print(my.values())
3.items()
---------
--->This method is used to access key :value pair in the dictionary
syntax-> dict.items()
eg:
my={"Name": "puji",1 : 3,(1,2): 6}
print(my.items())
4.clear()
---------
--->This clear() method is used to delete all the items in the dictionary
syntax->dict.clear()
eg:
my={"name":"puji","age":21, "edu":"b.tech"}
my.clear()
print(my)
5. update()
----------
--->this method is used to add new item(key:value)into the dictionary
syntax->dict.update({key:value})
eg:
my={"name":"puji","age":21,"edu":"b.tech"}
my.update({"role":"developer"})
print(my)
'''
