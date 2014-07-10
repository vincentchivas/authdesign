from model.auth import AuthUser
def check_session(func):
    '''check user session'''
    def wrapper(request,*args,**kv):
        userinfo=request.session.get('userid')
         if not userinfo:
            return response.redirect('/login')
            return func(request,*args,**kv)
        return wrapper      


def login(request):
    try:
        name=request.POST['username']
        password=request.POST['userpwd']
        userexist=AuthUser.get(username=name,password=password)
        if userexist:
            request.session['userid']=userexist.id
            request.session['sessionkey']=Session.generate() #generate a key and stort it in database
         else:
                response.redirect('login.html')

@check_session
def adduser(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']


