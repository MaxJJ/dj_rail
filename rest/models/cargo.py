from django.db import models
import datetime


class Cargo(models.Model):
    """Model definition for Cargo."""

    # TODO: Define fields here
    description = models.TextField(blank=True)
    tnved_code = models.CharField(max_length=50,blank=True)

    class Meta:
        """Meta definition for Cargo."""

        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        """Unicode representation of Cargo."""
        pass