'''
GEORALLY - LICENSED UNDER THE MIT LICENSE

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
	"Dimostra che, data una base di V, la rappresentazione di un vettore di V rispetto la base data è unica.",
	"Dimostra che i versori i e j sono base di R^2 e determina la dimensione di R^2.",
	"Dimostra che dimV è il minimo numero di vettori che possono generare tutto V.",
	"Dimostra che dimV corrisponde al numero massimo di vettori linearmente indipendenti.",
	"Dimostra che, in ogni applicazione lineare, f(0_v) = 0_w",
	"Dimostra che ker e Im sono sottospazi vettoriali rispettivamente di V e W.",
	"Dimostra che lo zero è unico se f è una applicazione lineare ingettiva. Dimostrala anche all'inverso.",
	"Dimostra che la base di V dà un sistema di generatori dell'immagine di f.",
	"Dimostra che, data una base di V, la base di v dà una base dell'immagine di f se e solo se f è ingettiva.",
	"Dimostra che due matrici simili hanno lo stesso determinante.",
	"Dimostra che l'autospazio è un sottospazio vettoriale di V.",
	"Dimostra che due matrici simili hanno lo stesso polinomio caratteristico.",
	"Dimostra che l'autovalore è soluzione del polinomio caratteristico.",
	"Dimostra che due autospazi generati da due autovalori distinti sono separati dallo zero.",
	"Definisci e dimostra la condizione di parallelismo e di perpendicolarità tra due piani.",
	"Definisci e dimostra la condizione di parallelismo tra una retta ed un piano.",
	"Definisci e dimostra la condizione di perpendicolarità tra piano e retta.",
	"Definisci e dimostra il calcolo dell'angolo tra due piani.",
	"Definisci e dimostra il calcolo dell'angolo tra un piano ed una retta.",
	"Determina e dimostra il legame che persiste tra l'autovettore di un endomorfismo e l'autovettore di una matrice. (AX=λX)"
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
