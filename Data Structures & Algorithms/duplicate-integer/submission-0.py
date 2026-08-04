class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        j={}
        for i in range(len(nums)):
            if nums[i] in j:
                return True
            else:
                j[nums[i]]=1
        return False
        