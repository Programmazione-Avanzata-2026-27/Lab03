class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = int(anno_acquisto)
        self.valore = float(valore)

    # Il metodo __str__  definisce come l'oggetto viene mostrato come testo.
    # Senza questo, la funzione print() stamperebbe solo un incomprensibile indirizzo di memoria. #nascosto
    def __str__(self):
        return f"[{self.codice}] {self.tipo} {self.marca} ({self.anno_acquisto}) - €{self.valore}"


class Prestito:
    def __init__(self, codice, data, id_strumento, cognome_allievo):
        self.codice = codice
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f"Prestito {self.codice}: Strumento {self.id_strumento} assegnato a {self.cognome_allievo} il {self.data}"


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile
        # Uso i dizionari invece delle liste per l'accesso diretto ai dati tramite  chiave

        self.strumenti = {}
        self.prestiti = {}
        self.ultimo_id_prestito = 0

    def carica_file_strumenti(self, file_path):
        try:

            with open(file_path, "r", encoding="utf-8") as f:
                for linea in f:

                    dati = linea.strip().split(',')
                    if len(dati) == 5:
                        id, tipo_strumento, marca, anno_acquisto, valore = dati
                        self.strumenti[id] = Strumento(id, tipo_strumento, marca, anno_acquisto, valore)
        except FileNotFoundError:
            # Se il file non esiste, ho il crash e uso raise per evidenziare l'errore
            raise FileNotFoundError(f"File {file_path} non trovato.")

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        if not self.strumenti:
            nuovo_num = 1
        else:
            numeri = []
            for k in self.strumenti.keys():


                numeri.append(int(k[1:]))
            nuovo_num = max(numeri) + 1

        nuovo_id = "S" + str(nuovo_num)
        nuovo_strumento = Strumento(nuovo_id, tipo, marca, anno_acquisto, valore)
        self.strumenti[nuovo_id] = nuovo_strumento

        return nuovo_strumento

    def strumenti_ordinati_per_marca(self):

        #
        return sorted(self.strumenti.values(), key=lambda x: x.marca)

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        if id_strumento not in self.strumenti:

            raise Exception("Errore: strumento non presente nel sistema.")
        for p in self.prestiti.values():
            if p.id_strumento == id_strumento:
                raise Exception("Errore: strumento già in prestito.")

        self.ultimo_id_prestito += 1
        nuovo_id_prestito = "P" + str(self.ultimo_id_prestito)
        nuovo_prestito = Prestito(nuovo_id_prestito, data, id_strumento, cognome_allievo)
        self.prestiti[nuovo_id_prestito] = nuovo_prestito
        return nuovo_prestito

    def termina_prestito(self, id_prestito):
        if id_prestito not in self.prestiti:
            raise Exception("Errore: prestito inesistente.")

        # Il comando "del" rimuove fisicamente la coppia chiave-valore dal dizionario, cosi da gestire la fine del prestito
        del self.prestiti[id_prestito]