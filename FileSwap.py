ff=open("E:\\dummy\\a.txt","r")
str=ff.read()
ff1=open("E:\\dummy\\b.txt","r")
str1=ff1.read()
ff2=open("E:\\dummy\\a.txt","w")
ff2.write(str1)
ff2.close()
ff3=open("E:\\dummy\\b.txt","w")
ff3.write(str)
ff3.close()