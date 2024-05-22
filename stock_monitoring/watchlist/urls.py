from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, WatchlistView, StockSymbolView, FetchStockDetailsView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('watchlists/', WatchlistView.as_view(), name='watchlists'),
    path('watchlists/<int:watchlist_id>/', WatchlistView.as_view(), name='watchlist-detail'),
    path('watchlists/<int:watchlist_id>/stocks/', StockSymbolView.as_view(), name='stock-list'),
    path('watchlists/<int:watchlist_id>/stocks/<int:stock_id>/', StockSymbolView.as_view(), name='stock-detail'),
    path('fetch_stock/', FetchStockDetailsView.as_view(), name='fetch_stock_details'),
]