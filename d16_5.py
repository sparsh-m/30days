#https://leetcode.com/problems/count-and-say/
def countAndSay(n):
    num = '1'
    for k in range(n):
        i,j = 0,0
        s = ''
        #Count the number of continous
        #occurances of a digit
        while j<len(num):
            if num[i]==num[j]:
                j+=1
            else:
                #Append the number of occurances
                #append the said digit
                s+=str(j-i)
                s+=num[i]
                i=j
        s+=str(j-i)
        #append the said digit
        s+=num[j-1]
        if k==n-1:
            return num
        num=s

print(countAndSay(40))