array=[1,2,3,3,4,5,10]

def binarySearch0(array,target):
    index=0
    lenth=len(array)
    for i in range(lenth):
        if array[i]==target:
            return i
        if i==lenth-1:
            return '-1'
        pass
    pass

def binarySearch1(array,target):
    find=False
    start=0
    end=len(array)-1
    out=[]
    while start<=end:
        mid = (end + start) // 2
        value = array[mid]
        if value==target:
            find=True
            out.append(mid)
        if value <target:
            start=mid+1
        else:
            end=mid-1
            pass
        pass
    out.sort()
    if find:
        return out[0]
    else:
        return -1

def binarySearch2(array,target,start=0,end=len(array)-1,out=[]):
    mid=(start+end)//2
    if array[mid]==target:
        out.append(mid)
        print(out)
        pass
    if start==end:
        return out
    if array[mid]<target:
        return binarySearch2(array,target,mid+1,end,out)
    if array[mid]>target:
        return binarySearch2(array,target,start,mid-1,out)

class Solution:
    def binarySearch(self,nums,target):
        return self.search(nums,0,len(nums)-1,target)
    def search(self,nums,start,end,target):
        if start>end:
            return -1
        mid=(start+end)//2
        if nums[mid]>target:
            return self.search(nums,start,mid,target)
        if nums[mid]==target:
            return mid
        if nums[mid]<target:
            return self.search(nums,mid,end,target)

a=Solution()
print(a.binarySearch(array,3))