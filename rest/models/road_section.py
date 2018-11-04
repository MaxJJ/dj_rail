from django.db import models
from .place import Place

class RoadSection(models.Model):

    road = models.CharField(max_length=6,blank=True, null=True)
    in_station = models.ForeignKey('Place', related_name="road_in_station", on_delete=models.SET_NULL, null=True)
    out_station = models.ForeignKey('Place', related_name="road_out_station", on_delete=models.SET_NULL, null=True)
    

    class Meta:
        """Meta definition for RoadSection."""

        verbose_name = 'RoadSection'
        verbose_name_plural = 'RoadSections'

    def __str__(self):
        """Unicode representation of RoadSection."""
        return " %s " % (self.road)
