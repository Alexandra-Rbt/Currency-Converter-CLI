#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Currency Converter CLI - Main Program

A command-line currency converter where users convert amounts
between different currencies using fixed exchange rates.
"""
from utils import (
    get_exchange_rates,
    normalize_currency,
    validate_currency,
    get_user_amount,
    get_user_currency
)


def convert_currency(amount, source_currency, target_currency):
    rates = get_exchange_rates()
    amount_in_usd = amount / rates[source_currency]
    converted_amount = amount_in_usd * rates[target_currency]
    return round(converted_amount, 2)


def display_currencies():
    """
    Display available currencies
    """
    rates = get_exchange_rates()
    currencies = ', '.join(rates.keys())
    print(f"Valute disponibile: {currencies}")


def main():
    """
    Main program loop
    """
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
