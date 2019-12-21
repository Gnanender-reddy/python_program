def primes(n): #defining function for primes
    array = [i for i in range(2,n+1)] #taking range up to n+1
    p = 2
    #In this loop we are making even numbers as zero
    while p <= n:
        i = 2*p
        while i <= n:
            array[i-2] = 0
            i += p
        p += 1

    return [num for num in array if num > 0]

#Driver Code
if __name__ == '__main__':

    a=primes(1000)
    print(a)
    print("The prime numbers in two dimensional \n")
    print([a[:24],a[25:45],a[46:61],a[62:77],a[78:94],a[95:108],a[109:125],a[126:139],a[140:154],a[155:168]])



























# def getprime(N, primeArr):  # Print prime or not
#     for num in range(0, N + 1):
#         if num > 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#             else:
#                 primeArr.append(num)
#
# N = 1000
# primeArr = []
# getprime(1000, primeArr)        #calling prime function
# blocks = []
# k = 0
# for i in range(0, 10):
#     blocks.append([])
#     min = k
#     k = k + 100
#     for j in primeArr:
#         if  j <= k and j >= min:
#             blocks[i].append(j)
#
# for i in blocks:
#     print (i)