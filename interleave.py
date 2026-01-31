# https://www.geeksforgeeks.org/problems/interleave-the-first-half-of-the-queue-with-second-half/1

# Given a queue q[] of even size. Your task is to rearrange the queue by interleaving its first half with the second half.

# Interleaving is the process of mixing two sequences by alternating their elements while preserving their relative order.
# In other words, Interleaving means place the first element from the first half and then first element from the 2nd half and again second element from the first half and then second element from the 2nd half and so on....

# Examples:

# Input: q[] = [2, 4, 3, 1]
# Output: [2, 3, 4, 1]
# Explanation: We place the first element of the first half 2 and after that 
# place the first element of second half 3 and after that repeat
# the same process one more time so the resulting queue will be [2, 3, 4, 1]

q= [8 ,12, 13, 15, 9, 14, 2, 4, 20, 12]

def rearrangeQueue( q):
        #code here 
        half_len=len(q)//2

        new_q=[]
        
        for i in range(half_len):
            new_q.append(q[i])
            new_q.append(q[half_len+i])
        
        return new_q


print(rearrangeQueue(q))