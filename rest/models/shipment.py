from django.db import models
import datetime
from .person import Person

from .currency import Currency
from .railbill import Railbill
from .cargo import Cargo
from .factura import Factura
from .invoice import Invoice
# from .order import Order
from .model_defaults import *


class Shipment(models.Model):
    """Model definition for Shipment."""
    name = models.CharField(max_length=6)
    description=models.CharField(max_length=50,default='shipment')
    order = models.ForeignKey('Order', on_delete=models.CASCADE,default=1,blank = True,null=True)
    contract=models.CharField(max_length=50,default="ПО ИНВОЙСУ")
    cargo_is_general=models.NullBooleanField()
    container = models.ForeignKey('Container',related_name="container",on_delete=models.SET_NULL,null=True)
    buyer = models.ForeignKey(Person,related_name="buyer",on_delete=models.SET_DEFAULT,default=PERSON)
    seller = models.ForeignKey(Person,related_name="seller",on_delete=models.SET_DEFAULT,default=PERSON)
    # cargo = models.ForeignKey('Cargo',related_name="cargo", on_delete=models.DO_NOTHING,blank = True,null=True)
    facturas = models.ManyToManyField(Factura,related_name="shipments_facturas")
    invoices = models.ManyToManyField(Invoice,related_name="shipment_invoices")
    rw_bill = models.OneToOneField(Railbill,on_delete=models.SET_NULL,null=True)

    class Meta:
        """Meta definition for Shipment."""

        verbose_name = 'Shipment'
        verbose_name_plural = 'Shipments'

    def __str__(self):
        """Unicode representation of Shipment."""
        return str(self.name)