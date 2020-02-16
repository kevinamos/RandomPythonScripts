import time
from math import log, ceil

def num_of_steps(num):
    num=int(num, 2)
    steps=0
    while num >0:
        if num%2==0:
            num=num/2
        else:
            num=num-1
        steps+=1
    return steps

# Function to print binary number for the  
# input decimal using recursion

def decimalToBinary(n, d=[]):
    if d!=[]:
        d=d+[n%2]
    if(n > 1):
        d=[1]
        decimalToBinary(n//2)
    return d


print(decimalToBinary(7, []))
def num_of_steps2(num):
    num=int(num, 2)
    print(num)
    l=log(num,2)
    if ceil(l)==int(l):
        return l+1
    steps=0
    while num >0:
        if num%2==0:
            num=num/2
        else:
            num=num-1
        steps+=1
    return steps


start=time.time()

n=''.join((str(1) for i in range(1000)))
print(num_of_steps2(n) )

print(time.time()-start)

#print(num_of_steps2('001000111111111111111111111111111111111111111111111111111111000000000000111111111111111111111111111111111111111111111111111111111111111111111001000111111111111111111111111111111111111111111111111111111000000000000111111111111111111111111111111111111111111111111111111111111111111111001000111111111111111111111111111111111111111111111111111111000000000000111111111111111111111111111111111111111111111111111111111111111111111001000111111111111111111111111111111111111111111111111111111000000000000111111111111111111111111111111111111111111111111111111111111111111111') )

