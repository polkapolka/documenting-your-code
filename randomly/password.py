"""
random password
"""
import random
import string
from typing import Optional, Iterable


def generate_password(chars: int, punctuation: bool, invalid_chars: Optional[Iterable[str]]=None) -> str:
    """ Generate a valid password.

    Args:
        chars: number of characters in the password
        punctuation: whether punctuation is included in the valid chars.
        invalid_chars: characters to exclude from the password

    Returns: str valid password
    """
    valid_chars = string.ascii_letters + string.digits

    if punctuation:
        valid_chars += string.punctuation

    if invalid_chars:
        for invalid_char in invalid_chars:
            valid_chars = valid_chars.replace(invalid_char, "")

    password_chars = random.choices(valid_chars, k=chars)
    password = "".join(char for char in password_chars)

    return password
