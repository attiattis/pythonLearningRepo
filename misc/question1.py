# find the nth smallest element in the array
def findTheNthSmallest(li, n):
    li.sort()
    return(li[n])
n = int(input("Enter the array size : "))
arr = []
for i in range(n):
    arr.append(int(input("Enter the array element : ")))

index = int(input("Enter the position of the smallest element : "))
# call the function
print(index, " th smallest item is " , findTheNthSmallest(arr, index))