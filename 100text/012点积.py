A=[1,1,1]
B=[2,2,2]

class Solution:
    def dotProduct(self,A,B):
        lenA=len(A)
        lenB=len(B)
        res=0
        if lenA!=lenB or lenA==lenB==0:
            return -1
        for i in range(lenA):
            res=res+A[i]*B[i]
            pass
        return res


if __name__=='__main__':
    a=Solution()
    print(a.dotProduct(A,B))