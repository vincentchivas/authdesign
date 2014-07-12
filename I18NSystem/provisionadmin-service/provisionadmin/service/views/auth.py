from model.auth import AuthUser

def login(request):
    try:
        name=request.POST['username']
        password=request.POST['password']
        user=AuthUser(name,password)
        


