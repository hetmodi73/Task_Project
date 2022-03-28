from django.shortcuts import render

# Create your views here.

def blog_grid(request):
    return render(request,"blog/blog_grid.html")

def blog_sidebar(request):
    return render(request,"blog/blog_sidebar.html")

def blog_single(request):
    return render(request,"blog/blog_single.html")
