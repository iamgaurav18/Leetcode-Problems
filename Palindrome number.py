class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=x
        s=0
        if(x<0):
            return False
        elif(x==0):
            return True
        else:
            while(a>0):
                r=a%10
                a=a//10
                s=s*10+r
            if(s==x):
                return True
