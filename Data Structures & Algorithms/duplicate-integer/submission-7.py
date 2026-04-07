class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Hash = set()

        for n in nums:
            if n in Hash:
                return True
            else:
                Hash.add(n)
        return False