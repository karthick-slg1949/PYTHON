# clear error message : file exists error

fp=open('svg.txt','x')
fp.write('exclusive creation mode for write operation')
fp.close()