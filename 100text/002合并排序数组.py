A=[1,2,3,4]
B=[2,4,5,6]

def mergeSortArray(A,B):
    C=A+B
    print(C)
    C.sort()
    return C

print(mergeSortArray(A,B))