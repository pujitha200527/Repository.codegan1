'''operators
--->1.Arithmetic operator
2.Assignment operator
3.comparison operator
4.logical operator
5.identity operator
6.membership operator
7.bitwise operator
1.arithmetic operator---> + , - ,% ,* ,** '''
Num_1=78
Num_2=89
Num_3=90
print(Num_1+Num_2+Num_3)
num_1=6
num_2=9
print(num_1 - num_2)
a = 8
b = 3
print(a%b)
print(a% b==0)
print(a%b!=0)
digi_ =9
digi_2 =3
print(digi_ * digi_2)
print(digi_ ** digi_2)
digi_1 =100.67
digi_3 =3.7
print(digi_1// digi_3)
'''2.Assignment Operators
---> =+ ,-= ,%= ,*= ,**= ,//= ,&= '''
number = 9
number += 4
print(number)
a=9
a-=5
print(a)
b=34
b%=4
print(b)
c=56
c*=4
print(c)
d=89
d**=6
print(d)
'''3.comparison operators
---> ==, !=, >=, <=, <, >
'''
e=90
f=100
print(e>f)
print(e<f)
print(e<=f)
print(e>=f)
print(e==f)
print(e!=f)
'''4.logical operators
---> and, or, not
'''
g = 5
h = 8
print(g > 8 and h < 10)
'''is--->this operator is used to check the object
is not--->this operator is used to check the object not same
'''
y = 9
z = 9
print(y is z)
list_ =[1,2]
list_2 =[1,2]
list_3 = list_
print(id(list_))
print(id(list_2))
print(id(list_3))
print(list_ is list_2)
print(list_ == list_2)
'''in--->are used to check it ,it present in it
in not--->are used to check it,it not present in it'''
'''&--->Bitwise AND
5---> 0101
3---> 0011
--------
1 --> 0001'''
print(5&3)







