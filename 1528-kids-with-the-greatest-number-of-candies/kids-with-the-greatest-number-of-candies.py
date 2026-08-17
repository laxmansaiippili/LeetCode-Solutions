class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        great=max(candies);
        arr=list();
        for candie in candies:
            if(candie+extraCandies>=great):
                arr.append(True);
            else:
                arr.append(False);
        return arr;