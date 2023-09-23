class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = len)
        s,d="",""
        a=0
        c=True
        if(len(strs[0])==0):
            return s
        elif(len(strs)==1):
            return strs[0]
        else:
            for i in range(len(strs[0])):
                d=strs[0][i]
                for j in range(len(strs)):
                    if(d==strs[j][i]):
                        continue
                    else:
                        c=False
                        break
                if(c==False):
                    break
                if(a==len(strs[0])-1):
                    s=s+d
                    break
                else:
                    s=s+d
                    a=a+1
            return s