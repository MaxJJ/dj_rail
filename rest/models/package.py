from django.db import models

class Package(models.Model):
    """Model definition for Package."""

    # TODO: Define fields here

    package_name_rus=models.CharField(max_length=30,blank=True)
    package_name_eng=models.CharField(max_length=30,blank=True)
    package_code=models.CharField(max_length=3,blank=True)

    class Meta:
        """Meta definition for Package."""

        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

    def __str__(self):
        """Unicode representation of Package."""
        pass
