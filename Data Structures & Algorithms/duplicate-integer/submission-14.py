class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Hash = set()
        for i in nums:
            if i in Hash:
                return True
            Hash.add(i)
        return False