from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import user

# Create your views here.
@login_required

def index(request):
    return render(request,"client/index.html")

# def about(request):
#     return render(request,"client/about.html")

# def blog_grid(request):
#     return render(request,"client/blog_grid.html")
#
# def blog_sidebar(request):
#     return render(request,"client/blog_sidebar.html")
#
# def blog_single(request):
#     return render(request,"client/blog_single.html")

# def contact(request):
#     return render(request,"client/contact.html")

# def pricing(request):
#     return render(request,"client/pricing.html")

# def project(request):
#     return render(request,"client/project.html")

# def service(request):
#     return render(request,"client/service.html")

# def feedback(request):
#     return render(request,"client/feedback.html")

def user_list(request):
    return render(request, "client/user_list.html")

def user_detail(request):
    return render(request, "client/user_detail.html")

def user_confirm_delete(request):
    return render(request, "client/user_confirm_delete.html")

class NewUserView(CreateView):
    model = user
    fields = '__all__'
    template_name = 'client/index.html'
    #success_url = 'client/user_list.html'

class ListUserView(ListView):
    model = user
    context_object_name = 'client'
    template_name = 'client/user_list.html'

class UpdateUserView(UpdateView):
    model = user
    fields = '__all__'
    template_name = 'client/index.html'

class DetailUserView(DetailView):
    model = user
    fields = '__all__'
    success_url = '/client/view'

class DeleteUserView(DeleteView):
    model = user
    success_url = '/client/view'
