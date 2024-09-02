#18. Program Factors of 24 using while loopExample : Factors of 24 are (1,3,4,6,8,12,24)


number=24

i=1

factors=[]
while i<=number:
    if number % i==0:
        factors.append(i)
    i +=1
print("factors of",number,"are",factors)
    