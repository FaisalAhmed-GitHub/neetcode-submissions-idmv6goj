class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        subSet = set(nums)
        longest = 0

        for n in subSet:
            if (n-1) not in subSet:
                length = 1
                while (n + length) in subSet:
                    length += 1 
                longest = max(length, longest)
        return longest