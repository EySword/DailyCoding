List=[[100,1100],[1000,2000],[5500,6500]]
number=6000

class Solution:
    def inInterval0(self,List,number):
        listLen=len(List)
        isIn=False
        for i in range(listLen):
            if 0<number-List[i][0]<1000:
                isIn=True
                break
        return isIn

    def inInterval1(self,List,number):
        listLen=len(List)
        high=listLen-1
        low=0
        while high>=low:
            mid=(high+low)//2
            judge=number-List[mid][0]
            if 0<=judge<=1000:
                return True
            if judge<0:
                high=mid
            if judge>0:
                low=mid+1
        return False


if __name__=="__main__":
    a=Solution()
    print(a.inInterval1(List,number))