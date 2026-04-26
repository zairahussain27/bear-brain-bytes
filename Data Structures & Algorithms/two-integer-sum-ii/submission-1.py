class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for f in numbers:
            l = target - f
            if l in numbers:
                return [ numbers.index(f)+1, numbers.index(l)+1 ]