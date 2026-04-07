class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Hash = set()
        for n in nums:
            if n in Hash:
                return True
            Hash.add(n)
        return False