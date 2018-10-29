from django.db import models
import datetime
from .cargo import Cargo
from .person import Person
from .shipment import Shipment
from .model_defaults import *

class Factura(models.Model):
    """Model definition for Factura."""

    # TODO: Define fields here
    shipment=models.ForeignKey(Shipment,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=10,blank=True)
    doc_name = models.CharField(max_length=50,default='СЧЕТ-ФАКТУРА')
    date=models.DateField(auto_now=True)
    buyer=models.ForeignKey(Person,related_name='factura_buyer',on_delete=models.SET_DEFAULT,default=PERSON)
    seller=models.ForeignKey(Person,related_name='factura_seller',on_delete=models.SET_DEFAULT,default=PERSON)
    consignee=models.ForeignKey(Person,related_name='factura_consignee',on_delete=models.SET_DEFAULT,default=PERSON)
    consignor=models.ForeignKey(Person,related_name='factura_consignor',on_delete=models.SET_DEFAULT,default=PERSON)
    delivery_terms_str_code=models.CharField(max_length=3,default='CIP')
    delivery_terms_place=models.CharField(max_length=30,blank=True,null=True)
    contract_name=models.CharField(max_length=50,blank=True,null=True)
    contract_number=models.CharField(max_length=50,blank=True,null=True)
    cargo=models.ManyToManyField(Cargo,related_name='facturas_cargo')
    places=models.IntegerField(blank=True,null=True)
    pcs=models.FloatField(blank=True,null=True)
    nett=models.FloatField(blank=True,null=True)
    gross=models.FloatField(blank=True,null=True)
    price=models.FloatField(blank=True,null=True)
    total_amount=models.FloatField(blank=True,null=True)
    currency=models.CharField(max_length=4,blank=True,null=True)
    footer=models.TextField(blank=True,null=True)
    footer_first_str=models.TextField(blank=True,null=True)

    extra_total_description=models.CharField(max_length=100,blank=True,null=True)
    extra_total=models.FloatField(blank=True,null=True)
    grand_total=models.FloatField(blank=True,null=True)
    currency=models.CharField(max_length=4,blank=True,null=True)



    class Meta:
        """Meta definition for Factura."""

        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        """Unicode representation of Factura."""
        return "factura:%s" % self.name 