"""Currency formatting, rounding, and ISO 4217 code validation helpers."""

from typing import Union

_CURRENCY_SYMBOLS = {
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
    "JPY": "¥",
    "INR": "₹",
    "CAD": "CA$",
    "AUD": "A$",
    "CNY": "CN¥"
}


def is_valid_currency_code(code: str) -> bool:
    """Validate 3-letter uppercase ISO currency code."""
    return bool(code and len(code) == 3 and code.isupper() and code.isalpha())


def format_currency(amount: Union[int, float], currency_code: str = "USD", include_symbol: bool = True) -> str:
    """Format numeric amount into monetary representation with symbol/code."""
    code = currency_code.upper()
    symbol = _CURRENCY_SYMBOLS.get(code, f"{code} ")
    formatted_val = f"{amount:,.2f}"
    if include_symbol:
        return f"{symbol}{formatted_val}"
    return f"{formatted_val} {code}"
