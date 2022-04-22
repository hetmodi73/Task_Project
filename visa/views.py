from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import canada
# Create your views here.

def canada_form(request):
    return render(request,"visa/canada_form.html")

def canada_list(request):
    return render(request, "visa/canada_list.html")

class NewCanadaView(CreateView):
    model = canada
    fields = '__all__'
    template_name = 'visa/canada_form.html'

class ListCanadaView(ListView):
    model = canada
    context_object_name = 'visa'
    template_name = 'visa/canada_list.html'

class UpdateCanadaView(UpdateView):
    model = canada
    fields = '__all__'
    template_name = 'visa/canada_form.html'

class DetailCanadaView(DetailView):
    model = canada
    fields = '__all__'
    success_url = '/visa/view'

class DeleteCanadaView(DeleteView):
    model = canada
    success_url = '/visa/view'
