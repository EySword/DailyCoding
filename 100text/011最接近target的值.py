target=16
array=[1,3,5,11,7]

class Solution:
    def chosestTargetValue(self,target,array):
        lenArray=len(array)
        error=target
        out=[0,0]
        for i in range(lenArray-1):
            for j in range(i,lenArray):
                res=array[i]+array[j]
                if 0 <= (target-res) < error:
                    error=target-res
                    out[0]=array[i]
                    out[1]=array[j]
                    pass
                pass
            pass
        maxres=out[0]+out[1]
        print(maxres,'{}+{}={}'.format(out[0],out[1],maxres))



if __name__=="__main__":
    a=Solution()
    a.chosestTargetValue(target,array)
