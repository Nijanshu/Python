import random
import string

def rand(i):
    # Characters can be letters, digits, or punctuation symbols
    characters = string.ascii_letters

# Generate a random three-character string
    return ''.join(random.choice(characters) for _ in range(3))



def code(msg):
    msg=msg.split(' ')
    code=[]
    for i in msg:
        print(i)
        if(len(i)<3):
            code.append( i[::-1])
        else:
            sec=''
            sec+=i[1:]
            sec+=i[0]

            sec+=rand(3)
            sec=rand(3)+sec
            print(sec)
            code.append(sec)
    code=' '.join(code)
    return code

def decode(code):
    code=code.split(' ')
    decode=[]
    for i in code:
        if(len(i)<3):
            decode.append(i[::-1])#reverse
        elif(len(i)>8):
            msg=i[3:]# remove first thre
            msg2=msg[:-3] #remove last three
            fr=msg2[-1] #get last
            msg3=msg2[:-1] #remove last
            decode.append(fr+msg3) #add last to first
        else:
            return("Not able to decode")

    decode=' '.join(decode)
    return decode


msg=input('Enter msg')
print(decode(msg))
