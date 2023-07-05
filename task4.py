file_1 = open("input4.txt")
file_2 = open("output4.txt", "w")
n = int(file_1.readline().split()[0])
arr = list(map(int, file_1.readline().split()))
pref_k = [-1] * n

def Partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def kthelem(arr, l, r, k):
    pivot_pos = Partition(arr, l, r)
    pref_k[pivot_pos] = arr[pivot_pos]
    if pivot_pos == k:
        return arr[k]
    elif pivot_pos < k:
        return kthelem(arr, pivot_pos + 1, r, k)
    return kthelem(arr, l, pivot_pos - 1, k)


q = int(file_1.readline().split()[0])
for i in range(q):
    k = int(file_1.readline())
    k -= 1
    if pref_k[k] != -1:
        file_2.write(f"{pref_k[k]}\n")
    else:
        ans= kthelem(arr, 0, n - 1, k)
        file_2.write(f"{ans}\n")

file_1.close()
file_2.close()
