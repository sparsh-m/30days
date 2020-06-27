#https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
tasks = ['A','A','A','B','B','B','C','C','C','D','D']
n=2
frequencies = [0] * 26
for t in tasks:
	frequencies[ord(t) - ord('A')] += 1
print(frequencies)
# max frequency
f_max = max(frequencies)
# count the most frequent tasks
n_max = frequencies.count(f_max)

q = max(len(tasks), (f_max - 1) * (n + 1) + n_max)
print((f_max - 1) * (n + 1) + n_max)
