ff=open("b.txt","r")
print(ff.tell())
str=ff.read(10)
print(ff.tell())
ff.close()