class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if the diff bw target and hashset is there in the hashset we return those 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target :
                    return [i,j]
        return 402