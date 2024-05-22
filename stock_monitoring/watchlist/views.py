from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Watchlist, StockSymbol
from .serializers import UserSerializer, RegisterSerializer, WatchlistSerializer, StockSymbolSerializer
import requests

ALPHA_VANTAGE_API_KEY = 'N7GGKDLXF6M37WP0'  # Replace with your actual API key

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class WatchlistView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        watchlists = Watchlist.objects.filter(user=request.user)
        serializer = WatchlistSerializer(watchlists, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        watchlist = Watchlist.objects.create(name=data['name'], user=request.user)
        serializer = WatchlistSerializer(watchlist)
        return Response(serializer.data)

    def delete(self, request, watchlist_id):
        try:
            watchlist = Watchlist.objects.get(id=watchlist_id, user=request.user)
            watchlist.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Watchlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class StockSymbolView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, watchlist_id):
        stocks = StockSymbol.objects.filter(watchlist__id=watchlist_id, watchlist__user=request.user)
        serializer = StockSymbolSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self, request, watchlist_id):
        data = request.data
        symbol = data['symbol']
        
        # Fetch stock details from Alpha Vantage
        base_url = 'https://www.alphavantage.co/query'
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': '1min',
            'apikey': ALPHA_VANTAGE_API_KEY
        }
        response = requests.get(base_url, params=params)
        stock_data = response.json()
        
        if 'Time Series (1min)' in stock_data:
            latest_time = list(stock_data['Time Series (1min)'].keys())[0]
            latest_data = stock_data['Time Series (1min)'][latest_time]
            last_price = latest_data['4. close']
            last_updated = latest_time
        else:
            last_price = None
            last_updated = None
        
        watchlist = Watchlist.objects.get(id=watchlist_id, user=request.user)
        stock = StockSymbol.objects.create(watchlist=watchlist, symbol=symbol, last_price=last_price, last_updated=last_updated)
        serializer = StockSymbolSerializer(stock)
        return Response(serializer.data)

    def delete(self, request, watchlist_id, stock_id):
        try:
            stock = StockSymbol.objects.get(id=stock_id, watchlist__id=watchlist_id, watchlist__user=request.user)
            stock.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except StockSymbol.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class FetchStockDetailsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        symbol = request.data.get('symbol')
        watchlist_id = request.data.get('watchlist_id')
        base_url = 'https://www.alphavantage.co/query'
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': '1min',
            'apikey': ALPHA_VANTAGE_API_KEY
        }
        response = requests.get(base_url, params=params)
        data = response.json()

        try:
            time_series = data['Time Series (1min)']
            latest_time = sorted(time_series.keys())[0]
            latest_data = time_series[latest_time]

            stock_details = {
                'symbol': symbol,
                'last_price': latest_data['4. close'],
                'last_updated': latest_time
            }

            # Save stock details to the database
            watchlist = Watchlist.objects.get(id=watchlist_id, user=request.user)
            stock, created = StockSymbol.objects.get_or_create(
                watchlist=watchlist,
                symbol=symbol,
                defaults={
                    'last_price': stock_details['last_price'],
                    'last_updated': stock_details['last_updated']
                }
            )
            if not created:
                stock.last_price = stock_details['last_price']
                stock.last_updated = stock_details['last_updated']
                stock.save()

            return Response(stock_details)
        except KeyError:
            return Response({'error': 'Failed to fetch data for the provided symbol.'}, status=400)
