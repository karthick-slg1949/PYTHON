def login_required(func):
    def inner(name,is_login):
        if is_login==False:
            print('Login is required')
        else:
            func(name,is_login)
    return inner
        
def home_page(name,is_login):
    print('home page')
@login_required
def about_page(name,is_login):
    print('about page')
@login_required
def order_page(name,is_login):
    print('order page')

    
home_page('karthi',False)
about_page('karthi',False)
order_page('karthi',False)