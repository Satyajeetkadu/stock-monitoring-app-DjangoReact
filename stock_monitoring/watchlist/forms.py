from django import forms
from .models import Watchlist, StockSymbol

class WatchlistForm(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = ['name']

class StockSymbolForm(forms.ModelForm):
    class Meta:
        model = StockSymbol
        fields = ['symbol']