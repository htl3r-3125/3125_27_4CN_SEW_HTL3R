"""
Dieses Modul testet auf Palindrome
"""

# Metadaten zu dieser Datei:
__author__ = "Henry Koran"
__example__ = "SEW4/01/F1"
__date__ = "27.09.2026"
__version__ = "1.0"
__license__ = "GNU GPLv3"
__status__ = "Released"

import doctest
from unittest import skip


def is_palindrom(s: str):
    """
    Schaut nach ob ein String ein Palindrom ist
    :param s:
    :return:
    >>> is_palindrom("Anna")
    True
    >>> is_palindrom("Benedikt")
    False
    >>> is_palindrom("")
    False
    """
    if len(s) == 0: return False
    s_clean = s.lower()
    return s_clean == s_clean[::-1]


def is_palindrom_sentence(s: str):
    """
    Schaut nach ob ein Satz ein Palindrom ist
    :param s:
    :return:
    >>> is_palindrom_sentence("Was it a car or a cat I saw")
    True
    >>> is_palindrom_sentence("Das ist kein Palindrom")
    False
    >>> is_palindrom_sentence("")
    False
    """
    if len(s) == 0: return False
    s_clean = s.lower().replace(" ", "")
    return s_clean == s_clean[::-1]


def palindrom_product(x):
    """
    Ermittelt die größte Palindromzahl kleiner als x die das Produkt von zwei 3-Stelligen Zahlen ist
    :param x:
    :return:
    >>> palindrom_product(1000000)
    906609
    >>> palindrom_product(906606)
    888888
    >>> palindrom_product(-100)
    Traceback (most recent call last):
        ...
    ValueError: Die Zahl kann nicht negativ sein!
    """
    if x < 0: raise ValueError("Die Zahl kann nicht negativ sein!")
    biggest_number = 0
    for i in range(100,1000):
        for j in range(100,1000):
            if i*j >= x: continue
            if is_palindrom(str(i*j)):
                biggest_number = max(biggest_number, i*j)
    return biggest_number

def  get_dec_hex_palindrom(x):
    """
    Schaut was das größte Palindrom sowohl in Deciaml als auch in Hex ist, welche kleiner als x ist
    :param x:
    :return:
    >>> get_dec_hex_palindrom(1000)
    979
    >>> get_dec_hex_palindrom(100000)
    98689
    >>> get_dec_hex_palindrom(-100)
    Traceback (most recent call last):
        ...
    ValueError: Die Zahl kann nicht negativ sein!
    """
    if x < 0 : raise ValueError("Die Zahl kann nicht negativ sein!")
    biggest_number = 0
    for i in range(x-1,-1,-1):
        if is_palindrom(str(i)) and is_palindrom(str(hex(i)[2::])):
            biggest_number = max(i, biggest_number)
    return biggest_number

def main() -> None:
    doctest.testmod()


if __name__ == "__main__":
    main()
