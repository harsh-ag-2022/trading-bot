import os
from binance.client import Client
from binance.enums import *
from logging_config import logger
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.environ.get("BINANCE_API_KEY")
        api_secret = os.environ.get("BINANCE_API_SECRET")
        
        if not api_key or not api_secret:
            logger.error("API keys not found in environment variables.")
            raise ValueError("Please set BINANCE_API_KEY and BINANCE_API_SECRET.")
            
        logger.info("Initializing Binance Testnet Client...")
        # Initialize client and force testnet URL
        self.client = Client(api_key, api_secret, testnet=True)
        # Verify connection
        try:
            self.client.futures_ping()
            logger.info("Successfully connected to Binance Futures Testnet.")
        except Exception as e:
            logger.error(f"Network failure or API error: {e}")
            raise