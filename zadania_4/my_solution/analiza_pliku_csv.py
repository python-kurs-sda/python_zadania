"""
    Zadanie bedzie polegalo na analizie pliku male_oscars.csv.
    Wczytaj plik csv i wykonaj ponizsze zadania:
    a) napisz funkcje, ktora zwroci imie i nazwisko najstarszego zdobywcy oskara z tej listy (kolumna year),
    b) napisz funkcje, ktora posortuje zdobywcow oskara od najstarszego do najmlodszego,
    c) napisz funkcje, ktora doda nowy wiersz do pliku: powinna ona przyjmowac tylko rok, imie i nazwisko zwyciezcy
    oraz tytul filmu - indeks powinien byc ustalany automatycznie.
    Zabezpiecz program na wypadek gdyby argument filename byl sciezka do nieistniejacego pliku. Użyj bloków
    try-except w każdej funkcji.
"""
import csv


def get_name_of_the_oldest_winner(filename: str) -> str:
    """Wyciaga imie i nazwisko najstarszego zwyciezcy oskarow.

    :param filename: sciazka do pliku.
    :return: imie i nazwisko najstarszego zwyciezcy jako string
    """
    try:
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter= ',')
            oldest_winner_age, oldest_winner_name = 0, None
            next(csv_reader)
            for row in csv_reader:
                if int(row[2]) > oldest_winner_age:
                    oldest_winner_age, oldest_winner_name = int(row[2]), row[3]
            return oldest_winner_name
    except OSError as e:
        print(e)


def sort_oscar_winners_due_to_age(filename: str) -> list:
    """Sortuje liste zwyciezcow wedlug ich wieku - od najstarszego do najmlodszego.

    :param filename: sciazka do pliku.
    :return: posortowana lista.
    """
    try:
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            sorted_list = sorted(csv_reader, key=lambda row: row[2])
            return sorted_list
    except OSError as e:
        print(e)


def add_new_winner(filename: str, year: int, age: int, name:str, title:str):
    """Dodaje nowy wiersz do pliku .csv.

    :param filename: sciazka do pliku.
    """
    try:
        with open(filename, 'r+') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                last_index = int(row[0])
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            csv_writer.writerow([int(last_index + 1), year, age, name, title])
    except OSError as e:
        print(e)


