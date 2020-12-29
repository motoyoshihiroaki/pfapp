from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
from django.views import generic
# from django.views.generic import base

from .forms import InquiryForm

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('index:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました')
        return super().form_valid(form)
