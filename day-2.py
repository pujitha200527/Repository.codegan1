'''
variables
------------
To define a variable,we have 2 rules
1.good way to define a variable(No error)
2.bad way to define a variable (will get error)
note
---
--->we are going to use meaningful words or name for defining variables'''
num=90
num_2=6
'''keywords
-------
-->This keywords not only use as a variable
--->identifiers are nothing but keywords
--->Ex:if,while,for'''
a, b, c = 23, 56, 78
print(a)
print(a+b)
print(f"\n{a}\n{b}\n{c}")
'''Tokens
------
-->nothing but a small program or code in python to complete the task'''
a,b,c,d=4,5,6,7
print(a+d)
'''
Comments
-------
--->These are 2 types
1.Single line
-->this is used to explain about that particular line in the code,for this we can use #simple
2.Multi-line
--->To comment more than single line we can use multi line commenting
""" """,''' '''
Note
That won't be consider by the cursor
'''
a,b,c=5,7,9 #here in the same line,i have assign 3 variable and values
print(a+b)
'''
Boolean type
--->this is used to find out the statement is true or false'''
a = 90
b = 9
print(a!=b)
num=7
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")
