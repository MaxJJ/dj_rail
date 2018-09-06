from django.db import models

class Unit(models.Model):
    """Model definition for Unit."""

    # TODO: Define fields here
   
    name_full=models.CharField(max_length=30,blank=True)
    name_full_eng=models.CharField(max_length=30,blank=True)

    name_short=models.CharField(max_length=30,blank=True)
    name_short_eng=models.CharField(max_length=30,blank=True)
    code=models.CharField(max_length=5,blank=True)
    class Meta:
        """Meta definition for Unit."""

        verbose_name = 'Unit'
        verbose_name_plural = 'Units'

    def __str__(self):
        """Unicode representation of Unit."""
        return self.name_full + 'Unit'
