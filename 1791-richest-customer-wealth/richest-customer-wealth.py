class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxsum=0;
        for i in range(len(accounts)):
            sum=0;
            for j in range(len(accounts[0])):
                sum=sum+accounts[i][j];
            maxsum=max(sum,maxsum);
        return maxsum;