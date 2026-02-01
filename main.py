#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Currency Converter CLI - Main Program

A command-line currency converter where users convert amounts
between different currencies using fixed exchange rates.
"""

# TODO 🇺🇸: Import utility functions from utils.py
# TODO 🇷🇴: Importă funcțiile utilitare din utils.py
from utils import (
    get_exchange_rates,
    normalize_currency,
    validate_currency,
    get_user_amount,
    get_user_currency
)


def convert_currency(amount, source_currency, target_currency):
    """
    Convert amount from source currency to target currency
    
    Args:
        amount: Amount to convert
        source_currency: Source currency code
        target_currency: Target currency code
    
    Returns:
        Converted amount as float
    """
    # TODO 🇺🇸: Get exchange rates, convert amount from
    #          source currency to USD (base), then from
    #          USD to target currency, return converted
    #          amount rounded to 2 decimals
    # TODO 🇷🇴: Obține ratele de schimb, convertește suma
    #          din valuta sursă în USD (bază), apoi din
    #          USD în valuta țintă, returnează suma
    #          convertită rotunjită la 2 zecimale

    # 🇺🇸 Write your code here (replace 'pass' with your code)
    # 🇷🇴 Scrie codul tău aici (înlocuiește 'pass' cu codul tău)
    rates = get_exchange_rates()
    amount_in_usd = amount / rates[source_currency]
    converted_amount = amount_in_usd * rates[target_currency]
    return round(converted_amount, 2)


def display_currencies():
    """
    Display available currencies
    """
    # TODO 🇺🇸: Get exchange rates, extract currency codes,
    #          format and display them as a comma-separated
    #          list
    # TODO 🇷🇴: Obține ratele de schimb, extrage codurile
    #          valutare, formatează și afișează-le ca listă
    #          separată prin virgule

    # 🇺🇸 Write your code here (replace 'pass' with your code)
    # 🇷🇴 Scrie codul tău aici (înlocuiește 'pass' cu codul tău)
    rates = get_exchange_rates()
    currencies = ', '.join(rates.keys())
    print(f"Valute disponibile: {currencies}")


def main():
    """
    Main program loop
    """
    # TODO 🇺🇸: Create infinite loop, display available
    #          currencies, get amount from user (handle
    #          'exit'), validate amount is numeric, get
    #          source currency, validate it, get target
    #          currency, validate it, perform conversion,
    #          display result formatted with 2 decimals
    # TODO 🇷🇴: Creează buclă infinită, afișează valutele
    #          disponibile, obține suma de la utilizator
    #          (gestionează 'exit'), validează că suma este
    #          numerică, obține valuta sursă, validează-o,
    #          obține valuta țintă, validează-o, efectuează
    #          conversia, afișează rezultatul formatat cu 2
    #          zecimale

    # 🇺🇸 Write your code here (replace 'pass' with your code)
    # 🇷🇴 Scrie codul tău aici (înlocuiește 'pass' cu codul tău)
    while True:
        display_currencies()
        amount = get_user_amount()
        if amount is None:
            print("Mulțumim că ai folosit Currency Converter CLI!")
            break
        source_currency = get_user_currency("Introdu valuta sursă (USD/EUR/GBP/RON): ")
        if source_currency is None:
            print("Mulțumim că ai folosit Currency Converter CLI!")
            break
        target_currency = get_user_currency("Introdu valuta țintă (USD/EUR/GBP/RON): ")
        if target_currency is None:
            print("Mulțumim că ai folosit Currency Converter CLI!")
            break
        converted_amount = convert_currency(amount, source_currency, target_currency)
        print(f"{amount:.2f} {source_currency} = {converted_amount:.2f} {target_currency}")
        print()


if __name__ == "__main__":
    main()
