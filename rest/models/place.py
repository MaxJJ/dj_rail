from django.db import models

class Place(models.Model):
    """Model definition for Place."""
    TYPE_OF_PLACE=[('port','SEA PORT'),
                    ('rwst','RAIL STATION')]

    name = models.CharField(max_length=50,blank=True)
    place_type= models.CharField(choices=TYPE_OF_PLACE, max_length=50,blank=True)
    is_border = models.BooleanField()

    class Meta:
        """Meta definition for Place."""

        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __str__(self):
        """Unicode representation of Place."""
        return "%s : %s" % (self.place_type,self.name)