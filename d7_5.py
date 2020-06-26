#https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n<1:
            return 0
        i=0
        j=0
        ans=1
        while j<n:
            if nums[i]==nums[j]:
                j+=1
            else:
                i+=1
                nums[i]=nums[j]
                ans+=1
        print(ans)
        return ans
