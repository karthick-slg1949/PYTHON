emp={
    'eid':101,
    'ename':"karthick",
    'esal':56000
}

for key in emp.keys():
    print(key)
print("-------------")

for key in emp.values():
    print(key)
print("-------------")

for value in emp.values():
    print(value)
print("-------------")

for key,value in emp.items():
    print(key,":",value)