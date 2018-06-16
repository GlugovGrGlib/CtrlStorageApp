class ElementsBase(models.Model):
    element_id = models.AutoField(db_column='element_ID', primary_key=True)  # Field name made lowercase.
    element_articul = models.CharField(db_column='element_Articul', max_length=30)  # Field name made lowercase.
    element_name = models.CharField(max_length=45)
    element_description = models.CharField(max_length=200, blank=True, null=True)
    elements_footprint = models.CharField(max_length=45)

    def __str__(self):
        return self.element_articul

    class Meta:
        managed = False
        db_table = 'elements_base'
        verbose_name = 'Element'

    def get_absolute_url(self):
        return reverse('/added/')


class PurchasesConsumption(models.Model):
    record_id = models.AutoField(db_column='record_ID', primary_key=True)  # Field name made lowercase.
    invoice = models.ForeignKey(Invoices, models.PROTECT, db_column='invoice_ID')  # Field name made lowercase.
    element = models.ForeignKey(ElementsBase, models.PROTECT, db_column='element_ID')  # Field name made lowercase.
    elements_quantity = models.IntegerField()
    element_price = models.FloatField()
    p_c = models.ForeignKey(PC, models.PROTECT, db_column='p/c')  # Field renamed to remove unsuitable characters.

    def __str__(self):
        return str(self.invoice)

    class Meta:
        managed = False
        db_table = 'purchases/consumption'
        verbose_name = 'Purchase/Consumption'
        verbose_name_plural = 'Purchases/Consumptions'

    def get_absolute_url(self):
        return reverse('/added/')
