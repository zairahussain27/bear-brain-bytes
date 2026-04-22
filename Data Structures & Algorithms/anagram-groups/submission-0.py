class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            # Create a frequency map for 'a' through 'z'
            count = [0] * 26 
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # Use tuple(count) as the key because lists are unhashable
            res[tuple(count)].append(s)
            
        return list(res.values())

        