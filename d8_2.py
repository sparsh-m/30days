#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
#Activity Selection
def solution(points):
	last = float('-inf')
	points.sort(key = lambda i:i[1])
	count=0
	for i in range(len(points)):
		if last < points[i][0]:
			count+=1
			last = points[i][1]
	return count
#arr = [[10,16], [2,8], [1,6], [7,12]]
arr = [[1,12],[2,8],[3,7],[9,11]]
print(solution(arr))
