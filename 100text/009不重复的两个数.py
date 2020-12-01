a=[3,2,7,5,5,7,3,9,10,9]

class Solution:
    def theTwoNumbers0(self,a):
        outNum=[]
        aSingle=set(a)
        # print(aSingle)
        for item in aSingle:
            a.remove(item)
            if not (item in a):
                    outNum.append(item)
                    pass
            pass
        # print(a)
        return outNum

    def theTwoNumbers1(self,a):
        outList=[0,0]
        findDifferent=1
        for item in a:
            outList[0]=outList[0]^item
            pass
        while findDifferent&outList[0]!=findDifferent:
            findDifferent=findDifferent<<1
            pass
        for item in a:
            if findDifferent&item==findDifferent:
                outList[1]=outList[1]^item
                pass
            pass
        outList[0]=outList[0]^outList[1]
        return outList



if __name__=='__main__':
    m=Solution()
    print(m.theTwoNumbers1(a))


