"""
random facts
"""
import requests
from requests.exceptions import RequestException
from typing import Union, Dict


def generate_random_fact(output_format: str, language: str) -> Union[Dict, str]:
    """Return fact from random fact url as dictionary or str.

    Args:
        output_format: html, json, txt, or md
        language: en or de

    Returns: dict or txt version of fact

    """
    if language not in {"en", "de"}:
        raise ValueError(f"{language} is not supported.")

    if output_format not in {"html", "json", "txt", "md"}:
        raise ValueError(f"{output_format} is not supported.")

    response = requests.get(
        f"https://uselessfacts.jsph.pl/random.{output_format}?language={language}"
    )

    if response.status_code == 200:
        if output_format == "json":
            fact = response.json()
        else:
            fact = response.text
    else:
        raise RequestException(
            f"Something went wrong. Request returned status {response.status_code}."
        )

    return fact
