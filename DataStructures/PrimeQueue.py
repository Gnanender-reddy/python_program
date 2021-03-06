"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Description:This code is for Prime Queue.

"""



from com.bridgelabz.DataStructures.Utility1 import LinkedList


def primes(n): #defining function for primes
    array = [i for i in range(2,n+1)] #taking range up to n+1
    p = 2

    while p <= n:
        i = 2*p
        while i <= n:
            array[i-2] = 0
            i += p
        p += 1

    return [num for num in array if num > 0]
def anagram(a):
    # initialize a list
    anagram_list = []
    for i in a:
        for j in a:
            if i != j and (sorted(str(i))==sorted(str(j))):
                anagram_list.append(i)
    return anagram_list
if __name__ == '__main__':
    print("The Prime Numbers are:\n", primes(1000), "\n")
    a = primes(1000)
    anagram_list=anagram(a)
    print("The prime anagrams up to 1000 is:\n",anagram_list,"\n")
    L=LinkedList()
    print("Adding prime anagrams to linked list:\n")
    for i in range(len(anagram_list)):
        L.add_element(anagram_list[i])
    L.display()

