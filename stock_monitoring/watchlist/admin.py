from django.contrib import admin
from .models import Watchlist, StockSymbol

admin.site.register(Watchlist)
admin.site.register(StockSymbol)