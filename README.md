# Currency-Converter-CLI
A simple and efficient command-line currency converter developed in Python. Allows users to convert amounts between different currencies using fixed exchange rates.

# About The Project
Currency Converter CLI is a command-line application that enables quick conversion between four major currencies: USD, EUR, GBP, and RON. The project emphasizes proper input validation and a user-friendly experience.

# Key Features
Conversion between 4 currencies (USD, EUR, GBP, RON)  
 Complete input validation  
 Error handling with clear messages  
 Formatting with 2 decimal places  
 Multiple conversions in a single session  
 'exit' command for quick termination  

 # Installation Steps
Clone the repository:
```bash
git clone https://github.com/username/currency-converter-cli.git
cd currency-converter-cli
```

# Running
```bash
python main.py
```

#

# Successful Conversion Example
```
Available currencies: USD, EUR, GBP, RON
Enter amount (or 'exit' to quit): 100
Enter source currency (USD/EUR/GBP/RON): USD
Enter target currency (USD/EUR/GBP/RON): EUR
100.00 USD = 92.00 EUR
```


# main.py
- `convert_currency()` - Converts amount between two currencies
- `display_currencies()` - Displays available currencies
- `main()` - Main program loop

# utils.py
- `get_exchange_rates()` - Returns dictionary with exchange rates
- `normalize_currency()` - Normalizes user input
- `validate_currency()` - Validates if currency is available
- `get_user_amount()` - Gets and validates amount
- `get_user_currency()` - Gets and validates currency

# Implemented Concepts
- Data structures (dictionaries)
- Input validation
- Exception handling (try-except)
- Modular organization
- String formatting (f-strings)
- While loops for continuous validation
