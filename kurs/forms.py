from django.forms import ModelForm, Textarea, ModelChoiceField, forms
from . import models


class CtrlForm(ModelForm):
    class Meta:
        model = models.CtrlBase
        fields = ['ctrl_name', 'ctrl_description']
        widgets = {
            'ctrl_description': Textarea(attrs={'cols': 30, 'rows': 3}),
        }


class ElementForm(ModelForm):
    class Meta:
        model = models.ElementsBase
        fields = ['element_articul', 'element_name', 'element_description', 'elements_footprint']
        widgets = {
            'element_description': Textarea(attrs={'cols': 30, 'rows': 3}),
        }


class CtrlBomForm(ModelForm):
    class Meta:
        model = models.CtrlBom
        fields = ['ctrl', 'element', 'elements_quantity']


class InvoiceForm(ModelForm):
    class Meta:
        model = models.Invoices
        fields = ['invoice_number', 'invoice_date', 'supplier_customer']


class OrderForm(ModelForm):
    class Meta:
        model = models.Order
        fields = ['order_number', 'order_date', 'ctrl', 'ctrl_quantity', 'customer']


class PurchForm(ModelForm):
    class Meta:
        model = models.PurchasesConsumption
        fields = ['invoice', 'element', 'elements_quantity', 'element_price', 'p_c']
        default_data = {
        'p_c': 1
        }


class ConsumpForm(ModelForm):
    class Meta:
        model = models.PurchasesConsumption
        fields = ['invoice', 'element', 'elements_quantity','element_price', 'p_c']
        default_data = {
        'p_c': 0
        }


class SuppForm(ModelForm):
    class Meta:
        model = models.SuppliersCustomersBase
        fields = ['supplier_customer_identify', 'supplier_customer_name', 'supplier_customer_info']
        default_data = {
        'p_c': 1
        }


class CustomForm(ModelForm):
    class Meta:
        model = models.SuppliersCustomersBase
        fields = ['supplier_customer_identify', 'supplier_customer_name', 'supplier_customer_info']
        default_data = {
        'p_c': 0
        }
