from django.db import models
from django.core.urlresolvers import reverse
from django.forms import ModelForm

# Create your models here.


class CtrlBase(models.Model):
    ctrl_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    ctrl_name = models.CharField(max_length=45)
    ctrl_description = models.CharField(max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('/added/')

    def __str__(self):
        return self.ctrl_name

    class Meta:
        managed = True
        verbose_name = 'Controller'


class ElementsBase(models.Model):
    element_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    element_articul = models.CharField(max_length=30)  # Field name made lowercase.
    element_name = models.CharField(max_length=45)
    element_description = models.CharField(max_length=200, blank=True, null=True)
    elements_footprint = models.CharField(max_length=45)

    def __str__(self):
        return self.element_articul

    class Meta:
        managed = True
        verbose_name = 'Element'

    def get_absolute_url(self):
        return reverse('/added/')


class CtrlBom(models.Model):
    ctrl_bom_id = models.AutoField(primary_key=True)
    ctrl = models.ForeignKey(CtrlBase, models.PROTECT)  # Field name made lowercase.
    element = models.ForeignKey(ElementsBase, models.PROTECT)  # Field name made lowercase.
    elements_quantity = models.IntegerField()

    def __str__(self):
        return self.ctrl.ctrl_name

    class Meta:
        managed = True
        verbose_name = 'BOM'

    def get_absolute_url(self):
        return reverse('/added/')


class SuppliersCustomersBase(models.Model):
    supplier_customer_id = models.AutoField(primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    supplier_customer_identify = models.BooleanField()  # Field name made lowercase. Field renamed to remove unsuitable characters.
    supplier_customer_name = models.CharField(max_length=100)  # Field renamed to remove unsuitable characters.
    supplier_customer_info = models.CharField(max_length=200, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    def __str__(self):
        return self.supplier_customer_name

    class Meta:
        managed = True
        verbose_name_plural = 'Suppliers/Customers'

    def get_absolute_url(self):
        return reverse('/added/')


class Invoices(models.Model):
    invoice_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    invoice_number = models.CharField(unique=True, max_length=45)
    invoice_date = models.DateTimeField()
    supplier_customer = models.ForeignKey(SuppliersCustomersBase, models.PROTECT)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return self.invoice_number

    class Meta:
        managed = True
        verbose_name = 'Invoice'

    def get_absolute_url(self):
        return reverse('/added/')


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    order_number = models.CharField(max_length=45)
    order_date = models.DateTimeField()
    ctrl = models.ForeignKey(CtrlBase, models.PROTECT)  # Field name made lowercase.
    ctrl_quantity = models.IntegerField()
    customer = models.ForeignKey(SuppliersCustomersBase, models.PROTECT)  # Field name made lowercase.

    def __str__(self):
        return self.order_number

    class Meta:
        managed = True

    def get_absolute_url(self):
        return reverse('/added/')


class PurchasesConsumption(models.Model):
    record_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    invoice = models.ForeignKey(Invoices, models.PROTECT)  # Field name made lowercase.
    element = models.ForeignKey(ElementsBase, models.PROTECT)  # Field name made lowercase.
    elements_quantity = models.IntegerField()
    element_price = models.FloatField()
    p_c = models.BooleanField()  # Field renamed to remove unsuitable characters.

    def __str__(self):
        return str(self.invoice)

    class Meta:
        managed = True
        verbose_name = 'Purchase/Consumption'
        verbose_name_plural = 'Purchases/Consumptions'

    def get_absolute_url(self):
        return reverse('/added/')
