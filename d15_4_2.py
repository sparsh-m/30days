#https://leetcode.com/problems/string-to-integer-atoi/
"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
def myAtoi(self, s: str) -> int:
    #in case a minus sign is repeated
    negative_flag = 1
    #incase a plus sign is repeated
    positive_flag = -1
    #to break loop when a whitespace reappears
    whitespace_flag = 0
    #to handle if there is a space between integers
    digit_flag = 0
    res = 0
    for i in s:
        #to handle - sgn
        if i == '-':
            whitespace_flag = 1
            if positive_flag == 1 or negative_flag == -1 or digit_flag:
                return res*negative_flag
            negative_flag= -1
        #to handle + sign
        elif i == '+':
            whitespace_flag = 1
            if positive_flag == 1 or negative_flag == -1 or digit_flag:
                return res*negative_flag
            positive_flag= 1
        #in case of a digit
        elif 48<=ord(i)<58:
            whitespace_flag = 1
            digit_flag = 1
            res = res*10 + ord(i)-48
            #in case limit is surpassed
            if res>2147483647:
                return 2147483647 if negative_flag==1 else -2147483648
        #for any other 
        elif (48>ord(i) or ord(i)>=58) and ord(i)!=32:
            return res*negative_flag
        elif whitespace_flag:
            return res*negative_flag
    return res*negative_flag