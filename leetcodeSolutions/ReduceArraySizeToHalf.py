'''
    You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

'''
from collections import Counter
arr = [1,3,3,3,3,5,5,5,2,2,7]
arr_chr_count = Counter(arr).most_common()

count = 0
current_length = 0 
target_length = len(arr) // 2
for i, j in arr_chr_count:
    if current_length >= target_length:
        break
    count += 1
    current_length += j

print(count)

