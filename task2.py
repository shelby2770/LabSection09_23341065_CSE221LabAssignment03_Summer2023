import math
file_1= open("input2.txt")
file_2= open("output2.txt", "w")

n= int(file_1.readline())
arr= list(map(int, file_1.readline().split()))

pref_max= [0]*n
max_val= -math.inf
for i in range(n-1, -1, -1):
    max_val= max(abs(arr[i]), max_val)
    pref_max[i]= max_val

total= -math.inf
for i in range(0, n-1):
    total= max(total, arr[i]+ pref_max[i+1]**2)
file_2.write(str(total))
file_1.close()
file_2.close()
