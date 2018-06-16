from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

from kurs import models
from kurs import forms

@login_required
def show_ctrls(request):
    ctrls_view = models.CtrlBase.objects.all()
    current_user = request.user
    return render(request, 'show_ctrls.html', locals())

@login_required
def show_elements(request):
    elements_view = models.ElementsBase.objects.all()
    current_user = request.user
    return render(request, 'show_elements.html', locals())

@login_required
def show_bom(request):
    bom_view = models.CtrlBom.objects.all()
    ctrls_view = models.CtrlBase.objects.all()
    elements_view = models.ElementsBase.objects.all()
    current_user = request.user
    return render_to_response('show_boms.html', locals())

@login_required
def show_orders(request):
    orders_view = models.Order.objects.all()
    ctrls_view = models.CtrlBase.objects.all()
    customer_view = models.SuppliersCustomersBase.objects.all()
    current_user = request.user
    return render_to_response('show_orders.html', locals())

@login_required
def show_suppliers(request):
    suppliers_view = models.SuppliersCustomersBase.objects.filter(supplier_customer_identify=1)
    current_user = request.user
    return render_to_response('show_suppliers.html', locals())

@login_required
def show_clients(request):
    clients_view = models.SuppliersCustomersBase.objects.filter(supplier_customer_identify=0)
    current_user = request.user
    return render_to_response('show_clients.html', locals())

@login_required
def show_purchases(request):
    purchases_view = models.PurchasesConsumption.objects.filter(p_c=1)
    elements_view = models.ElementsBase.objects.all()
    invoices_view = models.Invoices.objects.all()
    suppliers_view = models.SuppliersCustomersBase.objects.all()
    current_user = request.user
    return render_to_response("show_purchases.html", locals())

@login_required
def show_consumptions(request):
    consumptions_view = models.PurchasesConsumption.objects.filter(p_c=0)
    elements_view = models.ElementsBase.objects.all()
    invoices_view = models.Invoices.objects.all()
    suppliers_view = models.SuppliersCustomersBase.objects.all()
    current_user = request.user
    return render_to_response("show_consumptions.html", locals())

@login_required
def show_stock(request):
    elements_view = models.ElementsBase.objects.all()
    current_user = request.user
    return render_to_response("show_stock.html", locals())

class NewCtrl(CreateView):
    model = models.CtrlBase
    form_class = forms.CtrlForm
    success_url = '/added/'

class NewElement(CreateView):
    model = models.ElementsBase
    form_class = forms.ElementForm
    success_url = '/added/'

class NewBom(CreateView):
    model = models.CtrlBom
    form_class = forms.CtrlBomForm
    success_url = '/added/'

class NewOrder(CreateView):
    model = models.Order
    form_class = forms.OrderForm
    success_url = '/added/'

class NewConsumption(CreateView):
    model = models.PurchasesConsumption
    form_class = forms.ConsumpForm
    success_url = '/added/'

class NewPurchase(CreateView):
    model = models.PurchasesConsumption
    form_class = forms.PurchForm
    success_url = '/added/'

class NewSupplier(CreateView):
    model = models.SuppliersCustomersBase
    form_class = forms.SuppForm
    success_url = '/added/'

class NewCustomer(CreateView):
    model = models.SuppliersCustomersBase
    form_class = forms.CustomForm
    success_url = '/added/'
