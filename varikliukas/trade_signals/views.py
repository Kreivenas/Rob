from django.shortcuts import render
from binance.client import Client
from .models import TradeSignal

def trade_signal_list(request):
    # Connect to Binance API
    client = Client('your_api_key', 'your_api_secret')

    # Get trade signals from the database
    trade_signals = TradeSignal.objects.all()

    # Retrieve trade signals from the Binance API
    # Replace 'your_symbol' with the specific symbol you want to retrieve
    binance_trade_signals = client.get_recent_trades(symbol='your_symbol')

    context = {
        'trade_signals': trade_signals,
        'binance_trade_signals': binance_trade_signals,
    }

    return render(request, 'trade_signals/trade_signal_list.html', context)
def home(request):
    return render(request, 'home.html')