# Jira reader
> Projekt służy do odczytania informacji z aplikacji Jira

Program odczytuje informacje z aplikacji Jira, poprzez wywoływanie odpowiednich stron www. Z odczytanych informacji
budowane są raporty i wyświetlane użytkownikowi

_Więcej informacji znajduje się w [Wikipedii projektu][wiki]._

## Instalacja
Należy pobrać wersję dystrybucyjną programu i skopiować w dowolne miejsce na dysku. 

## Przykład użycia
W systemie Windows należy uruchomić plik **jira_reader.exe**

## Środowisko deweloperskie
#### Python
Należy pobrać wersję [Pythona 3.10.4][python-version] w postaci pliku 'Windows installer' i zainstalować na komputerze deweloperskim.
#### Pytest
Pakiet jest wykorzystywany do uruchamiania testów jednostkowych. Należy zainstalować pakiet Pytest poleceniem:
```sh
pip install pytest
```
#### Pyinstaller
Pakiet jest wykorzystywany do przygotowania wersji dystrybucyjnej programu. Pakiet należy zainstalować poleceniem:
```sh
pip install pyinstaller
```
#### Requests
Pakiet służy do obsługi protokołu http. Pakiet należy zainstalować poleceniem:
```sh
python -m pip install requests
```
> Uwaga: od wersji 1.1.0 pakiet `requests` został wycofany i zastąpiony pakietem `selenium`
#### Beautifulsoup4
Pakiet służy do transformacji HTML-a do drzewa zawierającego obiekty Pythona. Pakiet należy zainstalować poleceniem:
```sh
pip install beautifulsoup4
```
#### Lxml
Pakiet służy do parsowania HTML-a i XML-a. Jest wykorzystywany jako parser w module `beautifulsoup4`. Pakiet należy
zainstalować poleceniem:
```sh 
pip install lxml
```
#### Selenium
Pakiet jest wykorzystywany do pobierania zawartości stron Jiry. Pakiet należy zainstalować poleceniem:
```sh
pip install -U selenium
```
Po instalacji pakietu należy pobrać [sterownik do przeglądarki Chrome][chromium-driver]. Sterownik należy dobrać do
posiadanej wersji przeglądarki.
Po pobraniu odpowiedniego pliku `zip`, należy go rozpakować i znajdujący się w środku plik `.exe` wgrać do Pythona do 
katalogu `scripts`. W przypadku, gdy Python został uruchomiony jako środowisko wirtualne w projekcie, to katalogiem do
którego należy wgrać plik `.exe` jest `projekt/venv/scripts`.
W wersji 1.1.0 obsługiwana jest tylko przeglądarka Chrome.
#### prettytable
Pakiet jest wykorzystywany do wyświetlania na konsoli raportu z pobranych informacji.
```sh
python -m pip install -U prettytable
```

#### Lista pakietów
Prawidłowe środowisko deweloperskie powinno zawierać poniższą listę pakietów:
```sh
Package                   Version
------------------------- -----------
altgraph                  0.17.2
async-generator           1.10
atomicwrites              1.4.0
attrs                     21.4.0
beautifulsoup4            4.11.1
certifi                   2022.5.18.1
cffi                      1.15.1
charset-normalizer        2.0.12
colorama                  0.4.4
cryptography              37.0.4
future                    0.18.2
h11                       0.13.0
idna                      3.3
iniconfig                 1.1.1
lxml                      4.9.0
outcome                   1.2.0
packaging                 21.3
pefile                    2022.5.30
pip                       22.1.2
pluggy                    1.0.0
prettytable               3.4.1
py                        1.11.0
pycparser                 2.21
pyinstaller               5.1
pyinstaller-hooks-contrib 2022.7
pyOpenSSL                 22.0.0
pyparsing                 3.0.9
PySocks                   1.7.1
pytest                    7.1.2
pywin32-ctypes            0.2.0
requests                  2.28.0
selenium                  4.4.0
setuptools                57.0.0
sniffio                   1.2.0
sortedcontainers          2.4.0
soupsieve                 2.3.2.post1
tomli                     2.0.1
trio                      0.21.0
trio-websocket            0.9.2
urllib3                   1.26.9
wcwidth                   0.2.5
wheel                     0.36.2
wsproto                   1.1.0
```

## Przygotowanie wersji dystrybucyjnej programu
Do przygotowania wersji dystrybucyjnej programu potrzebny jest Pyinstaller oraz plik cli.py.
Aby utworzyć wersję dystrybucyjną należy wykonać polecenie:
```sh
pyinstaller cli.py --name jira_reader
```
gdzie:
- **pyinstaller** - nazwa modułu, który tworzy wersję dystrybucyjną programu
- **cli.py** - nazwa skryptu, z informacjami dla pyinstaller-a
- **--name jira_reader** - nazwa docelowa programu exe, który zostanie utworzony

Wersja dystrybucyjna tworzona jest w katalogu:
> .\dist\jira_reader


## Historia zmian

* 1.1.0
  * ...
* 1.0.0
    * Odczytanie i wyświetlenie informacji o jednym wskazanym tasku z Jiry. Pobierane informacje to: czas planowany,
  czas zalogowany, czas pozostały.

## Licencja

Program jest rozpowszechniany na podstawie licencji ``GNU GPL`` 
[https://pl.wikipedia.org/wiki/GNU_General_Public_License][licence]

## Autor

[PiotrZET][mail]

<!-- Markdown link & img dfn's -->
[wiki]: https://github.com/ZalewskiPiotr/jira_reader/wiki
[licence]: https://pl.wikipedia.org/wiki/GNU_General_Public_License
[python-version]: https://www.python.org/downloads/release/python-3104/
[chromium-driver]: https://chromedriver.chromium.org/downloads
[mail]: mailto:1piotrzalewski@gmail.com