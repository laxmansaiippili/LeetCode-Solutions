class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        x=prices[0];
        i=1;
        maxprofit=0;
        while(i<len(prices)):
            if(prices[i]>x):
                maxprofit=max(maxprofit,prices[i]-x);
                
            else:
                x=prices[i];
            i+=1;
        return maxprofit;