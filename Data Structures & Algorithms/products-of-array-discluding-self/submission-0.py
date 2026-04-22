class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_array=[1]*len(nums)

        prefix=1
        for i in range(len(nums)):
            result_array[i]=prefix  # take the prefix in result array
            prefix*=nums[i]         # now take multiple of previous prefix with new

        postfix=1
        for i in range(len(nums)-1,-1,-1):
            result_array[i]*=postfix #multiple the prefix with postfix
            postfix*=nums[i] #take the postfix of previos and multiply with new post

        return result_array