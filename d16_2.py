#KMP Algorithm
def ta(pattern):
    i,j = 1,0
    arr = [0]*len(pattern)
    while i<len(pattern):
        #If the characters match
        #arr[i] = j+1
        if pattern[i] == pattern[j]:
            arr[i] = 1 + j
            j+=1
            i+=1
        else:
            #in case the characters don't match
            #let j be arr[j-1]
            if j!=0:
                j = arr[j-1]
            else:
                arr[i] = 0 
                #i moves ahead to the next element
                i+=1
    return arr

ta("aabaabaaa")

def KMP(pattern, text):
    tp = ta(pattern)
    i,j = 0,0
    while i<len(text) and j<len(pattern):
        if text[i] == pattern[j]:
            i+=1
            j+=1
        else:
            if j!=0:
                j = tp[j-1]
            else:
                i+=1
        #string match
        if j==len(pattern):
            return True
    return False
pattern = "aq"
text = "abababab"
res = KMP(pattern, text)
print(res)
