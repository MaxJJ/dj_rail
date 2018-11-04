from django.db import models
from ..models.place import Place
from ..models.shipment import Shipment
from .model_defaults import PLACE
from ..models.road_section import RoadSection


class Railbill(models.Model):
    """Model definition for Railbill."""

    # TODO: Define fields here
    shipment=models.OneToOneField(Shipment,on_delete=models.SET_NULL,null=True)
    number = models.CharField(max_length=10,blank=True)
    dispatch = models.ForeignKey(Place,related_name="rwb_dispatch_station",on_delete=models.SET_NULL,null=True)
    destination = models.ForeignKey(Place,related_name="rwb_destination_station",on_delete=models.SET_NULL,null=True)
    road_sections=models.ManyToManyField(RoadSection,related_name="rwb_road_sections")

    gr_23=models.TextField(blank=True)
    
    class Meta:
        """Meta definition for Railbill."""

        verbose_name = 'Railbill'
        verbose_name_plural = 'Railbills'

    def __str__(self):
        """Unicode representation of Railbill."""
        pass
