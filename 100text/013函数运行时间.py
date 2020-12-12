s=['F1 Enter 10','F2 Enter 18','F2 Exit 19','F1 Exit 20']
s1=["F1 Enter 10","F1 Exit 18","F1 Enter 19","F1 Exit 20"]
class Solution:
    def getRunTime(self,s):
        target={}
        slen=len(s)
        for i in range(slen):
            information=s[i].split(' ')
            if information[0] not in target.keys():
                target[information[0]]=0
                pass
            if information[1]=='Enter':
                target[information[0]]-=int(information[2])
            if information[1]=='Exit':
                target[information[0]]+=int(information[2])
            pass
        outList=[]
        for key in target.keys():
            outStr=key+'|'+str(target[key])
            outList.append(outStr)
            pass
        return outList



if __name__=="__main__":
    a=Solution()
    print(a.getRunTime(s1))
