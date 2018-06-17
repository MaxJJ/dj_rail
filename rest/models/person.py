from django.db import models
import datetime

class Person(models.Model):
    """Model definition for Person    ."""

    # TODO: Define fields here
    name= models.CharField(max_length=100,blank=True,default='name')
    inn = models.CharField(max_length=15,blank=True,default='ИНН')
    rail_code = models.CharField(max_length=4,blank=True,default='9999')

    class Meta:
        """Meta definition for Person."""
        ordering=('name',)
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        """Unicode representation of Person."""
        return "person:%s" % self.name