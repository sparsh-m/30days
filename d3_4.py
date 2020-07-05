#https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/submissions/
"""
from collections import Counter
Creates a hash table with the number of instances of an element

from functools import reduce
At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the 
number just succeeding the second element and the result is again stored.

applying gcd to each succive element with reduce() will give the min no of similar
cards in a deck

Time Complexity: O(n), Counter and euclid gcd i reverse fib therefore it is O(log N)
Space Complexity: O(n)
"""

def gcd(x, y):
    return y if x==0 else gcd(y%x, x)

def hasGroupsSizeX(deck):
    from collections import Counter
    from functools import reduce
    vals = Counter(deck).values()
    return reduce(gcd, vals) >=2
