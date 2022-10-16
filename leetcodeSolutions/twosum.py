# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
numbers = [1,3,2,7,11,15]
target = 9
def solve(numbers, target):
    di = {}
    for i, num in enumerate(numbers):
        if num not in di:
            di[target-num] = i
        else:
            return [di[num]+1, i+1]

print(solve(numbers, target))
