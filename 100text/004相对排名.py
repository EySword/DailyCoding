score=[3,4,2,1,5]


def findRelativeRanks(score):
    scoreNum={}
    sum=len(score)
    outRange=[0]*sum
    for i in range(sum):
        scoreNum[score[i]]=i
        pass

    sortScore=sorted(score,reverse=False)

    outRange[scoreNum[sortScore[0]]]='Gold Medal'
    outRange[scoreNum[sortScore[1]]]='Silver Medal'
    outRange[scoreNum[sortScore[2]]]='Bronze Medal'
    for i in range(3,sum):
        outRange[scoreNum[sortScore[i]]]=sortScore[i]
        pass

    return outRange

print(findRelativeRanks(score))


