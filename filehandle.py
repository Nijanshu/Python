f=open('hi.text','r')
fs=open('hello.text','w')
# print(f.readline())
# print(f.readline())
# # print(f.readline())
# # print(f.readline())

f.seek(10)  #10th from first
fs.write(f.readline())  #  write content of one file to another
# print(f.tell()) #tells the starting/current position
fs.truncate(3) #
# print(f.read())
f.close() # close
# fs.close() # close


