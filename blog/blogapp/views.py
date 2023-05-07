from django.shortcuts import render
from blogapp.models import Blog

def home(request):
    return render(request,'home.html',{})

def addblog(request):
    return render(request,'addblog.html',{})

def viewblogs(request):
    blogs=Blog.objects.all()
    return render(request,'viewblogs.html',{'blogs':blogs})

def addtodb(request):
    title1 = request.POST.get('title')
    desc1 = request.POST.get('desc')
    blog1 = request.POST.get('blog')

    blog = Blog(title=title1,description=desc1,text=blog1)
    blog.save()
    return render(request,'home.html',{})


