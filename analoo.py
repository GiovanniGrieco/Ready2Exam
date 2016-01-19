'''
ANALOO - LICENSED UNDER THE MIT LICENSE

Copyright (c) 2016 Giovanni Grieco <giovanni.grc96@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the 
Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import random

doms = [
	"Leggi di composizione dei numeri reali e loro proprietà.",
	"Relazione d'ordine in R, compatibilità con le leggi di composizione e proprietà.",
	"Definizione di relazione d'ordine.",
	"Definizione di assioma di Dedekind.",
	"Definizione di N, Z, Q e loro relazioni come sottoinsiemi.",
	"Relazione tra Q ed R con lemma sull'irrazionalità. Dimostrala per contraddizione.",
	"Teorema sulla non completezza di Q. Dimostralo per assurdo.",
	"Rappresentazione grafica della relazione d'ordine di R e costruzione della diagonale del quadrato unitario.",
	"Definizione di Maggiorante e Minorante di un insieme.",
	"Concetto di insieme limitato superiormente e inferiormente.",
	"Definizione di Massimo e Minimo di un insieme.",
	"Unicità del Massimo e Minimo di un insieme.",
	"Dimostrazione della possibile non esistenza di un max/min per un insieme.",
	"Teorema dell'esistenza del sup e inf di un insieme.",
	"Definizione del sup e inf di un insieme.",
	"Concetto dei simboli ±∞",
	"Principio del minimo intero.",
	"Proprietà archimedea dei numeri reali (con corollario e osservazione).",
	"Teorema dell'esistenza della radice n-esima.",
	"Teorema di densità di Q in R. Dimostralo.",
	"Teorema di densità di R\\Q in R. Dimostralo.",
	"Principio di induzione completa dei numero reali.",
	"Disequazione del Brnoulli, legge di Gauss.",
	"Cosa sono i fattoriali?",
	"Binomio di Newton.",
	"Caratteristiche generali (notazione e ordinamento) dei numeri complessi.",
	"Leggi di composizione dei numeri complessi e proprietà.",
	"Rappresentazione dei numeri complessi sul piano di Gauss.",
	"Concetto di Rez, Imz, i e i^2.",
	"Concetto di numero immaginario puro.",
	"Rappresentazione dei numeri complessi in forma algebrica.",
	"Operazioni tra numeri complessi in forma algebrica.",
	"Definizione di coniugato di un numero complesso con proprietà.",
	"Principio di identità dei numeri complessi.",
	"Rappresentazione trigonometrica dei numeri complessi.",
	"Potenza n-esima di z ∈ C e formula di Demoivre.",
	"Definizione di radice n-esima di un numero complesso. Dimostralo.",
	"Formula risolutiva delle radici n-esime di un numero complesso.",
	"Formula risolutiva delle equazioni di II grado in C.",
	"Definizione di funzione e proprietà.",
	"Definizione di funzione ristretta.",
	"Definizione di funzione ridotta.",
	"Definizione di funzione invertibile.",
	"Definizione di funzione monotona.",
	"Funzione retta.",
	"Funzione valore assoluto.",
	"Funzione potenza n-esima pari.",
	"Funzione radice n-esima.",
	"Funzione potenza n-esima dispari.",
	"Funzione potenza n-esima negativa.",
	"Funzione potenza razionale.",
	"Funzione potenza reale.",
	"Funzione esponenziale.",
	"Funzione logaritmo.",
	"Funzione trigonometrica.",
	"Operazioni tra funzioni.",
	"Funzione composta.",
	"Funzione pari/dispari.",
	"Definizione di intorno.",
	"Definizione di punto di accumulazione.",
	"Definizione di punto isolato.",
	"Definizione di limite.",
	"Teorema sull'esistenza unica del limite. Dimostrala per contraddizione.",
	"Definizione di funzione continua e teorema delle funzione elementari.",
	"Definizione di limite destro e sinistro e teorema.",
	"Operazioni tra limiti di funzioni.",
	"Teorema del confronto (I versione).",
	"Teorema del confronto (II versione)",
	"Teorema della permanenza del segno. Dimostralo.",
	"Limiti notevoli. Dimostrali.",
	"Teorema sul limite delle funzioni monotone.",
	"Teorema sul limite della funzione composta.",
	"Definizione di funzione infinitesima in un punto.",
	"Definizione di ordine di una funzione indinitesima.",
	"Teorema sulla non esistenza dei limiti seno/coseno.",
	"Teorema sul limite di una funzione limitata per una non limitata; con proposizione.",
	"Definizione di successione.",
	"Limiti per le successioni (definizione e proposizione).",
	"Limiti per le successioni oscillanti.",
	"Definizione di sottosuccessione estratta.",
	"Teorema sul limite di una sottosuccessione estratta.",
	"Teorema sulla continuità delle funzioni.",
	"Continuità globale delle funzioni in intervalli.",
	"Teorema di Weierstrass.",
	"Teorema degli zeri.",
	"Teorema dei valori intermedi.",
	"Teorema sulla continuità delle funzioni inverse da funzioni continue.",
	"Concetto di derivabilità",
	"Teorema sulla derivabilità delle funzioni. Dimostralo.",
	"Teorema sulla derivata del prodotto. Dimostralo.",
	"Derivate notevoli.",
	"Teorema sulla derivata della funzione inversa. Dimostralo.",
	"Teorema sulla derivata della composta.",
	"Teorema di Fermat. Dimostralo.",
	"Teorema di Rolle. Dimostralo.",
	"Teorema di Lagrange.",
	"Teorema di Cauchy.",
	"Criterio di monotonia.",
	"Caratterizzazione delle funzioni costanti.",
	"Criterio di caratterizzazione delle funzioni strettamente monotone.",
	"Teorema dell'Hôpital.",
	"Questioni legate alla derivata seconda.",
	"Corollario del teorema dell'Hôpital.",
	"Definizione di derivata seconda.",
	"Definizione di funzione concava/convessa.",
	"Definizione di punto di flesso.",
	"Simboli di Landau.",
	"Formula di Taylor. Dimostrala.",
	"Polinomio di Taylor.",
	"Corollario alla formula di Taylor.",
	"Asintoti.",
	"Integrazione di Riemann.",
	"Definizione di partizione.",
	"Somma integrale inf/sup di f.",
	"Teorema sulla Riemann-integrabilità delle funzioni continue.",
	"Teorema sulla Riemann-integrabilità delle funzioni monotone.",
	"Proprietà del Riemann-integrale.",
	"Teorema della media integrale per il Riemann-integrale.",
	"Definizione di funzione primitiva.",
	"Teorema fondamentale del calcolo integrale. Dimostralo.",
	"Teorema sulla caratterizzazione dell'insieme delle primitive di una funzione continua. Dimostralo.",
	"Teorema di Torricelli. Dimostralo.",
	"Integrali noti. Dimostrali.",
	"Integrali di II grado.",
	"Area della regione di piano compresa tra 2 funzioni.",
	"Formula di integrazione per parti.",
	"Fai una domanda e scelta e risponditi."
]

def pseudorandomQuestion():
	random.seed()
	i = random.randint(0, len(doms)-1)
	return doms[i]

print("Georally by corsaro. Licensed by MIT License.")
print("")
while True:
	print(pseudorandomQuestion())
	input("Premi invio per continuare...")
	print("")
