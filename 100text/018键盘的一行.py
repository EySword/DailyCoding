a=['Hello','Alaska',"Dad",'Peace']

class Solution:
    def findWords(self,a):
        wordList='asdfghjklASDFGHJKL'
        outLise=[]
        for item in a:
            isIn=True
            for word in item:
                if word in wordList:
                    continue
                else:
                    isIn=False
                    break
            if not isIn:
                continue
            else:
                outLise.append(item)
        return outLise

if __name__=="__main__":
    m=Solution()
    print(m.findWords(a))