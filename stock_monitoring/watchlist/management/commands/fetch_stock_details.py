# import requests
# from django.core.management.base import BaseCommand
# from django.utils import timezone
# from watchlist.models import StockSymbol

# class Command(BaseCommand):
#     help = 'Fetch stock details from Alpha Vantage API'

#     def handle(self, *args, **kwargs):
#         api_key = 'N7GGKDLXF6M37WP0'
#         base_url = 'https://www.alphavantage.co/query'

#         for stock in StockSymbol.objects.all():
#             params = {
#                 'function': 'TIME_SERIES_INTRADAY',
#                 'symbol': stock.symbol,
#                 'interval': '1min',
#                 'apikey': api_key
#             }
#             response = requests.get(base_url, params=params)
#             data = response.json()

#             try:
#                 time_series = data['Time Series (1min)']
#                 latest_time = sorted(time_series.keys())[0]
#                 latest_data = time_series[latest_time]

#                 stock.last_price = latest_data['4. close']
#                 stock.last_updated = timezone.now()
#                 stock.save()

#                 self.stdout.write(self.style.SUCCESS(f'Successfully updated {stock.symbol}'))
#             except KeyError:
#                 self.stdout.write(self.style.ERROR(f'Failed to fetch data for {stock.symbol}'))
