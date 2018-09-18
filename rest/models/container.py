from django.db import models

class Container(models.Model):
    """Model definition for Container."""
    name=models.CharField(max_length=20,blank=True,null=True)
    containers_type=models.CharField(max_length=6,blank=True,null=True)
    payload=models.IntegerField(blank=True,null=True)
    tare=models.IntegerField(blank=True,null=True)
    owner=models.CharField(max_length=30,blank=True,null=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Container."""

        verbose_name = 'Container'
        verbose_name_plural = 'Containers'

    def __str__(self):
        """Unicode representation of Container."""
        pass
