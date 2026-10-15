# Lab 03 - Soluzione

#### Argomenti

- Lettura da file (continuazione).
- Eccezioni (continuazione).
- Classi e oggetti (metodi dunder, metodi getter e setter, collezioni di oggetti).
- Ordinamento (di oggetti).

---

## Deposito di Strumenti Musicali

Progettare un sistema per gestire il prestito degli strumenti musicali di un deposito di strumenti (ad esempio
quello di una scuola di musica, messo a disposizione degli allievi in prestito). Il deposito è caratterizzato da
un nome e da un responsabile e gestisce un insieme di strumenti i cui dati sono memorizzati in un unico file CSV,
`strumenti.csv`, che possono essere dati in prestito.

Il file `strumenti.csv` contiene, riga per riga, le informazioni relative agli strumenti. Ogni riga corrisponde a
un singolo strumento definito da un codice univoco, il tipo (ad esempio Chitarra, Violino, Tromba), la marca,
l'anno di acquisto e il valore in euro. Un esempio del file è il seguente:

```file
S1,Chitarra,Yamaha,2019,250.00
S2,Violino,Stentor,2020,180.00
S3,Tromba,Bach,2018,600.00
S4,Pianoforte Digitale,Roland,2021,900.00
...
```

### Implementazione

Per questo laboratorio è necessario utilizzare la classe `DepositoStrumenti` presente nel file
`deposito_strumenti.py`. Le informazioni sugli strumenti devono essere modellate tramite una classe dedicata.
Il file `main.py` consente di interagire con il sistema tramite un menù testuale utilizzabile dalla console.

```menu in console
--- MENU DEPOSITO STRUMENTI ---
1. Modifica nome del responsabile del deposito
2. Carica strumenti da file
3. Aggiungi un nuovo strumento (da tastiera)
4. Visualizza strumenti ordinati per marca
5. Presta uno strumento
6. Termina prestito strumento
7. Esci
Scegli un'opzione >>
```

Le operazioni disponibili devono essere gestite dai metodi della classe `DepositoStrumenti`.
Per leggere e modificare il nome del responsabile, si possono utilizzare direttamente gli attributi della classe
oppure definire gli opportuni metodi getter/setter.

Per caricare i dati dal file CSV deve essere implementato, all'interno della classe `DepositoStrumenti`, il metodo
`carica_file_strumenti(file_path)`, che legge il file passato come parametro, crea gli oggetti corrispondenti e li
memorizza nel sistema. Se il file non viene trovato il metodo scatena l'eccezione `FileNotFoundError`.

Per aggiungere un nuovo strumento deve essere implementato, all'interno della classe `DepositoStrumenti`, il
metodo `aggiungi_strumento(tipo, marca, anno_acquisto, valore)`, che riceve come parametri il tipo dello
strumento, la marca, l'anno di acquisto e il valore. Il metodo crea e inserisce un nuovo oggetto strumento nel
sistema (assegnandogli automaticamente un codice univoco formato dalla lettera `S` seguita da un numero intero
progressivo, calcolato a partire dall'ultimo identificativo già presente nel sistema). Il metodo deve restituire
il riferimento allo strumento aggiunto.

La classe `DepositoStrumenti` deve inoltre includere il metodo `strumenti_ordinati_per_marca()`, che restituisce
un elenco degli strumenti presenti nel sistema ordinati alfabeticamente in base alla marca.

> **💡 SUGGERIMENTO:**  
> Per ordinare una lista è possibile utilizzare la funzione `sorted(lista, key=...)` oppure il metodo `lista.sort(key=...)`.
> Per specificare l'attributo da usare nell'ordinamento si può usare `attrgetter`, importandolo dal modulo 
> [`operator`](https://docs.python.org/3/library/operator.html):
>
> ```python
> from operator import attrgetter
> ```
>
> Una volta importato, `attrgetter("nome_attributo")` può essere usato come valore del parametro `key`, dove 
> "nome_attributo" indica l'attributo in base al quale ordinare gli oggetti della lista.

Per gestire i prestiti, la classe `DepositoStrumenti` deve implementare il metodo
`nuovo_prestito(data, id_strumento, cognome_allievo)`. Ogni prestito sarà caratterizzato da un codice univoco,
dalla data in cui è avvenuto, dal codice univoco dello strumento e dal cognome dell'allievo che sta effettuando il
prestito. Il codice univoco del prestito sarà definito con la lettera `P` seguita da un numero intero progressivo
a partire da 1, ad esempio `P1`, `P2`, `P3`, e così via. Il codice deve essere assegnato nel momento in cui il
prestito viene creato. Il metodo deve restituire un riferimento al prestito creato. Il metodo inoltre deve
verificare se lo strumento richiesto sia già in prestito oppure non sia presente nel sistema. Se una di queste
condizioni è vera, deve scatenare un'eccezione (ad esempio generica, `Exception`) per indicare l'errore.

Per terminare un prestito (ad esempio alla riconsegna dello strumento), la classe `DepositoStrumenti` include il
metodo `termina_prestito(id_prestito)`. Il metodo riceve come parametro il codice univoco del prestito ed ha il
compito di concludere il prestito, rimuovendo ogni riferimento dal sistema. Se il codice non corrisponde ad alcun
prestito esistente, il metodo deve scatenare un'eccezione (ad esempio generica, `Exception`) per indicare
l'errore.

> **💡 NOTA:**
> Tutte le classi richieste dall'esercizio (esclusa la classe `DepositoStrumenti`) devono implementare un metodo
> speciale di rappresentazione testuale, ovvero `__str__()` e/o `__repr__()`, in modo che l'oggetto
> risulti comprensibile quando viene stampato.
