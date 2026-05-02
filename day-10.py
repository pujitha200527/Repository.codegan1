'''
range()
-----------
-->this range() will generate sequence numbers upto the limit
syntax-->range(starting, ending, step)
eg:
choice_U = int(input("enter the limit:"))
for j in range(100,choice_U+1,3):
    print(j)
'''
'''
for i in range(2,101):
    if i%2==0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")
'''

'''break
--------------
-->this break statement will exit if the condition becomes true, and never enter into next loops
eg:
any = ["aareffa", "mouni","haniya","pujitha"]
for i in any:
       print(i)
       if i=="mouni":
          break
continue
-------------
-->this statement will skip that particular iteration and goes to next iterations'''
any = ["aareffa", "mouni","haniya","pujitha"]
for i in any:
       if i=="mouni":
          continue
       print(i)
