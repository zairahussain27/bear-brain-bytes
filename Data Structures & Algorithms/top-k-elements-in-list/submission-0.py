class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        result =[]
        while k > 0:
            max_num = max(freq, key=freq.get)
            result.append(max_num)
            freq.pop(max_num)
            k -=1
        return result

       