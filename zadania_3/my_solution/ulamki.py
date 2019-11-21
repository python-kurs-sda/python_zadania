"""
    Stworz klase Ulamek reprezentujaca liczby ulamkowe.
    Kazdy obiekt typu Ulamek powinien miec dwa atrybuty: self.licznik oraz self.mianownik.
    Glownym celem zadania jest dorobienie imlementacji, dzieki ktorej mozliwe stanie sie
    dodawanie, mnozenie, dzielenie i odejmowanie od siebie dwoch obiektow typu Ulamek. W tym celu nalezy
    przeladowac operatory +, -, *, / (magiczne metody: __add__, __sub__, __mul__, __div__).
    Pamietac trzeba o tym, ze przed dodaniem ulamkow, nalezy je sprowadzic do wspolnego mianowanika!
    Dla uproszczenia: nie trzeba skracac ulamkow, czyli ulamka 10/20 nie trzeba bedzie sprowadzac do postaci 1/2.
    Takie dzialania powinny sie zakonczyc sukcesem:
    >> half = Ulamek(1, 2)
    >> print(half.licznik)
    1
    >> print(half.mianownik)
    2
    >> quarter = Ulamek(1, 4)
    >> print(quarter.licznik)
    1
    >> print(quarter.mianownik)
    4
    >> result = half + quarter  # 1/2 + 1/4
    >> print(result.licznik)
    6
    >> print(result.mianownik)
    8
    Zauwaz, ze nie chcemy w tym przypadku skracac ulamka do postaci 3/4. Algorytm zamienia 1/2 na 4/8 a 1/4 na 2/8
    (po prostu wymnaza liczby przez siebie).
"""


class Fraction:

    def __init__(self, nominator, denominator: int):
        self.nominator = nominator
        self.denominator = denominator

    def get_common_denominator(self, fraction2):
        nominator1 = self.nominator * fraction2.denominator
        nominator2 = fraction2.nominator * self.denominator
        common_denominator = self.denominator * fraction2.denominator
        return nominator1, nominator2, common_denominator

    def __add__(self, other):
        if self.denominator != other.denominator:
            nominator1, nominator2, common_denominator = self.get_common_denominator(other)
            new_nominator = nominator1 + nominator2
            new_denominator = common_denominator
        else:
            new_nominator = self.nominator + other.nominator
            new_denominator = self.denominator
        return Fraction(new_nominator, new_denominator)

    def __sub__(self, other):
        if self.denominator != other.denominator:
            nominator1, nominator2, common_denominator = self.get_common_denominator(other)
            new_nominator = nominator1 - nominator2
            new_denominator = common_denominator
        else:
            new_nominator = self.nominator - other.nominator
            new_denominator = self.denominator
        return Fraction(new_nominator, new_denominator)

    def __mul__(self, other):
        new_nominator = self.nominator * other.nominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_nominator, new_denominator)

    def __truediv__(self, other):
        new_nominator = self.nominator * other.denominator
        new_denominator = self.denominator * other.nominator
        return Fraction(new_nominator, new_denominator)



