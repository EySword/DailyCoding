s='abcd'
t='bcaed'

class Solution:
    def findTheDifference0(self,s,t):
        listT=list(t)
        listT.sort()
        strT=''.join(listT)
        for i in range(len(s)):
            if s[i]!=strT[i]:
                return strT[i]
        return strT[-1]

    def findTheDifference1(self, s, t):
        flag=0
        for i in range(len(s)):
            flag+=(ord(t[i])-ord(s[i]))
            pass
        flag+=ord(t[-1])
        return chr(flag)


if __name__=="__main__":
    a=Solution()
    print(a.findTheDifference1(s,t))