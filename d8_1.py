#https://www.geeksforgeeks.org/find-maximum-meetings-in-one-room/
arr = [[1,2],[3,4],[0,6],[5,7],[8,9],[5,8]]
a = sorted(arr, key = lambda x:x[1])
ans=[]
ans.append(1)
for i in range(1,len(a)):
	if a[ans[-1]-1][1]<a[i][0]:
		ans.append(i+1)
print ans
		
