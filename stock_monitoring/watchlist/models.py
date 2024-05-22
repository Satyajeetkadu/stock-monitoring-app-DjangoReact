from django.contrib.auth.models import User
from django.db import models

class Watchlist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlists')

    def __str__(self):
        return self.name

class StockSymbol(models.Model):
    watchlist = models.ForeignKey(Watchlist, related_name='stocks', on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    last_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.symbol