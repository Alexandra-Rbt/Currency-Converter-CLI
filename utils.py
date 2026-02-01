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
    # TODO 🇺🇸: Return dictionary with exchange rates:
    #          {'USD': 1, 'EUR': 0.92, 'GBP': 0.79, 'RON': 4.62}
    # TODO 🇷🇴: Returnează dicționar cu ratele de schimb:
    #          {'USD': 1, 'EUR': 0.92, 'GBP': 0.79, 'RON': 4.62}

    # 🇺🇸 Write your code here (replace 'pass' with your code)
    # 🇷🇴 Scrie codul tău aici (înlocuiește 'pass' cu codul tău)
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
    # TODO 🇺🇸: Convert currency_input to uppercase and strip
    #          whitespace, return normalized currency code
    # TODO 🇷🇴: Convertește currency_input la uppercase și
    #          elimină spațiile, returnează codul valutar
    #          normalizat

    # 🇺🇸 Write your code here (replace 'pass' with your code)
    # 🇷🇴 Scrie codul tău aici (înlocuiește 'pass' cu codul tău)
    return currency_input.strip().upper()


def validate_currency(currency):
    """
    Validate if currency is available
    
    Args:
        currency: Currency code to validate
    
    Returns:
        True if currency is valid, False otherwise
    """
    # TODO 🇺🇸: Get exchange rates, check if currency exists
    #          in the rates dictionary, return True if valid,
    #          False otherwise
    # TODO 🇷🇴: Obține ratele de schimb, verifică dacă valuta
    #          există în dicționarul de rate, returnează True
    #          dacă este validă, False altfel

    # 🇺🇸 Write your code here (replace 'pass' with your code)
    # 🇷🇴 Scrie codul tău aici (înlocuiește 'pass' cu codul tău)
    rates = get_exchange_rates()
    return currency in rates


def get_user_amount():
    """
    Get and validate user's amount input
    
    Returns:
        Valid amount as float
    """
    # TODO 🇺🇸: Create infinite loop for input validation,
    #          get user input, check if it's 'exit' (return
    #          None), try to convert to float, return valid
    #          amount or print error message on invalid input
    # TODO 🇷🇴: Creează buclă infinită pentru validarea
    #          inputului, obține input de la utilizator,
    #          verifică dacă este 'exit' (returnează None),
    #          încearcă să convertească la float, returnează
    #          suma validă sau afișează mesaj de eroare la
    #          input invalid

    # 🇺🇸 Write your code here (replace 'pass' with your code)
    # 🇷🇴 Scrie codul tău aici (înlocuiește 'pass' cu codul tău)
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
    # TODO 🇺🇸: Create infinite loop for input validation,
    #          get user input, normalize it, check if it's
    #          'exit' (return None), validate currency,
    #          return valid currency or print error message
    #          on invalid input
    # TODO 🇷🇴: Creează buclă infinită pentru validarea
    #          inputului, obține input de la utilizator,
    #          normalizează-l, verifică dacă este 'exit'
    #          (returnează None), validează valuta, returnează
    #          valuta validă sau afișează mesaj de eroare la
    #          input invalid

    # 🇺🇸 Write your code here (replace 'pass' with your code)
    # 🇷🇴 Scrie codul tău aici (înlocuiește 'pass' cu codul tău)
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
