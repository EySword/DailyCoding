length=15
connections=[[2,8],[6,9]]

class Solution:

    def modernLudo(self,length,connections):
        step=[i for i in range(length+1)]
        for local in range(length+1):
            for dice in range(1,7):
                if local >= dice:
                    step[local]=min(step[local],step[local-dice]+1)
                    pass
            for item in connections:
                if local==item[1]:
                    step[local]==min(step[local],step[item[0]])
                    pass
                pass
            pass
        return step[length]
