class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left=0;
        right=len(s)-1;
        chars=list(s);
        while(left<right):
            while chars[left] not in "aeiouAEIOU" and left<len(s)-1:
                left+=1;
            while chars[right] not in "aeiouAEIOU" and right>0:
                right-=1;
            if(left<right):
                chars[left],chars[right]=chars[right],chars[left];
                left+=1;right-=1;
        return "".join(chars);
