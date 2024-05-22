from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Watchlist, StockSymbol

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class StockSymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockSymbol
        fields = ['id', 'symbol', 'last_price', 'last_updated']

class WatchlistSerializer(serializers.ModelSerializer):
    stocks = StockSymbolSerializer(many=True, read_only=True)

    class Meta:
        model = Watchlist
        fields = ['id', 'name', 'stocks']