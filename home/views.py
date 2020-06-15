from django.shortcuts import render,HttpResponse,redirect,Http404
from .models import Contact
from django.db import IntegrityError
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog.forms import PostForm
# Create your views here.
def home(request):
    return render(request,('home/home.html'))
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<5:
            messages.error(request,'please fill form correctly')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,'your message has been sent successfully')

    return render(request,'home/contact.html')
def about(request):
    return render(request,'home/about.html')
def seach(request):
    search = request.GET['search']
    if len(search) > 50:
        allPosts = []
    else:
        allPostsTitle = Post.objects.filter(title__icontains=search)
        allPostsContent = Post.objects.filter(content__icontains=search)
        allPostsAuthor = Post.objects.filter(author__icontains=search)
        allPosts = allPostsTitle.union(allPostsContent,allPostsAuthor)
    context = {'allPosts':allPosts,'search':search}
    return render(request,'home/search.html',context)
def signup(request):
    if request.method == 'POST':
        UserName = request.POST['UserName']
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        email = request.POST['email']
        Password = request.POST['Password']
        Confirm = request.POST['confirm']
        #check for errors
        if len(UserName)>10:
            messages.error(request,"username must be under 10 characters")
            return redirect('home')
        if not UserName.isalnum():
            messages.error(request,"username should only contains letters and numbers")
            return redirect('home')
        if Password != Confirm:
            messages.error(request,"password do not match ")
            return redirect('home')
        # create user
        try:
            myuser = User.objects.create_user(UserName,email,Password)
            myuser.first_name = FirstName
            myuser.last_name = LastName
            myuser.save()
            messages.success(request,"your account has been successfully created")
            return redirect(('home'))
        except IntegrityError:
            messages.error(request,'username already exist')
            return redirect(('home'))

    else:
        return HttpResponse('404 - Not Found')
def handlelogin(reuest):
    if reuest.method == 'POST':
        loginusername = reuest.POST['user']
        loginpass = reuest.POST['pass']
        user = authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(reuest,user)
            messages.success(reuest,'You LoggedIn SuccessFully')
            return redirect(('home'))
        else:
            messages.error(reuest,'Invalid Credentials')
            return redirect(('home'))
    return HttpResponse('404- Not found')
def handlelogout(request):
    logout(request)
    messages.success(request,"successfully logged out")
    return redirect('home')
def create_post(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {'form':form}
    return render(request,'blog/create_post.html',context)
