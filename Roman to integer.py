class Solution:
    def romanToInt(self, s: str) -> int:
        a="IVXLCDM"
        b=(1,5,10,50,100,500,1000)
        l=len(s)
        c=False
        p=0
        for i in range(l):
            if(c):
                c=False
                continue
            if(i+1<=l-1):
                if(a.index(s[i])<a.index(s[i+1])):
                    p=p+(b[a.index(s[i+1])]-b[a.index(s[i])])
                    c=True
                else:
                    p=p+b[a.index(s[i])]
            else:
                p=p+b[a.index(s[i])]
        return p