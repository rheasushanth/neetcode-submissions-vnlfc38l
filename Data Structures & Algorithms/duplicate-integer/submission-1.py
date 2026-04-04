class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list1 = sorted(nums)
        for i in range(1,len(nums)):
            if list1[i] == list1[i-1]:
                return True
        return False
        