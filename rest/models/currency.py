from django.db import models


class Currency(models.Model):
    """Model definition for Currency."""

    # TODO: Define fields here

    currency_abbr = models.CharField(default="EUR", max_length=50)
    currency_code = models.CharField(default="978", max_length=50)

    class Meta:
        """Meta definition for Currency."""

        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        """Unicode representation of Currency."""
        return str(self.currency_abbr)
