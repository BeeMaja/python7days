#straight forward
print("Hello world")

#variable string
hello = "Hello"
hello += " world"
print(hello)

#for loop
for n in hello:
    print(n, end='')
print('') #for newline

#while loop
i = 0
while i < len(hello):
    print(hello[i], end='')
    i+=1
print('') #for newline

#function
def helloW():
    print ('Hello world')
helloW()

#from file
fh = open('hello.txt','r')
print (fh.read())
fh.close()
