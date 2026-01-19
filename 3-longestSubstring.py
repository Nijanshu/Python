def lengthOfLongestSubstring(s):
    first=s[0]
    long=0
    f=0
    i=0
    # for i in range(1,len(s)):
    while i < len(s):
        if s[i]==first:
            first=s[i+1]
            print (f"first: {i} "+first)
            if(long<i-f):
                long=i-f
                print (f"long: {long}")
            f=i+1
            i+=1
        for j in range(i+1,len(s)):
            if(s[j]!=s[i]):
                

        i+=1

    return long


print(lengthOfLongestSubstring('pwwkew'))


