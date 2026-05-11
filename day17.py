'''Generators
-----------------
-->Generators in python is enable lazy evaluation for producing sequence of values efficiently
-->They differ from regular functions by execution and resuming on demand
-->Generators create iterators that yield values one at a time using the yield keyword
eg:
for j in range(1,10):
    print(j)

Functions VS Generators
----------------------------------
-->regular functions execute fully upon call and return a single value,terminating afterward
-->generators  use yield to produce multiple value lazily, acting like iterators without building the entire sequence in memory
eg:
def add (num,num_2):
    print(num+num_2)
add(5,6)
add(86,9)
eg:
def count_(num):
    i=1
    while i<=num:
        yield i
        i+=1
gen_=count_(3)
print(next(gen_))
print(next(gen_))
print(next(gen_))

yield
-----------------
-->yield pauses the generator function, saves it state(local variable,position),and returns the yielded value to the caller

Next
------------------------
--> This advances the generator by executing until the next yield, returning that value, subsquent calls resume from there
'''
def message_gen():
    yield"First Message"
    yield"Second Message"
    yield"Done"
gen_= message_gen()
print(next(gen_))
print(next(gen_))
print(next(gen_)

    
