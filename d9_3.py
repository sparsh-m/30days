#backtrackinf solution for https://leetcode.com/problems/flower-planting-with-no-adjacent/submissions/
def gardenNoAdj(N, paths):
    answer = [0 for i in range(N)]
    solve(paths,1,N,answer)
    return answer

def isSafe(paths,gardenNo,flower,answer):
    options = set()
    #Make a set of all the neighbouring vertices
    for i in range(len(paths)):
        if gardenNo in paths[i]:
            options.add(paths[i][0])
            options.add(paths[i][1])
        if len(options)>4:
            break
    #print(gardenNo, list(options))
    #If the neighbouring gardens have the
    #flower return false
    for i in options:
        if answer[i-1]==flower:
            return False
    return True

def solve(paths,gardenNo,n,answer):
    #Base case if flowers for all gardens have been selected
    if gardenNo>n:
        return True
    #Only four distinct colors are possible due to
    #coloring theorem
    flowers = [1,2,3,4]
    for flower in flowers:
        if isSafe(paths,gardenNo,flower,answer):
            #assign the flower if its safe
            answer[gardenNo-1] = flower
            if solve(paths,gardenNo+1,n,answer):
                return True
    return False

N = 6
paths = [[1,2],[1,3],[1,4],[1,5],[1,6]]
print(gardenNoAdj(N, paths))


#also check graph submission
def gardenNoAdj_graph( N, paths):
        graph = [[] for i in range(N)]
        for x,y in paths:
            graph[x-1].append(y-1)
            graph[y-1].append(x-1)
        
        ans = [0 for i in range(N)]
        for i in range(N):
            used_color = []
            for j in graph[i]:
                used_color.append(ans[j])
            for color in range(1,5):
                if color not in used_color:
                    ans[i]=color
                    break
        return ans