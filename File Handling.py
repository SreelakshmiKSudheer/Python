with open("file.txt","r+") as myfile:
    print("Content:")
    print(myfile.read())
    
    myfile.write("I am fine")
    
    print("Content:")
    print(myfile.read())
myfile.close()

'''
File opening modes
"r" : read
"w" : write
"a" : append
"r+": read and write
'''