from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import canada_pr

# Create your views here.

def canada_pr_form(request):
    return render(request,"pr/canada_pr_form.html")

def canada_pr_list(request):
    return render(request, "pr/canada_pr_list.html")

class NewCanada_prView(CreateView):
    model = canada_pr
    fields = '__all__'
    template_name = 'pr/canada_pr_form.html'

class ListCanada_prView(ListView):
    model = canada_pr
    context_object_name = 'visa'
    template_name = 'pr/canada_pr_list.html'

class UpdateCanada_prView(UpdateView):
    model = canada_pr
    fields = '__all__'
    template_name = 'pr/canada_pr_form.html'

class DetailCanada_prView(DetailView):
    model = canada_pr
    fields = '__all__'
    success_url = '/pr/view'

class DeleteCanada_prView(DeleteView):
    model = canada_pr
    success_url = '/pr/view'
