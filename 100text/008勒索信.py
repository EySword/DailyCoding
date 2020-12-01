import time
ransomNote='aamnde".%w "'
magazine='aarenmsd"" ""ewq .%,/'

class Solution:
    def canConstruct0(self,ransomNote,magazine):
        for ransomItem in ransomNote:
            isFind=False
            for magItem in magazine:
                if ransomItem==magItem:
                    isFind=True
                    magazine=magazine.replace(magItem,'',1)
                    break
            if not isFind:
                return False
        return True

    def canConstruct1(self,ransomNote,magazine):
        magWord={}
        for item in magazine:
            if item not in magWord.keys():
                magWord[item]=1
            else:
                magWord[item]+=1
                pass
            pass
        for item in ransomNote:
            if item in magWord.keys() and magWord[item]>0:
                magWord[item]-=1
                continue
            else:
                return False
        return True

if __name__=='__main__':
    a=Solution()
    print(a.canConstruct1(ransomNote,magazine))
