def countConsistentStrings(allowed, words):
    n=0
    k=0
    for a in words:
        for b in a:
            if b in allowed:
                print(a, b,n)
                n+=1
        if(n==len(a)):
            k+=1
        
        n=0
    
    return k

# def countConsistentStrings(self, allowed, words):


#         count = 0
#         s = set(allowed)
#         for word in words:
#             for letter in word:
#                 if letter not in s:
#                     count += 1
#                     break
#         return len(words) - count
                
allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
print(countConsistentStrings(allowed, words)) 
            
        
            