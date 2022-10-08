""" Skrypt z funkcjami pomocniczymi

Ten skrypt zawiera funkcje pomocnicze wykorzystywane podczas pisania kodu.

Skrypt zawiera funkcje:
-----------------------
- save_content_to_file()

"""


def save_content_to_file(content: str, file_path: str):
    """ Zapis podanej zawartości do podanego pliku

    :param content: Zawartość do zapisu
    :type content: str
    :param file_path: ścieżka z nazwą pliku
    :type file_path: str
    :return: ---
    :rtype: ---
    """
    with open(file_path, 'w') as file:
        file.write(content)
