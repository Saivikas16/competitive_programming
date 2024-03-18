class Solution(object):
    def searchRange(self, nums, target):
        n=len(nums)
        left,right=0,n-1
        if target in nums:
            for i in range(0,n):
                if nums[left]==nums[right]:
                    return [left,right]
                elif nums[left]<target:
                    left=left+1
                else:
                    right=right-1
        else:
            return [-1,-1]
                
