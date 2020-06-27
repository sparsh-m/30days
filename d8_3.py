#https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/
#https://leetcode.com/problems/coin-change/ can't be done using greedy(causes tle)
#the below code fails for deno = [92,10,7] n=100
def findMin(V): 
      
    # All denominations of Indian Currency 
    deno = [92,10,7] 
    n = len(deno) 
      
    # Initialize Result 
    ans = [] 
  
    # Traverse through all denomination 
    i = n - 1
    while(i >= 0): 
          
        # Find denominations 
        while (V >= deno[i]): 
            V -= deno[i] 
            ans.append(deno[i]) 
  
        i -= 1
  
    # Print result 
    for i in range(len(ans)): 
        print(ans[i], end = " ") 
  
# Driver Code 
if __name__ == '__main__': 
    n = 100
    print("Following is minimal number", 
          "of change for", n, ": ", end = "") 
    findMin(n)
