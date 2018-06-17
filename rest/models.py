from django.db import models
import datetime

# Create your models here.

class Place(models.Model):
    """Model definition for Place."""
    TYPE_OF_PLACE=[('port','SEA PORT'),
                    ('rwst','RAIL STATION')]

    name = models.CharField(max_length=50,blank=True)
    place_type= models.CharField(choices=TYPE_OF_PLACE, max_length=50,blank=True)
    is_border = models.BooleanField()

    class Meta:
        """Meta definition for Place."""

        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __str__(self):
        """Unicode representation of Place."""
        return "%s : %s" % (self.place_type,self.name)

class Person(models.Model):
    """Model definition for Person."""

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

class Factura(models.Model):
    """Model definition for Factura."""

    # TODO: Define fields here
    name = models.CharField(max_length=10,default='XXX-XXXX')
    goods = models.ManyToManyField(Cargo)

    class Meta:
        """Meta definition for Factura."""

        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        """Unicode representation of Factura."""
        return "factura:%s" % self.name



class Shipment(models.Model):
    """Model definition for Shipment."""
    name = models.CharField(max_length=6)
    from_order = models.OneToOneField('Order', on_delete=models.CASCADE,blank=True, null=True)
    consignor = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='consignor',default=1)
    consignee = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='consignee',default=1)
    facturas = models.ManyToManyField(Factura,blank=True, null=True)

    class Meta:
        """Meta definition for Shipment."""

        verbose_name = 'Shipment'
        verbose_name_plural = 'Shipments'

    def __str__(self):
        """Unicode representation of Shipment."""
        return str(self.name)


class Railbill(models.Model):
    """Model definition for Railbill."""

    # TODO: Define fields here
    name = models.CharField(max_length=10,default='00000000')
    shipment = models.OneToOneField(Shipment, on_delete=models.CASCADE)
    class Meta:
        """Meta definition for Railbill."""

        verbose_name = 'Railbill'
        verbose_name_plural = 'Railbills'

    def __str__(self):
        """Unicode representation of Railbill."""
        pass


class Order(models.Model):
    """Model definition for Order."""
    customer = models.CharField(max_length=10,blank=True,default="RLS")
    created = models.DateField(auto_now_add=True)
    will_arrive = models.DateField(auto_now=True)
    is_closed = models.BooleanField(default=False)
    short_description = models.CharField(max_length=100,blank=True,default="name")
    description = models.TextField(blank=True)
    dispatch_place = models.ForeignKey('Place', on_delete=models.CASCADE,related_name='dispatch_place',blank=True)
    destination_place = models.ForeignKey('Place', on_delete=models.CASCADE,related_name='destination_place',blank=True)
   
    shipments = models.ManyToManyField(Shipment,blank=True,related_name='shipments')




    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return "%s : %s" % (self.short_description,self.destination_place)




