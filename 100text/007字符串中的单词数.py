s='Hello, my name is  John.'

class Solution:
    def countSegments(self,s):
        wordNum=0
        for i in range(len(s)):
            if s[i]!=' ' and (i==0 or s[i-1]==' '):
                wordNum+=1
                pass
            pass
        return wordNum
    pass

if __name__=='__main__':
    a=Solution()
    print(a.countSegments(s))
