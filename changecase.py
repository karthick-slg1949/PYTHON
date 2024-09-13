def change_case(func):
    def inner(name):
        return 'HI_'+name.upper()
    return inner

@change_case
def display(name):
    print(name)
display('vinoth')
display('alagar')