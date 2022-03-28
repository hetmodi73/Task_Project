from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import feedback
# Create your views here.

def Feedback(request):
    return render(request, "Feedback/feedback.html")

def feedback_list(request):
    return render(request, "Feedback/feedback_list.html")

class NewFeedbackView(CreateView):
    model = feedback
    fields = '__all__'
    template_name = 'Feedback/feedback.html'
    #success_url = 'Feedback/feedback_list.html'

class ListFeedbackView(ListView):
    model = feedback
    context_object_name = 'Feedback'
    template_name = 'Feedback/feedback_list.html'

class UpdateFeedbackView(UpdateView):
    model = feedback
    fields = '__all__'
    template_name = 'Feedback/feedback.html'
    #success_url = '/Feedback/view'

class DetailFeedbackView(DetailView):
    model = feedback
    fields = '__all__'
    success_url = '/Feedback/view'

class DeleteFeedbackView(DeleteView):
    model = feedback
    success_url = '/Feedback/view'
