from django.db import models
from .person import Person
from .measure_unit import Unit
from .package import Package
from .model_defaults import *



class Invoice(models.Model):
    """Model definition for Invoice."""

    number=models.CharField(max_length=50,blank=True)
    date=models.DateField(auto_now=True)
    currency=models.CharField(max_length=3,blank=True)
    incoterms_place=models.CharField(max_length=50,blank=True)
    incoterms_code=models.CharField(max_length=3,default='CIP')
    buyer=models.ForeignKey(Person,related_name='inv_buyer',on_delete=models.SET_DEFAULT,default=PERSON)
    seller=models.ForeignKey(Person,related_name='inv_seller',on_delete=models.SET_DEFAULT,default=PERSON)
    consignee=models.ForeignKey(Person,related_name='inv_consignee',on_delete=models.SET_DEFAULT,default=PERSON)
    unit=models.ForeignKey(Unit,related_name='inv_unit',on_delete=models.SET_DEFAULT,default=UNIT)
    units_qty=models.FloatField(default=0.0)
    package=models.ForeignKey(Package,related_name='inv_package',on_delete=models.SET_DEFAULT,default=PACKAGE)
    packages_qty=models.IntegerField(default=0)
    nett_kgs=models.FloatField(default=0.0)
    gross_kgs=models.FloatField(default=0.0)

    class Meta:
        """Meta definition for Invoice."""

        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        """Unicode representation of Invoice."""
        pass
