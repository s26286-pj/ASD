# ASD

## Zadanie 1
Wyniki dla tablicy 300000 elementowej z losowo generowanymi liczbami w:
Przedziale -10000 do 10000:

|Algorytm|Tablica losowa|Tablica posortowana|Tablica odwrotnie posortowana|
|---|---|---|---|
|Quicksort|0.9979009628295898|Błąd*|Błąd*|
|HeapSort|2.2236390113830566|2.06311297416687|2.1068928241729736
|MergeSort|1.4283130168914795|0.8539118766784668|0.8999197483062744


*przekroczona została pythonowa maksymalna głębokość rekursji (1000) przy algorytmie.

Najwolniejszym w każdym przypadku był algorytm heapsort. 

Quicksort jest najszybszym w przypadku tablicy losowej - niestety przy tablic posortowanych i posortowanych odwrotnie występuje duża liczba rekursji wyrzucając wyjątek w Pythonie uniemożliwiając wykonanie pomiaru dla zadanej w zadaniu minimalnej wielkości tablicy

Merge sort jest najszybszy w przypadku tablic posortowanych Omega(n log n). Podobny wynik został osiągnięty dla tablicy odwrotnie posortowanej co jest całkowitym zaskoczeniem - jest to teoretycznie najgorszy molżliwy scenariusz dla tego algorytmu powinien on być zbliżony do tablicy nieuporządkowanej thete(n log n)

Heap sort wykazał się duża stabilnością wśród 3 przypadków zgodnie z oczekiwaniami. O(n log n). Najlepszy scenariusz dla tego algorytmu to tablica z takimi samymi elementami O(n).
