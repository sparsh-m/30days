#https://leetcode.com/problems/trapping-rain-water/
def trap(arr):
	left = 0
	right = len(arr)-1
	leftmax = 0
	rightmax = 0
	ans=0
	while left<right:
		if arr[left]<arr[right]:
			if arr[left]>=leftmax:
				leftmax = arr[left]
			else:
				ans+=(leftmax-arr[left])
			left+=1
		else:
			if arr[right]>=rightmax:
				rightmax = arr[right]
			else:
				ans+=(rightmax-arr[right])
			right-=1
	return ans
a = [1,2,4,0,3,2,1]
ans = trap(a)
print ans
