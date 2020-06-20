#3 sum two pointers
def solve(nums, target):
    triplets = set()
    for i in range(len(nums)):
        l=0
        r=len(nums)-1
        while l<r:
            if l==i:
                l+=1
            if r==i:
                r-=1
            if nums[l]+nums[r] == target-nums[i]:
                temp = set()
                temp.add(nums[i])
                temp.add(nums[l])
                temp.add(nums[r])
                triplets.add(tuple(temp))
                break
            elif nums[l]+nums[r] > target-nums[i]:
                r-=1
            elif nums[l]+nums[r] < target-nums[i]:
                l+=1   
    return triplets


#3sum hash set
def sum3(nums, target):
    solution=[]
    for i in range(len(nums)):
        s = set()
        curr = target-nums[i]
        for j in range(i+1, len(nums)):
            if curr-nums[j] in s:
                solution.append([nums[i], nums[j], curr-nums[j]])
                break
            else:
                s.add(nums[j])
    return solution

#print(sum3([1, 4, 45, 6, 10, 8],22))

#4sum two pointers as it uses less memory
def fourSum_twoPointer(nums, target):
    n = len(nums)
    if n<4:
        return []
    nums.sort()
    solution=set()        
    for i in range(n):
        for j in range(i+1,n):
            curr = target-nums[i]-nums[j]
            l=0
            r=n-1
            while l<r:
                while l==i or l==j:
                    l+=1
                while r==i or r==j:
                    r-=1
                
                if l>=r:
                    break

                if nums[l]+nums[r] == curr:
                    temp = [nums[i],nums[j],nums[l],nums[r]]
                    #print(temp)
                    temp.sort()
                    solution.add(tuple(temp))
                    l+=1
                elif nums[l]+nums[r] > curr:
                    r-=1
                elif nums[l]+nums[r] < curr:
                    l+=1

    s=[]
    for i in solution:
        s.append(list(i))

    return s

nums=[-3,-2,-1,0,0,1,2,3]
target=0
print(fourSum_twoPointer(nums,target))