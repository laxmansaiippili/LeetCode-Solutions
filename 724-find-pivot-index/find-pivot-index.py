class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totsum=sum(nums);
        prevsum=0;
        for i in range(len(nums)):
            if(prevsum==totsum-prevsum-nums[i]):
                return i;
            prevsum+=nums[i];
        return -1;