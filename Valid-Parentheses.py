class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in s:
            if (i=='(' or i=='{' or i=='['):
                a.append(i)
            else:
                if(len(a)==0):
                    return False
                elif(i==')'):
                    if(a[len(a)-1]=='('):
                        a.pop()
                    else:
                        return False
                elif(i=='}'):
                    if(a[len(a)-1]=='{'):
                        a.pop()
                    else:
                        return False
                elif(i==']'):
                    if(a[len(a)-1]=='['):
                        a.pop()
                    else:
                        return False
        if(len(a)==0):
            return True