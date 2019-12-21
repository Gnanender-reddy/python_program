
def primes(n): #defining function for primes
    array = [i for i in range(2,n+1)]
    #taking range up to n+1
    p = 2

    while p <= n:

        i = 2*p

        while i <= n:
            array[i-2] = 0
            print(array)
            i += p
        p += 1
    return [num for num in array if num > 0]
print(primes(4))
