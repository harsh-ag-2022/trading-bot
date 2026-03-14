# Trading Bot

A Python-based cryptocurrency trading bot that automates trading operations on Binance with support for limit and market orders.

## Features

- **CLI Interface**: Command-line interface for easy order placement and management
- **Order Management**: Support for LIMIT and MARKET order types
- **Binance Integration**: Direct integration with Binance API via python-binance
- **Async Support**: Asynchronous operations using aiohttp and websockets
- **Logging**: Comprehensive logging for tracking trades and debugging
- **Configuration**: Environment-based configuration with python-dotenv

## Requirements

- Python 3.8+
- See `requirements.txt` for dependencies

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd trading-bot
```

2. Create a virtual environment:
```bash
python -m venv trade-bot
trade-bot\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your Binance API credentials:
```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

## Usage

### Place a LIMIT order:
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 90000
```

### Place a MARKET order:
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

## Project Structure

- `cli.py`: Command-line interface entry point
- `client.py`: Binance API client wrapper
- `orders.py`: Order management and execution logic
- `logging_config.py`: Logging configuration
- `requirements.txt`: Project dependencies
- `trade-bot/`: Virtual environment directory

## Logging

All trading activity is logged to `trading_bot.log`. Check the logs for detailed information about orders, errors, and API interactions.

## Security

**Important**: Never commit your `.env` file or API credentials to version control. Use environment variables for sensitive information.

## License

MIT License
