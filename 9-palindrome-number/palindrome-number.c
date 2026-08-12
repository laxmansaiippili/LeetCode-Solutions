bool isPalindrome(int x) {
    long  a,b=x,c=0,d,e,f;
    if(x<0)
    return 0;
    for(;b!=0;b/=10)
        c=c*10+b%10;
    return x==c;
}