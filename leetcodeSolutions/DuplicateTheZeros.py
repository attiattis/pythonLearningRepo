arr = [1,0,2,3,0,4,5,0]
# arr = [1,2,3]
# output : [1,0,0,2,3,0,0,4]
def count(arr):    
    count = 0 # count of zeros
    n = len(arr)
    for i in range(n):
        if (2*count)+i >= n:
            break
        if arr[i] == 0:
            count +=2
    # copy tht items to the last positions
    if count == 0:
        return arr
    i-=1
    j = n - 1
    if arr[i] == 0:
        arr[j] = 0
        j -= 1
        i -=1
    while j >=0:
        if arr[i] == 0:
            arr[j] = 0
            arr[j-1] = 0
            j -= 2
            i -=1
        else:
            arr[j] = arr[i]
            j -=1
            i -=1
    return arr

print(count(arr))
