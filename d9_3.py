#backtrackinf solution for https://leetcode.com/problems/flower-planting-with-no-adjacent/submissions/
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        answer = [0 for i in range(N)]
        self.solve(paths,1,N,answer)
        return answer
    
    def isSafe(self,paths,gardenNo,flower,answer):
        options = set()
        for i in range(len(paths)):
            if gardenNo in paths[i]:
                options.add(paths[i][0])
                options.add(paths[i][1])
            if len(options)>4:
                break
        #print(gardenNo, list(options))
        for i in options:
            if answer[i-1]==flower:
                return False
        return True
    
    def solve(self,paths,gardenNo,n,answer):
        if gardenNo>n:
            return True
        flowers = [1,2,3,4]
        for flower in flowers:
            if self.isSafe(paths,gardenNo,flower,answer):
                #print(gardenNo)
                #print(answer)
                answer[gardenNo-1] = flower
                if self.solve(paths,gardenNo+1,n,answer):
                    return True
        return False
#also check graph submission
