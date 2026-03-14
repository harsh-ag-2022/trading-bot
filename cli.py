import argparse
import sys
from orders import OrderManager
from logging_config import logger

def main():
    parser = argparse.ArgumentParser(description="Simplified Trading Bot (Binance Futures Testnet)")
    
    parser.add_argument('--symbol', type=str, required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument('--side', type=str, choices=['BUY', 'SELL'], required=True, help="Order side: BUY or SELL")
    parser.add_argument('--type', type=str, choices=['MARKET', 'LIMIT'], required=True, help="Order type: MARKET or LIMIT")
    parser.add_argument('--quantity', type=float, required=True, help="Order quantity")
    parser.add_argument('--price', type=float, help="Order price (Required if type is LIMIT)")

    args = parser.parse_args()

    # Input validation for LIMIT price
    if args.type == 'LIMIT' and args.price is None:
        parser.error("--price is required when --type is LIMIT")

    logger.info("--- Starting New Order Request ---")
    
    try:
        manager = OrderManager()
        manager.place_order(
            symbol=args.symbol.upper(),
            side=args.side.upper(),
            order_type=args.type.upper(),
            quantity=args.quantity,
            price=args.price
        )
    except Exception as e:
        logger.error("Failed to execute CLI command due to startup errors.")
        sys.exit(1)

if __name__ == "__main__":
    main()