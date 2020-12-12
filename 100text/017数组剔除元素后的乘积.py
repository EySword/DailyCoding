A=[2,4,6]

class Solution:
    def productExcludeItseli(self,A):
        lengA=len(A)
        outList=[]
        reverseList=[1 for i in range(lengA+1)]
        for i in range(lengA-1,0,-1):
            reverseList[i]=A[i]*reverseList[i+1]
            pass
        tem=1
        for i in range(lengA):
            outList.append(tem * reverseList[i+1])
            tem*=A[i]
            pass
        return outList
    pass

if __name__=="__main__":
    a=Solution()
    print(a.productExcludeItseli(A))
