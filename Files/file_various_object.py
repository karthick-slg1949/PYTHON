fp=open('one.txt','w')
print(fp.name)
print(fp.mode)
print(fp.readable())
print(fp.writable())

fp.close()
print(fp.closed)