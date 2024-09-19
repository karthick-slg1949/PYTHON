# r+ mode: read and write data into file.
# file has data? in the file ,will not be deleted

fp=open('svg.txt','r+')
data=fp.read()
fp.write('King of the south district')

fp.close()