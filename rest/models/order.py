from django.db import models
import datetime
from .cargo import Cargo
from .shipment import Shipment
from .person import Person
from .place import Place
from .comments import Comment

class InboundDoc(models.Model):
    """Model definition for InboundDoc."""

    doc_type=models.CharField(max_length=20,default="Bill Of Lading")
    number=models.CharField(max_length=20,blank=True)
    places=models.IntegerField(default=0)
    gross=models.FloatField(default=0.0)

    class Meta:
        """Meta definition for InboundDoc."""

        verbose_name = 'InboundDoc'
        verbose_name_plural = 'InboundDocs'

    def __str__(self):
        """Unicode representation of InboundDoc."""
        return self.number


class Order(models.Model):
    """Model definition for Order."""
    customer = models.CharField(max_length=10,blank=True,default="RLS")
    
    created = models.DateField(auto_now_add=True)
    will_arrive = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    short_description = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    consignor = models.ForeignKey('Person', on_delete=models.CASCADE,related_name='consignor',default=1)
    consignee = models.ForeignKey('Person', on_delete=models.CASCADE,related_name='consignee',default=1)
    inbound_bill = models.CharField(blank=True,max_length=30)
    inbound_docs = models.ManyToManyField(InboundDoc,blank=True)
    transit_or_export = models.CharField(blank=True,max_length=10)
    inbound_cargo = models.ManyToManyField(Cargo,blank=True)
    total_inbound_places = models.IntegerField(null=True)
    total_inbound_gross = models.FloatField(null=True)


    dispatch_place = models.ForeignKey('Place', on_delete=models.CASCADE,related_name='dispatch_place',default=1)
    destination_place = models.ForeignKey('Place', on_delete=models.CASCADE,related_name='destination_place',default=1)
   
    shipments = models.ManyToManyField(Shipment,related_name='shipments',blank = True,null=True)
    comments = models.ManyToManyField(Comment,related_name='comments',blank = True,null=True)




    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return "%s : %s" % (self.short_description,self.destination_place)



