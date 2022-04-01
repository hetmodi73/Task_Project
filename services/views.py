from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import service,service_details
# Create your views here.

def services(request):
    return render(request, "services/service.html")

def service_list(request):
    return render(request, "services/service_list.html")

def service_detail(request):
    return render(request, "services/service_detail.html")

def service_confirm_delete(request):
    return render(request, "services/service_confirm_delete.html")

class NewServiceView(CreateView):
    model = service
    fields = '__all__'
    template_name = 'services/service.html'

class ListServiceView(ListView):
    model = service
    context_object_name = 'services'
    template_name = 'services/service_list.html'

class UpdateServiceView(UpdateView):
    model = service
    fields = '__all__'
    template_name = 'services/service.html'

class DetailServiceView(DetailView):
    model = service
    fields = '__all__'
    success_url = '/services/view'

class DeleteServiceView(DeleteView):
    model = service
    success_url = '/services/view'

def service_details_list(request):
    return render(request, "services/service_details_list.html")

def service_details_detail(request):
    return render(request, "services/service_details_detail.html")

def service_details_confirm_delete(request):
    return render(request, "services/service_details_confirm_delete.html")

class NewService_detailsView(CreateView):
    model = service_details
    fields = '__all__'
    template_name = 'services/service.html'

class ListService_detailsView(ListView):
    model = service_details
    context_object_name = 'services'
    template_name = 'services/service_details_list.html'

class UpdateService_detailsView(UpdateView):
    model = service_details
    fields = '__all__'
    template_name = 'services/service.html'

class DetailService_detailsView(DetailView):
    model = service_details
    fields = '__all__'
    success_url = '/services/view'

class DeleteService_detailsView(DeleteView):
    model = service_details
    success_url = '/services/view'
