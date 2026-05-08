'''
fibbonaci series:
    num = 0
num_1 = 1
any = int(input("enter a number:"))
print(num,num_1,end = " ")
for j in range(1,any+1):
    num_2 = num + num_1
    num = num_1
    num_1 = num_2
    print(num_2,end=" ")
armstrong number:
armstrong = int(input("enter a number:"))
total = 0
length_ = len(str(armstrong))
for j in str(armstrong):
    total+=int(j) ** length_
if total ==  armstrong:
    print(f"{armstrong} is a armstrong number")
else:
    print(f"{armstrong} is not a armstrong number")
num = 15
if num % 3 ==0 and num % 5 == 0:
    print(f"{num} is Divi by 3 and 5")
else:
    print("not")
num = 100
for j in range(1,num+1):
    if j % 3 ==0 and j % 5 == 0:
         print(f"{j} is Divi by 3 and 5")
any = [34,67,56,2,3,7]
def sum_even(any):
    total = 0
    for j in any:
        if j % 2 ==0:
            total+=j
            print(total)
sum_even(any)
lambda function
--------------'''
an = lambda a,b,c,d:a*b*c*d
print(an(7,8,9,10))
        
