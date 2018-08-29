from django.db import models

class Container(models.Model):
    """Model definition for Container."""
    name=models.CharField(max_length=20,blank=True)
    containers_type=models.CharField(max_length=6,blank=True)
    payload=models.CharField(max_length=2,blank=True)
    tare=models.IntegerField(blank=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Container."""

        verbose_name = 'Container'
        verbose_name_plural = 'Containers'

    def __str__(self):
        """Unicode representation of Container."""
        pass
