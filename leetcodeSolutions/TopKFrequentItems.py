# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
import collections
nums = [3,0,1,0]
k = 1
result = {}
for i in nums:
    if i in result:
        result[i]+=1
    else:
        result[i] = 1
print(result.values())
li = sorted(result.values(), reverse=True)[:k]
li = ( [k for k,v in result.items() if v in li])

print(li)
