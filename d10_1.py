def combinationSum(candidates,target):
	candidates.sort()
	res=[]
	helper(candidates,target,res,0,[])
	return res

def helper(candidates,target,res,total,subset):
	if total>=target:
		if total==target:
			#print(subset)
			flag = True
			for k in res:
				if k==sorted(subset):
					flag=False
			if flag:
				res.append(sorted(subset))
	else:
		for i in range(len(candidates)):
			helper(candidates,target,res,total+candidates[i],subset+[candidates[i]])

a=[7,3,2]
n=18
l=combinationSum(a,n)
print(l)
