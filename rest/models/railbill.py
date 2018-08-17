from django.db import models


class Railbill(models.Model):
    """Model definition for Railbill."""

    # TODO: Define fields here
    
    name = models.CharField(max_length=10,default='00000000')
    gr_23=models.TextField(blank=True)
    
    class Meta:
        """Meta definition for Railbill."""

        verbose_name = 'Railbill'
        verbose_name_plural = 'Railbills'

    def __str__(self):
        """Unicode representation of Railbill."""
        pass
