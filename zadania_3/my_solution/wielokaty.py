"""
    Na podstawie klasy abstrakcyjnej Wielokat, stworz 3 klasy dziedziczace: Kwadrat, Prostokat, Trojkat.
    Kazda z tych klas musi byc konkretna (a nie abstrakcyjna), powinna wiec nadpisywac wszystkie metody
    abstrakcyjne z klasy Wielokat. Kazda konkretna klasa powinna miec definicje konstruktora __init__
    (dla przykładu obiekt typu Kwadrat, powinien miec jeden atrybut self.bok, obiekt prostokat dwa atrybuty:
    self.bok1, self.bok2, a trojkat self.bok, self.wysokosc).
    Na koniec stworz funkcje zarzadzajaca obiektami stworzonych klas, ktora w petli bedzie obliczala pola
    dla kazdego obiektu.
"""

from abc import ABC, abstractmethod
from typing import Union


class Polygon(ABC):

    @abstractmethod
    def get_area(self) -> Union[int, float]:  # Union sugeruje ze funkcja moze zwrocic inta albo floata
        """Metoda ma za zadanie obliczyc pole danego obiektu.

        Ze wzgledu na fakt, iz nie wiemy w tym momencie jaki to jest wielokat,
        nie potrafimy obliczyc jego pola. Do redefinicji w klasie dziedziczacej.

        :return: wartosc pola jako liczba calkowita lub wymierna.
        """
        ...


class Square(Polygon):

    def __init__(self, side: Union[int, float]):
        self.side = side

    def get_area(self) -> Union[int, float]:
        return self.side ** 2


class Rectangle(Polygon):

    def __init__(self, side1: Union[int, float], side2: Union[int, float]):
        self.side1 = side1
        self.side2 = side2

    def get_area(self) -> Union[int, float]:
        return self.side1 * self.side2


class Triangle(Polygon):

    def __init__(self, side: Union[int, float], height: Union[int, float]):
        self.side = side
        self.height = height

    def get_area(self) -> Union[int, float]:
        return self.side * self.height * 0.5


polygons = [Square(2), Rectangle(2, 3), Triangle(3, 4)]


def get_area(polygons: list) -> list:
    """Oblicza pola wszystkich wielokatow podanych w liscie.

    :param polygons: lista obiektow dziedziczacych po Wielokat.
    :return: lista obliczonych pol.

    """
    return [figure.get_area() for figure in polygons]




