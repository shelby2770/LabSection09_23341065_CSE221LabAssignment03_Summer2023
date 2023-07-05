file_1= open("input1.txt")
file_2= open("output1.txt", "w")
n= int(file_1.readline())
arr= list(map(int, file_1.readline().split()))
total= 0

#Using Fenwick Tree/ Binary Indexed Tree
BIT = [0] * (n + 1)
def getSum(idx):
    sum = 0
    while idx > 0:
        sum += BIT[idx]
        idx -= idx & (-idx)
    return sum

def update(idx, val):
    global n
    while idx <= n:
        BIT[idx] += val
        idx += idx & (-idx)

def BITtree(n):
    global total
    for i in range(n):
        total_sum = getSum(n)
        before_sum = getSum(arr[i])
        inv = total_sum - before_sum
        total+= inv
        update(arr[i], 1)


#Using Merge Sort
def merge(l, mid, r):
    global total
    res_arr= [0]* (r-l+1)
    idx1 = l
    idx2 = mid + 1
    pointer = 0
    while idx1<= mid and idx2<= r:
        if arr[idx1]>= arr[idx2]:
            total+= (r-idx2+1)
            res_arr[pointer]= arr[idx1]
            idx1+= 1
        else:
            res_arr[pointer]= arr[idx2]
            idx2+= 1
        pointer+= 1

    while idx1<= mid:
        res_arr[pointer]= arr[idx1]
        pointer+= 1
        idx1+= 1

    while idx2<= r:
        res_arr[pointer]= arr[idx2]
        pointer+= 1
        idx2+= 1

    j= l
    for i in range(len(res_arr)):
        arr[j]= res_arr[i]
        j+= 1

def mergeSort(l, r):
    if l<r:
        mid= l+ (r-l)//2
        mergeSort(l, mid)
        mergeSort(mid+1, r)
        merge(l, mid, r)


BITtree(n)
# mergeSort(0, n-1)
file_2.write(str(total))
file_1.close()
file_2.close()
