from binance.exceptions import BinanceAPIException
from client import BinanceFuturesClient
from logging_config import logger

class OrderManager:
    def __init__(self):
        self.api = BinanceFuturesClient().client

    def place_order(self, symbol, side, order_type, quantity, price=None):
        logger.info(f"Requesting {order_type} order: {side} {quantity} {symbol} at price {price}")
        
        try:
            params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity
            }
            
            if order_type == 'LIMIT':
                if not price:
                    raise ValueError("Price is required for LIMIT orders.")
                params['price'] = price
                params['timeInForce'] = 'GTC' # Good Till Canceled
                
            response = self.api.futures_create_order(**params)
            
            logger.info("Order successful!")
            logger.info(f"Details: OrderID: {response.get('orderId')}, Status: {response.get('status')}, ExecutedQty: {response.get('executedQty')}")
            return response
            
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.status_code} - {e.message}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")