from django.db import models
import datetime
from .person import Person
from .factura import Factura
from .currency import Currency
from .railbill import Railbill
from .cargo import Cargo
# from .order import Order


class Shipment(models.Model):
    """Model definition for Shipment."""
    name = models.CharField(max_length=6)
    belongs_to_order = models.ForeignKey('Order',on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey(Person,related_name="buyer", on_delete=models.CASCADE,default=1)
    seller = models.ForeignKey(Person,related_name="seller", on_delete=models.CASCADE,default=1)
    incoterms_abbr=models.CharField(max_length=3,default="CIP")
    incoterms_place=models.CharField(max_length=50,default="RIGA")
    currency=models.ForeignKey(Currency, on_delete=models.CASCADE,default=1)
    
    railbill = models.ForeignKey(Railbill, on_delete=models.CASCADE,default=1)
    facturas = models.ManyToManyField(Factura,default=1)
    outbound_cargo = models.ManyToManyField(Cargo)

    class Meta:
        """Meta definition for Shipment."""

        verbose_name = 'Shipment'
        verbose_name_plural = 'Shipments'

    def __str__(self):
        """Unicode representation of Shipment."""
        return str(self.name)