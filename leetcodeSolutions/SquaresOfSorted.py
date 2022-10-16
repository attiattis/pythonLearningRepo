class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left= 0 
        right = len(nums) - 1
        li = [None] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[right]) > abs(nums[left]):
                li[i] = nums[right] * nums[right]
                right -= 1
                
            else:
                li[i] = nums[left] * nums[left]
                left += 1
        return li
        
