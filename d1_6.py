#https://leetcode.com/problems/merge-intervals/
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