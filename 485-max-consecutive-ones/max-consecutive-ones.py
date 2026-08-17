class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i=0;
        maxnum=0;
        for num in nums:
            if(num==1):
                i+=1;
                maxnum=max(i,maxnum);
            else:
                i=0;
        return maxnum;