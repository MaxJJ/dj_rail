from django.db import models
import datetime

from .shipment import Shipment

class Order(models.Model):
    """Model definition for Order."""
    customer = models.CharField(max_length=10,blank=True,default="RLS")
    created = models.DateField(auto_now_add=True)
    will_arrive = models.DateField(auto_now=True)
    is_closed = models.BooleanField(default=False)
    short_description = models.CharField(max_length=100,blank=True,default="name")
    description = models.TextField(blank=True)
    dispatch_place = models.ForeignKey('Place', on_delete=models.CASCADE,related_name='dispatch_place',blank=True)
    destination_place = models.ForeignKey('Place', on_delete=models.CASCADE,related_name='destination_place',blank=True)
   
    shipments = models.ManyToManyField(Shipment,blank=True,related_name='shipments')




    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return "%s : %s" % (self.short_description,self.destination_place)