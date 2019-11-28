"""
    Napisz funkcje obliczajaca pierwiastki rownania kwadratowego (przypomnienie:
    http://matematyka.pisz.pl/strona/54.html).
    Funkcja powinna przyjmowac trzy argumenty - wartosci a, b i c z równania o postaci ax^2 + bx + c = 0,
    powinna zwracac dwa pierwiastki rownania kiedy delta>0 lub jeden kiedy delta=0,
    w zaleznosci od doboru wspolczynnikow a,b,c. W przypadku kiedy delta wyjdzie ujemna - rownanie nie ma rozwiazan.
    Nalezy w takim przypadku zglosic wyjatek NoSolutionError, ktory nalezy wczesniej zdefiniowac
    (to jest nasz wlasny wyjatek).
"""

from typing import Union


class NoSolutionError(Exception):
    pass


def solve_quadratic_equation(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Union[
    tuple, int, float]:
    """Znajduje pierwiastki rownania kwadratowego.

    :param a: wspolczynnik a rownania,
    :param b: wspolczynnik b rownania
    :param c: wspolczynnik c rownania
    :return: tuple z dwoma pierwiatkami lub liczba jako jedyny pierwiastek.
    """
    delta = b ** 2 - 4 * a * c
    x1 = 0
    x2 = 0
    if delta > 0:
        x1 = (-b - delta ** 0.5) / 2 * a
        x2 = (-b + delta ** 0.5) / 2 * a
        return x1, x2
    elif delta == 0:
        x1 = -b / 2 * a
        return x1
    else:
        raise NoSolutionError


if __name__ == '__main__':
    try:
        print(solve_quadratic_equation(1, 2, 5))
    except NoSolutionError:
        print('Delta ujemna. Brak rozwiązania')