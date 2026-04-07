class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in hash:
                return [hash[diff],i]
            hash[n] = i 