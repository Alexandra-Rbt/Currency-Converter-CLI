#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Currency Converter CLI - Utility Functions

Helper functions for currency conversion logic.
"""


def get_exchange_rates():
    """
    Get exchange rates dictionary
    
    Returns:
        Dictionary with currency codes as keys and rates as values
        (USD is base currency with rate 1.0)
    """
    return {
        'USD': 1.0,
        'EUR': 0.92,
        'GBP': 0.79,
        'RON': 4.62
    }


def normalize_currency(currency_input):
    """
    Normalize user input for consistent comparison
    
    Args:
        currency_input: Raw user input string
    
    Returns:
        Normalized currency code in uppercase
    """
    return currency_input.strip().upper()


def validate_currency(currency):
    """
    Validate if currency is available
    
    Args:
        currency: Currency code to validate
    
    Returns:
        True if currency is valid, False otherwise
    """
    rates = get_exchange_rates()
    return currency in rates


def get_user_amount():
    """
    Get and validate user's amount input
    
    Returns:
        Valid amount as float
    """
    while True:
        user_input = input("Introdu suma (sau 'exit' pentru a ieși): ")
        if user_input.lower().strip() == 'exit':
            return None
        try:
            amount = float(user_input)
            return amount
        except ValueError:
            print("Sumă invalidă! Te rog introdu un număr valid.")


def get_user_currency(prompt):
    """
    Get and validate user's currency input
    
    Args:
        prompt: Prompt message to display
    
    Returns:
        Valid currency code or None if user wants to exit
    """

    rates = get_exchange_rates()
    available_currencies = ', '.join(rates.keys())
    while True:
        user_input = input(prompt)
        normalized = normalize_currency(user_input)
        if normalized == 'EXIT':
            return None
        if validate_currency(normalized):
            return normalized
        else:
            print(f"Valută invalidă! Te rog alege din: {available_currencies}")
