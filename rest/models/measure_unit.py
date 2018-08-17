from django.db import models

class Unit(models.Model):
    """Model definition for Unit."""

    # TODO: Define fields here
    unit_name_full=models.CharField(max_length=30,blank=True)
    unit_name_short=models.CharField(max_length=30,blank=True)
    unit_code=models.CharField(max_length=5,blank=True)
    class Meta:
        """Meta definition for Unit."""

        verbose_name = 'Unit'
        verbose_name_plural = 'Units'

    def __str__(self):
        """Unicode representation of Unit."""
        pass
