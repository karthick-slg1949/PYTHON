#Positional Argument
def sub(a,b):
    print("Positional Argument",a+b)
    
sub(10,20)#10,20 is positional argument 
sub(20,10)

print("----------")

def add(c,d):
    print("positional Argument",c-d)
    
add(10,20)
add(20,10)

print("----------")
#Keyword Argument
def sam(e,f):
    print("Keyword Argument",e-f)
    
sam(e=10, f=20)
sam(f=20, e=10)#e=10,f=20 is keyword argument

print("----------")
#Default argument
def sum(x,y,z=100):
    print("Default Argument",x+y+z)
    
sum(10,20,30)
sum(10,20)

print("----------")

def ram(*a):
    print(a)
ram(10)
ram(10,20)
ram(10,20,30)
ram(10,20,30,40)
ram(10,20,30,40,50)

print("----------")
def add():
    return 10
print(add())