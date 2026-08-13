class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result=[];
        while(left<=right):
            val=left;
            issd=True;
            while(val>0):
                r=val%10;
                if(r==0):
                    issd=False;
                    break;
                if(left%r!=0):
                    issd=False;
                val=val//10;
            if(issd==True):
                result.append(left);
            left+=1;
        return result;

