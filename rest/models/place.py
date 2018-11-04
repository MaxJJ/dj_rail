from django.db import models

class Place(models.Model):
    """Model definition for Place."""


    place_name = models.CharField(max_length=50,blank=True)
    place_code=models.CharField(max_length=6,default="000000")
    is_out = models.NullBooleanField(default=False)
    road_name=models.CharField(max_length=100,blank=True)
    road_name_abbr=models.CharField(max_length=4,blank=True)
    road_code=models.CharField(max_length=4,blank=True)
    road_operator_name=models.CharField(max_length=20,blank=True)



    class Meta:
        """Meta definition for Place."""

        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __str__(self):
        """Unicode representation of Place."""
        return " %s : %s" % (self.place_code,self.place_name)