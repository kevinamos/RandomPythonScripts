def get_factorial(num):
    factorial = 1
    if num < 0:
        return 0
    elif(num == 0):
        return 1
    else:
        while(num > 0):
            factorial = factorial*num
            num = num-1
        return factorial


def zeros(n):
    factorial = repr(get_factorial(n))
    print(factorial)
    list_fact = [i for i in factorial]
    i = 1
    for digit in list_fact:
        if list_fact[-i] != '0':
            break
        i = i+1
    return i-1


def zeross(n):
    import math
    factorial = repr(math.factorial(n))
    print(factorial)
    list_fact = list(factorial)
    i = 1
    for digit in list_fact:
        if list_fact[-i] != '0':
            break
        i = i+1
    return i-1


def findTrailingZeros(n):

    # Initialize result
    count = 0

    # Keep dividing n by
    # powers of 5 and
    # update Count
    i = 5
    while (n/i >= 1):
        count += int(n/i)
        i *= 5

    return int(count)


# Driver program
n = 1000
print("Count of trailing 0s " +
      "in 100! is", findTrailingZeros(n))

print(get_factorial(-10))
# This code is contributed by Smitha Dinesh Semwal
