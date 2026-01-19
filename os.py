import os
import shutil

# os.mkdir(f"notes/")
# os.chdir(f"notes/maker/")

# for i in range(1,100):  # does not counts last one ie 100
#     os.mkdir(f"maker/Note {i}")
    # os.rename(f"notes/Note {i}",f"notes/Page {i}")
# os.mkdir(f"maker")
# notes= os.listdir("notes")
# print(notes)



print(os.getcwd())
shutil.rmtree("notes") #removes evrything
# for i in range(1,100):
#     i=str(i)
#     print(i)
#     print(type(i))

# for page in notes:
#     print(page)
    # os.rmdir(f"vari/{page}")

# os.rmdir('notes')