from django.db import models

class Tnved(models.Model):
    """Model definition for Tnved."""

    # TODO: Define fields here

    code=models.CharField(max_length=10,blank=True,null=True)
    description = models.TextField(blank=True,null=True)

    class Meta:
        """Meta definition for Tnved."""

        verbose_name = 'Tnved'
        verbose_name_plural = 'Tnveds'

    def __str__(self):
        """Unicode representation of Tnved."""
        pass
