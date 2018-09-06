from django.db import models
import datetime
from .cargo import Cargo

class Factura(models.Model):
    """Model definition for Factura."""

    # TODO: Define fields here
    name = models.CharField(max_length=10,default='XXX-XXXX')
    goods = models.ManyToManyField('Cargo')

    class Meta:
        """Meta definition for Factura."""

        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        """Unicode representation of Factura."""
        return "factura:%s" % self.name