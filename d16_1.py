#Z Algorithm
"""
Z(K): longest substring starting at Kwhich is also prefix of string

text = xabcabzabc
pattern = abc
$ is the special character used to separate
new string = abc$xabcabzabc
Z          = 00000300200300


Time Complexity:O(m+n)
"""
def ZAlgorithm(s):
    #Assign a z arr and let left and right be 0
    z = [0]*len(s)
    left, right = 0,0
    #i=1 since 0th element can't have a prefix
    i=1
    while i<len(s):
        #i lies outside zbox
        if i >= right:
            #starts matching from first element
            k=0
            count=0
            #k<i to ensure only preceeding elements are matched
            #i+k<len(s) to ensure bound
            while i+k<len(s) and k<i:
                if s[k]==s[i+k]:
                    count+=1
                    k+=1
                else:
                    break
            z[i] = count
            #makes a zbox
            left = i
            right = i + count
            i+=1
        else:
            #z box is created when there seems to be an exact repition of prev pattern
            #Since inside the zbox the first element starts from k=1
            k=1
            while i<len(s) and i<right:
                #boundry condition
                if z[k]+i< right:
                    #if satisfies can assign value without comparing
                    z[i] = z[k]
                    k+=1
                    i+=1
                else:
                    #if bound condition is broken assign new zbox
                    left = right = i
                    break
    print(z)

ZAlgorithm("abcabcabcabc")