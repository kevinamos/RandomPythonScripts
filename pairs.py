def get_sumatorial2(num):
    return ((num*num)+num)/2

def solution(A):
    set_of_A=set(A)
    if set_of_A==A:
        return 0
    total_pair=0
    for i in set_of_A:
        count=A.count(i)-1
        if count>0:
            total_pair+=get_sumatorial2(count)
            if total_pair>=1000000000:
                return 1000000000
    return total_pair



from random import randint
A=[3,5,6,3,3,5]
B=[x for x in range(10000)]
D=[randint(1, x) for x in range(2,700)]

A=A+B+D
print('working....')

print(solution([2,2,2,2,2]))

print('Done..')


            

