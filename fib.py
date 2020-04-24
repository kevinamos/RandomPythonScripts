def fib_rec(n):
    if n<=1:
        return 1
    return (fib_rec(n-1)+ fib_rec(n-2))


#l=[fib_rec(x) for x in range(10)]




def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
    
def get_sumatorial2(num):
    return ((num*num)+num)/2


def get_sumatorial(num):
    factorial = 0
    if num < 0:
        return 0
    elif(num == 0):
        return 1
    else:
        while(num > 0):
            factorial = factorial+num
            num = num-1
        return factorial


l1=[get_sumatorial(x) for x in range(1, 40)]
l2=[get_sumatorial2(x) for x in range(1, 40)]

print(l1==l2)

print(l2)

"""
def fib_it(n):
    if n<=1:
        return 1
    if 
        
        
  

l=[fib_it(x) for x in range(10)]
print(l)


def fib_mem():
    pass


0,1,1,2,3
"""
