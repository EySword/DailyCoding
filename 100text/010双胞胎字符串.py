s1='abcd'
t1='cdab'
s2='abcd'
t2='bcda'

class Solution:
    def isTwin(self,s,t):
        slen,tlen=len(s),len(t)
        if slen!=tlen:
            return "No"
        sOdd,sEven=[],[]
        tOdd,tEven=[],[]
        n=slen//2
        for i in range(n):
            sOdd.append(s[2*i])
            sEven.append(s[2*i+1])
            tOdd.append(t[2*i])
            tEven.append(t[2*i+1])
            pass
        if slen%2==1:
            sOdd.append(s[-1])
            tOdd.append(t[-1])
            pass
        sOdd.sort()
        sEven.sort()
        tOdd.sort()
        tEven.sort()
        if sOdd==tOdd and sEven==tEven:
            return "Yes"
        else:
            return "No"



if __name__=="__main__":
    a=Solution()
    print(a.isTwin(s2,t2))
