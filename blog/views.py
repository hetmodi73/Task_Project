from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import document,master_question,sub_question

# Create your views here.

def blog_grid(request):
    return render(request,"blog/blog_grid.html")

def document_list(request):
    return render(request, "blog/document_list.html")

def document_detail(request):
    return render(request, "blog/document_detail.html")

def document_confirm_delete(request):
    return render(request, "blog/document_confirm_delete.html")

class NewDocumentView(CreateView):
    model = document
    fields = '__all__'
    template_name = 'blog/blog_grid.html'

class ListDocumentView(ListView):
    model = document
    context_object_name = 'blog'
    template_name = 'blog/document_list.html'

class UpdateDocumentView(UpdateView):
    model = document
    fields = '__all__'
    template_name = 'blog/blog_grid.html'

class DetailDocumentView(DetailView):
    model = document
    fields = '__all__'
    success_url = '/blog/view'

class DeleteDocumentView(DeleteView):
    model = document
    success_url = '/blog/view'


def blog_sidebar(request):
    return render(request,"blog/blog_sidebar.html")

def master_question_list(request):
    return render(request, "blog/master_question_list.html")

def master_question_detail(request):
    return render(request, "blog/master_question_detail.html")

def master_question_confirm_delete(request):
    return render(request, "blog/master_question_confirm_delete.html")

class NewMaster_questionView(CreateView):
    model = master_question
    fields = '__all__'
    template_name = 'blog/blog_sidebar.html'

class ListMaster_questionView(ListView):
    model = master_question
    context_object_name = 'blog'
    template_name = 'blog/master_question_list.html'

class UpdateMaster_questionView(UpdateView):
    model = master_question
    fields = '__all__'
    template_name = 'blog/blog_sidebar.html'

class DetailMaster_questionView(DetailView):
    model = master_question
    fields = '__all__'
    success_url = '/blog/view'

class DeleteMaster_questionView(DeleteView):
    model = master_question
    success_url = '/blog/view'


def blog_single(request):
    return render(request,"blog/blog_single.html")

def sub_question_list(request):
    return render(request, "blog/sub_question_list.html")

def sub_question_detail(request):
    return render(request, "blog/sub_question_detail.html")

def sub_question_confirm_delete(request):
    return render(request, "blog/sub_question_confirm_delete.html")

class NewSub_questionView(CreateView):
    model = sub_question
    fields = '__all__'
    template_name = 'blog/blog_single.html'

class ListSub_questionView(ListView):
    model = sub_question
    context_object_name = 'blog'
    template_name = 'blog/sub_question_list.html'

class UpdateSub_questionView(UpdateView):
    model = sub_question
    fields = '__all__'
    template_name = 'blog/blog_single.html'

class DetailSub_questionView(DetailView):
    model = sub_question
    fields = '__all__'
    success_url = '/blog/view'

class DeleteSub_questionView(DeleteView):
    model = sub_question
    success_url = '/blog/view'

