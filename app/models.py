from django.conf import settings
from django.db import models


class Invoice(models.Model):
    invoice_date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(settings.AUTH_USER_MODEL)



class TaxRate(models.Model):
    DEFAULT_TAXRATE = 'HOOG'
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=4, decimal_places=3)

    def __str__(self):
        return '{} ({}%)'.format(self.name, self.rate.normalize())


class InvoiceItem(models.Model):
    invoice = models.ForeignKey('app.Invoice', related_name='items')

    description = models.CharField(max_length=150, blank=True)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, default=1)

    position = models.PositiveSmallIntegerField()

    tax_rate = models.ForeignKey('app.TaxRate')
