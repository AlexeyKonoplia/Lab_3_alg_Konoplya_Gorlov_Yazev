k = 0
def sortir(arr):
    global k
    for i in range(1,len(arr)):
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]: 
                arr[j],arr[j+1] = arr[j+1],arr[j]
                k += 1
    return arr
print(sortir([8, 7, 6, 5, 4,3 ,2 ,1]))
#print(k)
