# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView, ListView

from service.forms import CreateMailingForm, UpdateMailingForm, CreateClientForm
from service.models import Mailing, Client


# Create your views here.
class DashboardView(TemplateView):
    template_name = 'service/includes/inc_main_title.html'


class CreateMailingView(CreateView):
    model = Mailing
    form_class = CreateMailingForm
    success_url = reverse_lazy('service:list_mailing')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = Client.objects.all()
        context['clients'] = clients
        return context


class UpdateMailingView(UpdateView):
    model = Mailing
    form_class = UpdateMailingForm
    success_url = reverse_lazy('service:list_mailing')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = Client.objects.all()
        context['clients'] = clients
        return context


class ListMailingView(ListView):
    model = Mailing
    template_name = 'service/mailing_list.html'


class DetailMailingView(DetailView):
    model = Mailing
    template_name = 'service/mailing_detail.html'


class DeleteMailingView(DeleteView):
    model = Mailing
    template_name = 'service/mailing_confirm_delete.html'
    success_url = reverse_lazy('service:list_mailing')


class CreateClientView(CreateView):
    model = Client
    form_class = CreateClientForm
    success_url = reverse_lazy('service:clients_list')


class ListClientView(ListView):
    model = Client
    template_name = 'service/clients_list.html'


class DeleteClientView(DeleteView):
    model = Client
    template_name = 'service/client_confirm_delete.html'
    success_url = reverse_lazy('service:clients_list')
