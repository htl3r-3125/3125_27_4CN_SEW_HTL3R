"""
Dieses Modul beschäftigt sich mit der Collatzfolge
"""

# Metadaten zu dieser Datei:
__author__ = "Henry Koran"
__example__ = "SEW4/01/F2"
__date__ = "28.09.2026"
__version__ = "1.0"
__license__ = "GNU GPLv3"
__status__ = "Released"

import doctest
from typing import List


def collatz(n):
    """
    gibt einen Wert nach den Collatz-Regeln zurück
    :param n:
    :return:
    >>> collatz(4)
    2
    >>> collatz(5)
    16
    """
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(n * 3 + 1)


def collatz_sequence(number: int) -> list[int]:
    """
    :param number: Startzahl
    :return: Collatz Zahlenfolge, resultierend aus n
    >>> collatz_sequence(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    if number == 1:
        return [1]
    else:
        l = collatz_sequence(collatz(number))
        l.insert(0, number)
        return l


def longest_collatz_sequence(n: int) -> tuple[int, int]:
    """
    :param number: Startzahl
    :return: Startwert und Länge der längsten Collatz Zahlenfolge deren Startwert <=n ist
    >>> longest_collatz_sequence(100)
    (97, 119)
    """

    longest_num = 0
    longest_num_length = 0

    for i in range(n - 1, 1, -1):
        if len(collatz_sequence(i)) > longest_num_length:
            longest_num = i
            longest_num_length = len(collatz_sequence(i))
    return longest_num, longest_num_length


def main() -> None:
    doctest.testmod()


if __name__ == "__main__":
    main()
