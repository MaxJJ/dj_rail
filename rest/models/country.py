from django.db import models

class Country(models.Model):
    """Model definition for Country."""

    name_rus= models.CharField(max_length=100,blank=True)
    name_eng= models.CharField(max_length=100,blank=True)
    name_lat= models.CharField(max_length=100,blank=True)
    code= models.CharField(max_length=10,blank=True)

    class Meta:
        """Meta definition for Country."""

        verbose_name = 'Country'
        verbose_name_plural = 'Countrys'

    def __str__(self):
        """Unicode representation of Country."""
        pass
