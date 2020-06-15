from django.shortcuts import render,HttpResponse,redirect
from .models import Post,BlogComment
from django.contrib import messages
from .forms import PostForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import datetime
# Create your views here.
def blog(request):
    allPosts = Post.objects.all()
    week_ago = datetime.date.today() - datetime.timedelta(days=7)
    trends = Post.objects.filter(timeStamp__gte=week_ago).order_by('-read')
    context = {'allPosts':allPosts,'trends':trends}
    return render(request,'blog/bloghome.html',context)
def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    context = {'post':post,'comment':comments}
    return render(request,'blog/blogpost.html',context)
def blogComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postsno = request.POST.get('postsno')
        post = Post.objects.get(sno=postsno)
        comment = BlogComment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request, 'your comment has been posted successfully')
    return redirect(f'/blog/{post.slug}')
def trending(request):

    return render(request,'blog/trend.html',context)