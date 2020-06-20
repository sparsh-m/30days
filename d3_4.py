#https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/submissions/
#euclid gcd i reverse fib therefore it is O(log N)
def gcd(x, y):
    return y if x==0 else gcd(y%x, x)

def hasGroupsSizeX(deck):
    import collections
    from functools import reduce
    vals = collections.Counter(deck).values()
    return reduce(gcd, vals) >=2
