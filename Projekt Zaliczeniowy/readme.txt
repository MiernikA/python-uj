Dokumentacja projektu "Gra w życie"

Opis projektu
Projekt "Gra w życie" implementuje klasyczną grę w życie stworzoną przez matematyka Johna Conwaya. 
Gra polega na ewolucji komórek w dwuwymiarowej siatce na podstawie prostych zasad. Każda komórka może być w stanie "żywym" lub "martwym", a jej stan zmienia się w zależności od liczby żywych sąsiadów.

Struktura projektu
Projekt składa się z dwóch plików: main.py i data.py.

Plik main.py
Plik main.py zawiera główny kod implementacji gry w życie.

1. WARTOŚCI STAŁYCH
BT_WIDTH, BT_HEIGHT: Szerokość i wysokość przycisków.
GRID_SIZE: Rozmiar siatki.
CELL_SIZE: Rozmiar pojedynczej komórki.
CELL_BORDER_WIDTH: Grubość ramki komórki.
UPDATE_DELAY: Opóźnienie w milisekundach między krokami ewolucji.
LIVING_RULE: Zasady przetrwania żywych komórek.
RESPAWN_RULE: Zasady ożywiania martwych komórek.

2. Funkcje
initialize_grid(): Inicjalizuje pustą siatkę.
update_grid(): Aktualizuje stan komórek na podstawie zasad gry.
step(): Wykonuje krok ewolucji.
step_back(): Cofa ostatni krok ewolucji.
draw_grid(): Rysuje siatkę na ekranie.
toggle_running(): Włącza lub wyłącza automatyczną aktualazcje ewulcji.
go_one_step(): Wykonuje pojedynczy krok ewolucji.
clear_grid(): Czyści siatkę.
random_grid(): Wypełnia siatkę losowymi komórkami.
toggle_cell(row, col): Przełącza stan komórki o podanych współrzędnych.
select_pattern(pattern_name): Ustawia wybrany wzór do wstawienia.
apply_pattern(pattern): Wstawia wzór do aktualnej siatki.
apply_selected_pattern(): Wstawia wybrany wzór z listy dostępnych wzorów.
select_rule(rule_name): Ustawia wybraną zasadę ewolucji.
apply_selected_rule(): Zastosowuje wybraną zasadę ewolucji.

3. Interfejs użytkownika
Korzysta z biblioteki Tkinter do stworzenia prostego interfejsu graficznego.
Przyciski umożliwiają kontrolę rozgrywki, wstawianie wzorów, zmianę zasad ewolucji.

Plik data.py
Plik data.py zawiera dane potrzebne do projektu, takie jak wzory i zasady ewolucji. Struktura tego pliku obejmuje:

4. Klasa Data
patterns: Słownik zawierający różne wzory początkowe, takie jak Glider, Blinker itd.
rules: Słownik zawierający różne zasady ewolucji, takie jak Conway's 23/3, 34/34 itd.


5. Instrukcje obsługi
Przycisk "Start/Stop": Rozpoczyna lub zatrzymuje automatyczną ewolucję.
Przycisk "Random": Wypełnia siatkę losowymi komórkami.
Przycisk "Clear": Czyści siatkę.
Przycisk "Step": Wykonuje pojedynczy krok ewolucji.
Przycisk "Step Back": Cofa ostatni krok ewolucji.
Wybór wzoru: W rozwijanym menu można wybrać różne wzory do wstawienia na siatkę.
Przycisk "Apply Pattern": Wstawia wybrany wzór na siatkę.

Wybór zasady ewolucji: W rozwijanym menu można wybrać różne zasady ewolucji.
Przycisk "Apply Rule": Zastosowuje wybraną zasadę ewolucji.
