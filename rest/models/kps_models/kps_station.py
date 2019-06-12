from django.db import models


class KpsStation(models.Model):
    """Model definition for Kps Station."""
    kpsId = models.IntegerField(blank=True, null=True)
    Code = models.CharField(max_length=100, blank=True, null=True)
    RouteId = models.IntegerField(blank=True, null=True)
    StationDistrictId = models.IntegerField(blank=True, null=True)
    StationDistrictName = models.CharField(
        max_length=100, blank=True, null=True)
    Name = models.CharField(max_length=100, blank=True, null=True)
    Open = models.CharField(max_length=100, blank=True, null=True)
    ExpImpCode = models.CharField(max_length=100, blank=True, null=True)
    CountryCode = models.CharField(max_length=100, blank=True, null=True)
    CountryName = models.CharField(max_length=100, blank=True, null=True)
    RailwayCodeD2 = models.CharField(max_length=100, blank=True, null=True)
    RailwayCode = models.CharField(max_length=100, blank=True, null=True)
    RailwayName = models.CharField(max_length=100, blank=True, null=True)
    AdministrationShortname = models.CharField(
        max_length=100, blank=True, null=True)
    Paragraph = models.CharField(max_length=100, blank=True, null=True)
    IsVnk = models.NullBooleanField()

    class Meta:
        """Meta definition for Place."""

        verbose_name = 'KpsStation'
        verbose_name_plural = 'KpsStations'

    def __str__(self):
        """Unicode representation of KpsStation."""
        return "Station KPS  %s : %s" % (self.Name, self.Code)
