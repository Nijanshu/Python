def lengthOfLastWord(s):
    s=s.strip()
    ls=s.split(' ')
    return len(ls[-1])

s="   fly me   to   the moon "
print(lengthOfLastWord(s))