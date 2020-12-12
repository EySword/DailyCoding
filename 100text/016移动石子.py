arr=[5,4,1]

class Solution:
    def movingStones(self,arr):
        odd=0
        even=0
        arr.sort()
        lenArr=len(arr)
        for i in range(lenArr):
            even+=abs(arr[i]-1-2*i)
            odd+=abs(arr[i]-1-(2*i+1))
            pass
        print(odd,even)
        return min(odd,even)



if __name__=="__main__":
    a=Solution()
    print(a.movingStones(arr))