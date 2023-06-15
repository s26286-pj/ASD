# ASD

## Zadanie 1
Wyniki dla tablicy 300000 elementowej z losowo generowanymi liczbami w:
Przedziale -10000 do 10000:

|Algorytm|Czas wykonania[s]|
|---|---|
|Quicksort|0.9423463344573975|
|HeapSort|2.2103099822998047|
|MergeSort|1.42451810836792|

Przedziale -10 do 10
|Algorytm|Czas|
|---|---|
|Quicksort|Brak wyników*|
|HeapSort|2.0884158611297607|
|MergeSort|1.3351800441741943|

*przekroczona została pythonowa maksymalna głębokość rekursji (1000) przy algorytmie quicksort

Quicksort jest najszybszym algorytmem sortowania z trójki dla danych losowych, przy jego implementacji w należy pamiętać o własnościach używanego języka programowania.
