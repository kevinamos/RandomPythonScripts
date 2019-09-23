def is_palindrom(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    n_str = list(repr(n))
    n_str.reverse()
    n_str = int(''.join(n_str))
    num_sum = n_str+n
    if num_sum == n*2:
        return True, num_sum
    else:
        return False, num_sum


def palindrome_chain_length(n):
    palindrom = is_palindrom(n)
    count = 0
    while palindrom[0] == False:
        print(palindrom)
        count = count+1
        n = palindrom[1]
        palindrom = is_palindrom(n)
    return count


print(palindrome_chain_length(87))
