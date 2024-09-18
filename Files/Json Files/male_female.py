# read data.json and write male users and into the male.json and female user into the female.json
import json

fp1=open('data.json','r')
users=json.load(fp1)

print(type(users))
print(len(users))

male_users=list(filter(lambda user:user["gender"]=="Male",users))
fp2=open('male.json','w')
print(len(male_users))
print('Male  data created successfully')

female_users=list(filter(lambda user:user['gender']=="Female",users))
fp3=open('female.json','w')
print(len(female_users))
print('Female data created successfully')

json.dump(male_users,fp2)
json.dump(female_users,fp3)

fp1.close()
fp2.close()
fp3.close()