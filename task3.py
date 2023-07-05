file_1= open("input3.txt")
file_2= open("output3.txt", "w")
n= int(file_1.readline())
arr= list(map(int, file_1.readline().split()))

def QUICKSORT(A, p, r):
    if p<r:
        q= Partition(A, p, r)
        QUICKSORT(A, p, q-1)
        QUICKSORT(A, q+1, r)


def Partition(A, p, r):
    x= A[r]
    i= p-1
    for j in range(p, r):
        if A[j]<= x:
            i+= 1
            A[i], A[j]= A[j], A[i]
    A[i+1], A[r]= A[r], A[i+1]
    return i+1

QUICKSORT(arr, 0, n-1)

file_2.write(" ".join(map(str, arr)))
file_1.close()
file_2.close()
