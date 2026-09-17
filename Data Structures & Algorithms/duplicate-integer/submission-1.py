class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        j={}
        for i in nums:
            if i in j:
                return True
            j[i]=1
        return False