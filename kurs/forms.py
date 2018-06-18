# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Textarea, ModelChoiceField, DateInput
from kurs import models

P_C_CHOICES = (
    (1, 'Yes'),
    (0, 'No')
)

S_C_CHOICES = (
    (1, 'Поставщик'),
    (0, 'Клиент')
)

class CtrlForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CtrlForm, self).__init__(*args, **kwargs)

    class Meta:
        model = models.CtrlBase
        fields = ['ctrl_name', 'ctrl_description']
        labels = {
            'ctrl_name': u'Название',
            'ctrl_description': u'Описание',
        }
        widgets = {
            'ctrl_description': Textarea(attrs={'cols': 30, 'rows': 3}),
        }


class ElementForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ElementForm, self).__init__(*args, **kwargs)

    class Meta:
        model = models.ElementsBase
        fields = ['element_articul', 'element_name', 'element_description', 'elements_footprint']
        labels = {
            'element_articul': u'Артикул',
            'element_name': u'Название',
            'element_description': u'Описание',
            'elements_footprint': u'Посадочное место'
        }
        widgets = {
            'element_description': Textarea(attrs={'cols': 30, 'rows': 3}),
        }


class CtrlBomForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CtrlBomForm, self).__init__(*args, **kwargs)

    class Meta:
        model = models.CtrlBom
        fields = ['ctrl', 'element', 'elements_quantity']
        labels = {
            'ctrl': u'Контроллер',
            'element': u'Элемент',
            'elements_quantity': u'Количество элементов',
        }
        widgets = {
            'ctrl': InputWithPlusButton()
            'element': InputWithPlusButton()
        }


class InvoiceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = models.Invoices
        fields = ['invoice_number', 'invoice_date', 'supplier_customer']
        labels = {
            'invoice_number': u'Номер накладной',
            'invoice_date': u'Дата накладной',
            'supplier_customer': u'Клиент/поставщик',
        }
        widgets = {
            'invoice_date': DateInput(format='%d/%m/%Y'),
        }



class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

    class Meta:
        model = models.Order
        fields = ['order_number', 'order_date', 'ctrl', 'ctrl_quantity', 'customer']
        labels = {
            'order_number': u'Номер заказа',
            'order_date': u'Дата заказа',
            'ctrl': u'Контроллер',
            'ctrl_quantity': u'Количество контроллеров',
            'customer': u'Клиент'
        }
        widgets = {
            'order_date': DateInput(format='%d/%m/%Y'),
        }

class PurchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PurchForm, self).__init__(*args, **kwargs)
        self.fields['p_c'].initial = 1

    class Meta:
        model = models.PurchasesConsumption
        fields = ['invoice', 'element', 'elements_quantity', 'element_price']
        labels = {
            'invoice': u'Накладная',
            'element': u'Элемент',
            'elements_quantity': u'Описание',
            'element_price': u'Цена элемента',
        }


class ConsumpForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConsumpForm, self).__init__(*args, **kwargs)
        self.fields['p_c'].initial = 0

    class Meta:
        model = models.PurchasesConsumption
        fields = ['invoice', 'element', 'elements_quantity','element_price']
        labels = {
            'invoice': u'Накладная',
            'element': u'Элемент',
            'elements_quantity': u'Описание',
            'element_price': u'Цена элемента',
        }




class SuppForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SuppForm, self).__init__(*args, **kwargs)
        self.fields['supplier_customer_identify'].initial = 1

    class Meta:
        model = models.SuppliersCustomersBase
        fields = ['supplier_customer_name', 'supplier_customer_info']
        labels = {
            'supplier_customer_name': u'Название',
            'supplier_customer_info': u'Описание',
        }


class CustomForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomForm, self).__init__(*args, **kwargs)
        self.fields['supplier_customer_identify'].initial = 0

    class Meta:
        model = models.SuppliersCustomersBase
        fields = ['supplier_customer_name', 'supplier_customer_info']
        labels = {
            'supplier_customer_name': u'Название',
            'supplier_customer_info': u'Описание',
        }
