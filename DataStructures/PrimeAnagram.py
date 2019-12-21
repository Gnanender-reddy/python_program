
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

#Defining function for anagram
def anagram(a):
    # initialize a list
    anagram_list = []
    for i in a:
        for j in a:
            if i != j and (sorted(str(i))==sorted(str(j))):
                anagram_list.append(i)
    return anagram_list

#Driver code
if __name__ == '__main__':
    print("The Prime Numbers up to 1000:\n", primes(1000), "\n")
    a = primes(1000)
    T100=a[:25]
    c100=anagram(T100)
    print("The prime anagrams from 0 to 100 is:\n ",[c100])
    T200 = a[25:46]
    c200 = anagram(T200)
    print("The prime anagrams from 101 to 200 in two dimensional :\n ",[c200])
    T300 = a[45:61]
    c300 = anagram(T300)
    print("Sorry there are no anagrams present between 201 to 300\n")

    T400 = a[61:78]
    c400 = anagram(T400)
    print("The prime anagrams from 301 to 400 in two dimensional :\n ",[c400])

    T500 = a[78:94]
    c500 = anagram(T500)
    print("The prime anagrams from 401 to 500 in two dimensional :\n ",[c500])

    T600 = a[95:108]
    c600 = anagram(T600)
    print("Sorry there are no anagrams present between 501 to 600\n")

    T700 = a[109:125]
    c700 = anagram(T700)
    print("The prime anagrams from 601 to 700 in two dimensional :\n ",[c700])

    T800 = a[126:139]
    c800 = anagram(T800)
    print("Sorry there are no anagrams present between 701 to 800\n")

    T900 = a[140:154]
    c900 = anagram(T900)
    print("Sorry there are no anagrams present between 801 to 900\n")

    T1000 = a[155:168]
    c1000 = anagram(T1000)
    print("The prime anagrams from 901 to 1000 in two dimensional :\n ",[c1000])

    #
    #
    #
    # #d = np.array([np.array(c[0:2]), np.array(c[2:5]), np.array(c[5:8])])
    # #print(d)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #







 #    A=[c[0:2],c[2:5],c[5:8]]
  #  A=np.array(A)
   # print(A)

    #A = [[1,2,3],[4,5,6],[7,8,9]]
#A = np.array(A)

    #print("The Anagram elements from 0 to 100 are listed :", anagram(T100), "\n")

   # b = np.array([np.array(c[0:3]),np.array(c[3:5]),np.array(c[5:8])])
    #print(b)
#a = np.array([np.array([1,2,3]),np.array([2,3,4]),np.array([6,7,8])])
