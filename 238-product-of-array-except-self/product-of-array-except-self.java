class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n=nums.length;
        int[] res=new int[n];
        int[] right=new int[n];
        int prod=1;
        for(int i=n-1;i>=0;i--)
        {
            prod=prod*nums[i];
            right[i]=prod;
        }
        int left=1;
        int i=0;
        for(i=0;i<n-1;i++)
        {
            res[i]=left*right[i+1];
            left=left*nums[i];
        }
        res[i]=left;
        return res;
    }
}