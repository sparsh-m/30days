#https://leetcode.com/problems/merge-intervals/

"""
1)Sort the intervals on the basis of their starting points.
2)let merged be the final list of merged elements
3)If merged is empty or the start of the an interval is greater than
the interval preceeding it, add the interval to merged.
4)If if the start of an interval is smaller than or equal to the end
of the previous one the merge the intervals.
The start if this merged interval is the start of the preceeding interval
and it's end is the max of the end of the preceeding element and the 
suceeding element.
5)Repeat step 3 and 4 for all intervals.

Time Complexity: O(nlog(n))
Space Complexity: O(1), in case of an in place sort 
"""
def solve(intervals):
    intervals.sort(key=lambda i:i[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1]<interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
a = [[1,3],[4,16],[5,7],[8,9]]
print(solve(a))
