from django.db import models
import datetime
from .package import Package




from .measure_unit import Unit


class Cargo(models.Model):
    """Model definition for Cargo."""

    is_container = models.NullBooleanField()
    container_tare = models.FloatField(null=True)
    description = models.TextField(blank=True)
    tnved_code = models.CharField(max_length=50, blank=True)
    tved_description = models.TextField(blank=True)
    gng_code = models.CharField(max_length=50, blank=True)
    gng_description=models.TextField(blank=True)
    etsng_code=models.CharField(max_length=50, blank=True)
    package=models.ForeignKey(Package, on_delete=models.CASCADE,default=1)
    package_quantity = models.IntegerField(null=True)
    unit=models.ForeignKey(Unit, on_delete=models.CASCADE,default=1)
    unit_quantity=models.FloatField(null=True)
    nett_weight=models.FloatField(null=True)
    gross_weight=models.FloatField(null=True)
    unit_price=models.FloatField(null=True)
    total=models.FloatField(null=True)
    factura = models.ForeignKey('Factura',related_name="from_factura",on_delete=models.SET_NULL,null=True)
    is_indexed=models.NullBooleanField()


    class Meta:
        """Meta definition for Cargo."""

        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        """Unicode representation of Cargo."""
        return self.description
