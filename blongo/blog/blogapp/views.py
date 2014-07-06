from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Post
import datetime

def index(request):

    # Get all posts from DB
    posts = Post.objects 
    return render_to_response('index.html', {'Posts': posts,'right':'0',},
                              context_instance=RequestContext(request))

def login(request):
    if request.method=='GET': 
       return render_to_response('login.html')
    else:
        name=request.POST['username']
        password=request.POST['userpwd']
        if name=='vincent' and password=='123' :
            return render_to_response('admin.html',{},context_instance=RequestContext(request))


def add(request):
    if request.method == 'POST':
       # save new post
       title = request.POST['title']
       content = request.POST['content']
       post = Post(title=title)
       post.last_update = datetime.datetime.now() 
       post.content = content
       post.save()
       template = 'index.html'
    else :
        template='add.html'
    
    params = {'Posts': Post.objects}
    return render_to_response(template, params, context_instance=RequestContext(request))
         

       

def update(request):
    id = eval("request." + request.method + "['id']")
    post = Post.objects(id=id)[0]
    
    if request.method == 'POST':
        # update field values and save to mongo
        post.title = request.POST['title']
        post.last_update = datetime.datetime.now() 
        post.content = request.POST['content']
        post.save()
        template = 'index.html'
        params = {'Posts': Post.objects} 

    elif request.method == 'GET':
        template = 'update.html'
        params = {'post':post}
   
    return render_to_response(template, params, context_instance=RequestContext(request))
                              

def delete(request):
    id = eval("request." + request.method + "['id']")

    if request.method == 'POST':
        post = Post.objects(id=id)[0]
        post.delete() 
        template = 'index.html'
        params = {'Posts': Post.objects} 
    elif request.method == 'GET':
        template = 'delete.html'
        params = { 'id': id } 

    return render_to_response(template, params, context_instance=RequestContext(request))
                              
    
