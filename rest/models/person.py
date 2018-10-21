from django.db import models
import datetime

class Person(models.Model):
    """Model definition for Person    ."""

    # TODO: Define fields here
    name= models.CharField(max_length=100,blank=True,default='name')
    inn = models.CharField(max_length=15,blank=True,default='ИНН')
    okpo = models.CharField(max_length=15,blank=True)
    phone = models.CharField(max_length=15,blank=True)
    postal_code = models.CharField(max_length=15,blank=True)
    region = models.CharField(max_length=50,blank=True)
    city = models.CharField(max_length=50,blank=True)
    street_house = models.CharField(max_length=100,blank=True)
    rail_code = models.CharField(max_length=4,blank=True,default='9999')
    country=models.ForeignKey('Country',related_name='country',on_delete=models.CASCADE,blank = True,null=True)


    class Meta:
        """Meta definition for Person."""
        ordering=('name',)
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        """Unicode representation of Person."""
        return 'myrepr'