from com.bridgelabz.DataStructures.Utility1 import countBST, countBT

if __name__ == '__main__':
    n = int(input("Enter number of nodes to find bst"))

    # find count of BST and binary
    # trees with n nodes
    count1 = countBST(n)
    count2 = countBT(n)

    # print count of BST and binary trees with n nodes
    print("Count of BST with", n, "nodes is", count1)
