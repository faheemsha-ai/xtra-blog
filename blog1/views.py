from django.shortcuts import render, redirect
from . models import Post
from . forms import PostForm , LoginForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm 


def index(request):
    item = Post.objects.all()
    return render(request,'index.html' ,{"item" : item})
## about page
def about(request):
    return render(request,'about.html')
##contact
def contact(request):
    return render(request,'contact.html')
##post
def post(request,id):
    post=Post.objects.get(id=id)
    return render(request,'post.html',{"post":post})
##edit 
@login_required
def edit(request,id):
    data = Post.objects.get(id=id)
    form = PostForm(instance=data)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,'editing.html',{"form":form})
##delete
@login_required
def delete(request,id):
    remove = Post.objects.get(id=id)
    if request.method == 'POST':
        remove.delete()
        return redirect("/")
    return redirect("/")
## create
@login_required
def create(requets):
    form = PostForm()
    if requets.method == 'POST':
        form = PostForm(requets.POST, requets.FILES)
        if form.is_valid():
            form.save()
            form = PostForm()
            return redirect("/")
    return render(requets,'create.html',{"form":form})

##registaration
def signup(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login")
    return render(request,'singup.html',{"form":form})


## LOGIN
def login(requets):
    form = LoginForm()
    if requets.method == 'POST':
        form = PostForm(requets.POST)
        if form.is_valid():
            form.save()
            form = LoginForm()
            return redirect("/")
    return render(requets,'login.html',{"form":form})