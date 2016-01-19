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
	"Definisci una matrice trasposta generica.",
	"Verifica le proprietà delle operazioni tra matrici.",
	"Determina le proprietà del calcolo del determinante di una matrice.",
	"Definisci il teorema della matrice inversa.",
	"Definisci il rango di una matrice.",
	"Definisci il teorema di Kronecher.",
	"Definisci il teorema di Rouché-Capelli.",
	"Come risolvi un sistema con indici m diverso da n?",
	"Definisci il sistema omogeneo.",
	"Definisci l'algoritmo di Gauss per risolvere una matrice a scala.",
	"Come fai a determinare la distanza minima tra due rette sghembe? E la retta di minima distanza?",
	"Definisci la superficie nello spazio.",
	"Definisci la sfera.",
	"Definisci la curva.",
	"Definisci il cilindro.",
	"Definisci il cono.",
	"Come calcoli la superficie di rotazione?",
	"Definisci il vettore.",
	"Quando due vettori sono equipollenti?",
	"Cosa individua ogni punto generico del piano?",
	"Come si calcolano le coordinate del punto medio di due segmenti?",
	"Quando due vettori sono paralleli?",
	"Definisci la somma tra due vettori.",
	"Definisci il prodotto scalare di un vettore per uno scalare.",
	"Qual è la condizione di complanarità di 3 vettori nello spazio?",
	"Definisci il prodotto scalare tra due vettori, enumera e dimostra le proprietà",
	"Definisci l'ortogonalità tra due vettori.",
	"Definisci la norma di un vettore. A cosa equivale geometricamente?",
	"Definisci la normalizzazione di un vettore.",
	"Definisci l'angolo tra due vettori.",
	"Qual è la seconda definizione di prodotto scalare? Dimostra che le due definizione di prodotto scalare coincidono.",
	"Quando una terna di vettori si dice positivamente orientata?",
	"Cos'è la combinazione lineare di vettori?",
	"Quando i vettori si dicono linearmente indipendenti?",
	"Quando i vettori si dicono linearmente dipendenti?",
	"Se i vettori fossero linearmente dipendenti, quale sarebbe la combinazione lineare di uno di essi?",
	"Qual'è il significato geometrico della lineare dipendenza tra vettori?",
	"Definisci cos'è uno spazio vettoriale, enumera e dimostra le sue proprietà",
	"Definisci il sottospazio vettoriale.",
	"Cosa rappresentano tutte le rette passanti per l'origine rispetto a R^2?",
	"Definisci il generatore di un sottospazio vettoriale.",
	"Quando i vettori generano un vettore?",
	"Definisci la dimensione di un sottospazio vettoriale.",
	"Dimostra che, data una base di V, la rappresentazione di un vettore di V rispetto la base data è unica.",
	"Cosa sono le componenti di un vettore rispetto ad una base?",
	"Varia il numero di elementi che compongono le basi di uno spazio vettoriale?",
	"Dimostra che i versori i e j sono base di R^2 e determina la dimensione di R^2.",
	"Dimostra che dimV corrisponde al numero massimo di vettori linearmente indipendenti.",
	"Dimostra che dimV è il minimo numero di vettori che possono generare tutto V.",
	"Qual è il minimo numero di vettori che può generare tutto V?",
	"Che relazione c'è tra il determinante di una matrice e la verifica di linearità tra vettori?",
	"Che relazione c'è tra la dimensione di un sottospazio di V e la dimensione dello spazio V?",
	"Definisci l'applicazione lineare.",
	"Dimostra che, in ogni applicazione lineare, f(0_v) = 0_w",
	"Definisci il nucleo di un'applicazione lineare.",
	"Definisci l'immagine di un'applicazione lineare.",
	"Che relazione c'è tra la dimensione di V e le dimensioni del suo nucleo e del suo insieme immagine?",
	"Dimostra che ker e Im sono sottospazi vettoriali rispettivamente di V e W.",
	"Dimostra che lo zero è unico se f è una applicazione lineare ingettiva. Dimostrala anche inversamente.",
	"Un'applicazione lineare trasforma basi in basi? Verificalo.",
	"Un'applicazione lineare trasforma generatori in generatori? Verificalo.",
	"Da ogni sistema di generatori si può estrarre una base?",
	"Come si verifica che un'applicazione è lineare?",
	"Dimostra che la base di V dà un sistema di generatori dell'immagine di f.",
	"Dimostra che, data una base di V, la base di v dà una base dell'immagine di f se e solo se f è ingettiva.",
	"Definisci la matrice associata all'applicazione lineare rispetto ad una base.",
	"Cos'è un endomorfismo?",
	"Che relazione c'è tra le basi e un endomorfismo?",
	"Perché è importante la matrice associata ad una applicazione lineare? Cosa ti permette di fare?",
	"Definisci il cambiamento di base.",
	"Cos'è la matrice di passaggio?",
	"Che relazione c'è tra componenti di un vettore, la matrice di passaggio e le componenti dell'immagine di un vettore?",
	"Definisci le matrici simili.",
	"In caso di un endomorfismo, che relazione c'è tra la matrice associata rispetto ad una base e la matrice associata rispetto ad un'altra base?",
	"Dato un endomorfismo identico, qual è la matrice associata a quell'applicazione lineare rispetto una base?",
	"Definisci autovettore di un endomorfismo.",
	"Definisci l'autovalore.",
	"Definisci l'autospazio associato ad un autovalore.",
	"Che legame persiste tra un endomorfismo e un autovettore di una matrice associata all'endomorfismo?",
	"Definisci il polinomio caratteristico.",
	"Definisci l'equazione caratteristica.",
	"Che relazione persiste tra matrici associate allo stesso endomorfismo rispetto a 2 differenti basi?",
	"Come si determina l'autospazio associato ad un autovalore?",
	"Cosa puoi dedurre per gli autovettori se hai un endomorfismo e gli autovalori sono distinti?",
	"Che relazione c'è tra la dimensione di un autospazio e la molteplicità algebrica di uno stesso autovalore?",
	"A cosa corrisponde la molteplicità algebrica? E la molteplicità geometrica?",
	"Quando una matrice è diagonalizzabile?",
	"Definisci la diagonalizzazione di una matrice.",
	"È diagonalizzabile una matrice che non ha autovalori reali?",
	"Cos'è ogni retta passante per l'origine in termini analitici?",
	"Quali sono le possibili forme delle equazioni della retta?",
	"Cos'è la giacitura di una retta?",
	"Quali sono le possibili equazioni generiche di un fascio di piani?",
	"Cos'è una conica? E una quadratica?",
	"Dimostra che due matrici simili hanno lo stesso determinante.",
	"Dimostra che l'autospazio è un sottospazio vettoriale di V.",
	"Dimostra che due matrici simili hanno lo stesso polinomio caratteristico.",
	"Dimostra che l'autovalore è soluzione del polinomio caratteristico.",
	"Dimostra che due autospazi generati da due autovalori distinti sono separati dallo zero.",
	"Qual è il significato geometrico del vettore norma relativo ad un piano?",
	"Definisci e dimostra la condizione di parallelismo e di perpendicolarità tra due piani.",
	"Definisci e dimostra la condizione di parallelismo tra una retta ed un piano.",
	"Definisci e dimostra la condizione di perpendicolarità tra piano e retta.",
	"Definisci e dimostra il calcolo dell'angolo tra due piani.",
	"Definisci e dimostra il calcolo dell'angolo tra un piano ed una retta."
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
