class Solution:
    def findNthDigit0(self,n):
        totalStr=''
        i=1
        while len(totalStr)<n:
            totalStr+=str(i)
            i+=1
            pass
        return totalStr[n-1]

    def findNthDigit1(self,n):
        length=1 #每个数占的长度
        count=9 #一共有多少个数字
        start=0 #开始的数字（不是位数）
        while True:
            if n<=count:
                i=n//2+n%2
                cur=start+i
                return str(cur)[(n+1)%2]

            else:
                start+=count
                length+=1
                count*=10
                n-=start

if __name__=="__main__":
    a=Solution()
    print(a.findNthDigit1(11))