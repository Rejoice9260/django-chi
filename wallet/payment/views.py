from django.shortcuts import render
from .models import TransactionType, Transaction, PaymentAccount
from .forms import TransactionTypeForm
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class TransactionTypeListView(ListView, LoginRequiredMixin):
    model = TransactionType
    template_name = 'payment/transaction_type_list.html'
    context_object_name = 'transactiontypes'

class TransactionTypeCreateView(CreateView, LoginRequiredMixin):
    model = TransactionType
    template_name = 'payment/transaction_type_create.html'
    form_class = TransactionTypeForm
    success_url = reverse_lazy('transaction_type_list')    

class TransactionTypeDetailView(DetailView, LoginRequiredMixin):
    model = TransactionType
    template_name = 'payment/transaction_type_detail.html'
    context_object_name = 'transactiontype'    

class TransactionTypeUpdateView(UpdateView, LoginRequiredMixin):
    model = TransactionType
    form_class = TransactionTypeForm
    template_name = 'payment/transaction_type_update.html'
    success_url = reverse_lazy('transaction_type_list')     

class TransactionTypeDeleteView(DeleteView, LoginRequiredMixin):
    model = TransactionType
    template_name = 'payment/transaction_type_confirm_delete.html'   
    success_url = reverse_lazy('transaction_type_list') 