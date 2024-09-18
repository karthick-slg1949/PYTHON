fp1=open('data.txt','r')
data=fp1.read()

fp=open('city1.txt','x')
fp.write(data)
print('file created')

fp1.close()
fp.close()

