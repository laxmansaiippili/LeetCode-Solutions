class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        tot=0;
        n=len(mat);
        i=0;
        while(i<n):
            tot+=mat[i][i];
            tot+=mat[i][n-i-1];
            i+=1;
        if(n%2==0):
            return tot;
        else:
            return tot-mat[n//2][n//2];