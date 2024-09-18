#read the data into the data.txt and write into the silanthagudi.txt
fp1=open('data.txt','r')
data=fp1.read()

fp2=open('silanthagudi.txt','w')
fp2.write(data)

fp3=open('city.txt','a')
fp3.write(data)

print('new file created successfully')
fp1.close()
fp2.close()
fp3.close()
