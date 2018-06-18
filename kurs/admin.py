# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from kurs import models


admin.site.register(models.CtrlBase)
admin.site.register(models.ElementsBase)
admin.site.register(models.CtrlBom)
admin.site.register(models.Order)
admin.site.register(models.SuppliersCustomersBase)
admin.site.register(models.Invoices)
admin.site.register(models.PurchasesConsumption)
