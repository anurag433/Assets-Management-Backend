from django.db import models
from django.conf import settings

class Asset(models.Model):

    ASSET_TYPE = (
        ('CRYPTO', 'Crypto'),
        ('STOCK', 'Stock'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=10, choices=ASSET_TYPE)
    quantity = models.FloatField()
    purchase_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.asset_name
