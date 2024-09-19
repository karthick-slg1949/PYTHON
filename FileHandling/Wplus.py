# W+ : write and read mode
st='welcome to bangalore makkaley'

fp=open('statement.txt','w+')
fp.write(st)

fp.read()
print(st)
fp.close()