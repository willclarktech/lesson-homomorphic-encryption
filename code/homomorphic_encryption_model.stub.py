from typing import List, Tuple

from paillier import add, encrypt, multiply, PublicKey


def encrypted_celsius_to_fahrenheit(public_key: PublicKey, ciphertext: int) -> int:
    # °F = °C * 1.8 + 32
    pass


def encrypted_price_calculator(
    public_key: PublicKey,
    # a list of (encrypted price, quantity) tuples
    encrypted_cart: List[Tuple[int, int]],
) -> int:
    pass
