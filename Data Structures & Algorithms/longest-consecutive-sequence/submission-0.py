class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in numsSet:  # use set to avoid duplicates
            if (num - 1) not in numsSet:  # start of sequence
                current = num
                length = 1

                while (current + 1) in numsSet:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest