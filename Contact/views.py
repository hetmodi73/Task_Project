from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import contact

# Create your views here.

def Contact(request):
    return render(request,"Contact/contact.html")

def contact_list(request):
    return render(request, "Contact/contact_list.html")

class NewContactView(CreateView):
    model = contact
    fields = '__all__'
    template_name = 'Contact/contact.html'
   # success_url = 'Contact/contact_list.html'

class ListContactView(ListView):
    model = contact
    context_object_name = 'Contact'
    template_name = 'Contact/contact_list.html'

class UpdateContactView(UpdateView):
    model = contact
    fields = '__all__'
    template_name = 'Contact/contact.html'

class DetailContactView(DetailView):
    model = contact
    fields = '__all__'
    success_url = '/Contact/view'

class DeleteContactView(DeleteView):
    model = contact
    success_url = '/Contact/view'
