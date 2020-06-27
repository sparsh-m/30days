#https://www.geeksforgeeks.org/job-sequencing-problem/
"""
1) Sort all jobs in decreasing order of profit.
2) Iterate on jobs in decreasing order of profit.For each job ,
 do the following :
					a)Find a time slot i, such that slot is empty 
					and i < deadline and i is greatest.Put the job in
					this slot and mark this slot filled.
					b)If no such i exists, then ignore the job.
"""
