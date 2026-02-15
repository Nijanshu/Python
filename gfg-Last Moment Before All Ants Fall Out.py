# https://www.geeksforgeeks.org/problems/last-moment-before-all-ants-fall-out-of-a-plank/1

# We have a wooden plank of length n units. Some ants are walking on the plank, each ant moves with a speed of 1 unit per second, with some moving left and others right.
# When two ants moving in two different directions meet at some point, they change their directions and continue moving again. Assume changing directions does not take any additional time. When an ant reaches one end of the plank at a time t, it falls out of the plank immediately.

# Given an integer n and two integer arrays left[] and right[], the positions of the ants moving to the left and the right, return the time when the last ant(s) fall out of the plank.

# Examples :

# Input: n = 4, left[] = [2], right[] = [0, 1, 3]
# Output: 4
        
# Explanation: As seen in the above image, the last ant falls off the plank at t = 4.

n = 4
# n=float(n)
left= [2]
right= [0, 1, 3]

for i in range(0,n*2):
    print(i/2)
    for j in left:
        j+=1