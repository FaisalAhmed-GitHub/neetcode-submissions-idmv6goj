class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hashset = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in Hashset:
                return [Hashset[diff], i]
            Hashset[n] = i