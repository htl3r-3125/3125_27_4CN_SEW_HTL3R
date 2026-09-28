"""
Dieses Modul beschäftigt sich mit Rekursion
"""

# Metadaten zu dieser Datei:
__author__ = "Henry Koran"
__example__ = "SEW4/01/F3"
__date__ = "28.09.2026"
__version__ = "1.0"
__license__ = "GNU GPLv3"
__status__ = "Released"

import doctest
from time import time


def M(n):
    """
    McCarthy-91-Funktion
    :param n:
    :return:
    """
    if n <= 100:
        return M(M(n + 11))
    else:
        return n - 10


def main() -> None:
    """
    Testet die McCarthy-91-Funktion
    Führt außerdem die Doctests aus.
    """
    doctest.testmod()

    t0 = time()
    try:
        m_list: list[int] = []
        m_dict: dict[int, int] = {}
        for i in range(200):
            m_list.append(M(i))
            m_dict[i] = M(i)
    except ValueError:
        pass
    t1 = time()
    print(f"Dauer: {t1 - t0}")


if __name__ == "__main__":
    main()
