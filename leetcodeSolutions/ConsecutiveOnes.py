nums = [1,1,0,1,1,1]


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxCount = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = 0
            else:
                count +=1
                maxCount = max(maxCount, count)
        return maxCount

obj = Solution()
print(obj.findMaxConsecutiveOnes(nums))
