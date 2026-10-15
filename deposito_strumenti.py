from strumento import Strumento
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self._responsabile = responsabile
        self.strumenti = []
        self.prestiti = []
        self._prossimo_numero_prestito = 1

    @property
    def nome (self):
        return self._nome

    @nome.setter
    def nome (self, nome):
        self._nome = nome

    @property
    def responsabile (self):
        return self._responsabile

    @responsabile.setter
    def responsabile (self, responsabile):
        self._responsabile = responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file. Se il file non esiste, FileNotFoundError si propaga al chiamante."""
        with open(file_path, "r", encoding="utf-8") as f:
            righe = f.readlines()

        for riga in righe:
            riga = riga.strip()
            if riga == "":
                continue

            campi = riga.split(",")
            codice = campi[0].strip()
            tipo = campi[1].strip()
            marca = campi[2].strip()
            anno_acquisto = int(campi[3].strip())
            valore = float(campi[4].strip())

            strumento = Strumento(codice, tipo, marca, anno_acquisto, valore)
            self.strumenti.append(strumento)

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        if len(self.strumenti) == 0:
            nuovo_numero = 1
        else:
            ultimo_strumento = self.strumenti[-1]
            numero_ultimo_codice = int(ultimo_strumento.codice[1:])
            nuovo_numero = numero_ultimo_codice + 1

        nuovo_codice = f"S{nuovo_numero}"

        strumento = Strumento(nuovo_codice, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(strumento)

        return strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""

        # SOLUZIONE 1 ##################################################################
        lista_tuple = []  # inizializza lista di tuple (marca, tipo, oggetto_strumento)
        for s in self.strumenti:
            lista_tuple.append((s.marca, s.tipo, s))

        lista_tuple.sort()  # ordina per il primo elemento della tupla (marca) e se uguale, in base al secondo (tipo)

        lista_ordinata = [] # inizializzo la lista di strumenti ordinati
        for t in lista_tuple:
            lista_ordinata.append(t[2]) # prendo solo l'oggetto della tupla (alla posizione 2) e lo aggiungo alla lista
        return lista_ordinata

        # SOLUZIONE 2 (sfrutta il concetto di classe) ##################################
        # NB: bisogna importare attrgetter con "from operator import attrgetter"
        #
        # return sorted(self.strumenti, key=attrgetter("marca"))

        # SOLUZIONE 3 (lambda function) ################################################
        return sorted(self.strumenti, key=lambda strumento: strumento.marca)

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        strumento_trovato = None
        for strumento in self.strumenti:
            if strumento.codice == id_strumento:
                strumento_trovato = strumento

        if strumento_trovato is None:
            raise Exception(f"Lo strumento {id_strumento} non è presente nel sistema.")

        for prestito in self.prestiti:
            if prestito.id_strumento == id_strumento:
                raise Exception(f"Lo strumento {id_strumento} è già in prestito.")

        nuovo_codice = f"P{self._prossimo_numero_prestito}"
        self._prossimo_numero_prestito = self._prossimo_numero_prestito + 1

        prestito = Prestito(nuovo_codice, data, id_strumento, cognome_allievo)
        self.prestiti.append(prestito)

        return prestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        prestito_trovato = None
        for prestito in self.prestiti:
            if prestito.codice == id_prestito:
                prestito_trovato = prestito

        if prestito_trovato is None:
            raise Exception(f"Il prestito {id_prestito} non esiste.")

        self.prestiti.remove(prestito_trovato)
