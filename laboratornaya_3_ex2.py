import math
import time
# O(3n)
print('O(3n)')
c = 0
k = []
n = 12
#n = 13
for i in range(n):
    c+=1
    l = n // 2
    c += 1
    if i > l:
        k.append('High')
        c += 1
    elif i == l:
        k.append('Eq')
        c += 1
    else:
        k.append('Low')
        c += 1
print(*k)
print('Сложность Алгоритма', c)

# O(n*logn)
print(' ')
print('O(n*log(n))')
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        x = arr[len(arr)//2]
    l_nums, r_nums, m_nums = [],[],[]
    for i in arr:
        if i < x: l_nums += [i]
        elif i > x: r_nums += [i]
        else: m_nums += [i]
    return qsort(l_nums) + m_nums + qsort(r_nums)
n = [3,2,1]
print(*qsort(n))
#print('Временная сложность алгоритма', round(len(n) * math.log2(len(n))))

# O(n!)
print(' ')
print('O(n!)')
def factorial(n):
    num = n
    if n == 0: return 1
    for i in range(n):
      num = n * factorial(n - 1)
    return num
for i in range(10):
    t = time.perf_counter()
    fac = factorial(i)
    print(fac)
    #print(i, fac, time.perf_counter() - t)

# O(n**3)
print(' ')
print('O(n^3)')
def On3(n):
    k = 0
    for i in range(n):
        for j in range(n):
            for g in range(n):
                k += 1
    return k
print(On3(10))
#print('Сложность алгоритма', On3(10))

# O(3*log(n))
print(' ')
print('O(3*log(n))')
def BinarySearch(arr, x):
    mid = len(arr)//2 
    l = 0
    r = len(arr)
    if arr == []:
        return False
    if arr[mid] == x:
        return True
    if arr[mid] < x:
        return BinarySearch(arr[mid+1 : r], x)
    if arr[mid] > x:
        return BinarySearch(arr[l : mid], x)
    return False
arr = [1, 2 ,3 ,4 , 5 , 6, 7, 8, 10, 11 ]
n = 10
for i in range(n - 1, n + 2):
    print(BinarySearch(arr, i))
#print(round(3 * len(arr)))
