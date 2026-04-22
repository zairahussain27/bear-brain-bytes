class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        flag=False
        for i in range(len(nums) - 1):
            if(nums[i+1]==nums[i]):
                flag=True
                break
        return flag
