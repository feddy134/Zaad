from django.shortcuts import render
from .models import Contact
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages


# Create your views here.
def test(request):
    return render(request,'frontend/index.html')


class MainView(CreateView):
    template_name = 'frontend/index.html'
    model = Contact
    success_url = reverse_lazy('home')
    form_class = ContactForm

    def form_valid(self, form):
        messages.success(self.request, 'Your data has been saved successfully, Our executive will contact you shortly')
        return super(MainView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Some Error Occured while saving your data please check the form')
        return super(MainView, self).form_invalid(form)
