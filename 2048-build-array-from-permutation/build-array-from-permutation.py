class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[0]*len(nums);
        i=0;
        for num in nums:
            res[i]=nums[nums[i]];
            i+=1;
        return res;