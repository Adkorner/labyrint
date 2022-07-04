# labyrint
* Labyrint je štvorcová sieť veľkosti m x n 
* obsahuje steny medzi niektorými políčkami 
* Na niektorých políčkach sa nachádzajú odmeny (napríklad mince)
# úloha labyrintu
Nájsť ľubovoľnú (stačí jednu) trasu zo štartového políčka, ktorá pozbiera všetky odmeny. Treba dať pozor, aby sa na žiadne políčko nestúpilo dvakrát.
# reprezantácia labyrintu
graf, v ktorom sú políčka labyrintu vrcholy grafu a hrany sú priechody medzi políčkami <br />
Labyrint je popísaný v textovom súbore, ktorý má tento tvar: 
* prvý riadok obsahuje dve čísla: počet riadkov a počet stĺpcov labyrintu
* ďalej nasledujú riadky so stenami a odmenami (v ľubovoľnom poradí)
* ak riadok obsahuje iba 2 čísla, označuje to políčko s odmenou (riadok, stĺpec), riadky aj stĺpce číslujeme o 0
* inak riadok obsahuje postupnosť aspoň dvoch políčok (riadok1, stĺpec1, riadok2, stĺpec2, …) - touto postupnosťou definuje nejaké steny v labyrinte: stena je medzi prvým a druhým políčkom, aj druhým a tretím, … atď.
