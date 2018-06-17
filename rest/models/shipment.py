from django.db import models
import datetime
from .person import Person
from .factura import Factura


class Shipment(models.Model):
    """Model definition for Shipment."""
    name = models.CharField(max_length=6)
    from_order = models.OneToOneField('Order', on_delete=models.CASCADE,blank=True, null=True)
    consignor = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='consignor',default=1)
    consignee = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='consignee',default=1)
    facturas = models.ManyToManyField(Factura,blank=True, null=True)

    class Meta:
        """Meta definition for Shipment."""

        verbose_name = 'Shipment'
        verbose_name_plural = 'Shipments'

    def __str__(self):
        """Unicode representation of Shipment."""
        return str(self.name)