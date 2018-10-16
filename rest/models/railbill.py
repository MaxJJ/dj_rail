from django.db import models
from ..models.place import Place
from .model_defaults import PLACE


class Railbill(models.Model):
    """Model definition for Railbill."""

    # TODO: Define fields here
    
    number = models.CharField(max_length=10,blank=True)
    dispatch = models.ForeignKey(Place,related_name="rwb_dispatch_station",on_delete=models.SET_DEFAULT,default=PLACE)
    destination = models.ForeignKey(Place,related_name="rwb_destination_station",on_delete=models.SET_DEFAULT,default=PLACE)
    # # stations=models.ManyToManyField('RwbStations')
    # gr_3=models.TextField(blank=True)
    gr_23=models.TextField(blank=True)
    
    class Meta:
        """Meta definition for Railbill."""

        verbose_name = 'Railbill'
        verbose_name_plural = 'Railbills'

    def __str__(self):
        """Unicode representation of Railbill."""
        pass
