class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}

        for i in range (len(nums)):
            num=nums[i]
            needed=target-num
            if needed in seen:
                return [seen[needed],i]
                break
            else:
                seen[num]=i     
                     