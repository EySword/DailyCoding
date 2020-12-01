nums1=[4,1,2]
nums2=[1,3,4,2]

class Solution:
    def nextGreatElement0(self,nums1,nums2):
        lenNums1=len(nums1)
        outList=[-1]*lenNums1
        for i in range(lenNums1):
            value=nums1[i]
            indexIn2=nums2.index(nums1[i])
            for item in nums2[indexIn2:]:  #不+1避免越界
                if item > value:
                    outList[i]=item
                    break
            pass
        return outList
    def nextGreatElement1(self,nums1,nums2):
        nextElement={}
        outList=[]
        lenthNums2=len(nums2)
        for i in range(lenthNums2):
            value=nums2[i]
            nextElement[value]=-1
            for j in range(i,lenthNums2):
                if nums2[j]>value:
                    nextElement[value]=nums2[j]
                    break
                pass
            pass
        for i in nums1:
            outList.append(nextElement[i])
            pass
        return outList
    def nextGreatElement2(self,nums1,nums2):
        nextElement={}
        stack=[] #这里的元素只可能是降序排列的
        for item in nums2:
            while stack and stack[-1]<item:
                nextElement[stack[-1]]=item
                del stack[-1]
            stack.append(item)
            pass
        for item in stack:
            nextElement[item]=-1
            pass
        return [nextElement[item] for item in nums1]
    pass

if __name__=='__main__':
    s=Solution()
    print(s.nextGreatElement2(nums1,nums2))