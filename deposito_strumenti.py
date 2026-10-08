class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore ):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = int(anno_acquisto)
        self.valore = float(valore)
    def __str__(self):
        return  f"[{self.codice}] {self.tipo} {self.marca} - {self.anno_acquisto} ({self.valore} euro)"
            
class Prestito:
    def __init__(self, codiceprestito, data, codicestrumento, cognomeprestito):
        self.codiceprestito = codiceprestito
        self.dataprestito = data
        self.codicestrumento = codicestrumento
        self.cognomeprestito = cognomeprestito
    def __str__(self):
        return f"Prestito {self.codiceprestito} - Strumento {self.codicestrumento} all'allievo {self.cognomeprestito} in data {self.dataprestito}"
        
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile
        self.listastrumenti = []
        self.listaprestiti = []

    def carica_file_strumenti(self, file_path):
        try:
            with open(file_path, "r") as fileinput:
                for riga in fileinput:
                    riga = riga.strip()
                    if not riga:
                        continue
                    campi = riga.split(",")
                    codice = campi[0]
                    tipo = campi[1]
                    marca = campi[2]
                    anno_acquisto = campi[3]
                    valore = campi[4]
                    nuovostrumento = Strumento(codice, tipo, marca, anno_acquisto, valore)
                    self.listastrumenti.append(nuovostrumento)
        except FileNotFoundError:
            raise  FileNotFoundError(f"File {file_path} not found")

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        if len(self.listastrumenti) == 0:
            nuovonumero = 1
        else:
            ultimostrumento = self.listastrumenti[-1]
            nuovonumero = int(ultimostrumento.codice[1:]) + 1
        nuovocodice = f"S{nuovonumero}"
        nuovostrumento = Strumento(nuovocodice, tipo, marca, anno_acquisto, valore)
        self.listastrumenti.append(nuovostrumento)
        return  nuovostrumento

    def strumenti_ordinati_per_marca(self):
        listaordinata = sorted(self.listastrumenti, key=lambda x: x.marca)
        return listaordinata

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        esiste = False
        for strumento in self.listastrumenti:
            if strumento.codice == id_strumento:
                esiste = True
        inprestito = False
        for prestito in self.listaprestiti:
            if prestito.codicestrumento == id_strumento:
                inprestito = True
        if esiste == False or inprestito == True:
            raise Exception(f"Prestito {id_strumento} inexistente")
        nuovonumeroprestito = len(self.listaprestiti) + 1
        nuovocodiceprestito = f"P{nuovonumeroprestito}"
        nuovoprestito = Prestito(nuovocodiceprestito, data, id_strumento, cognome_allievo)
        self.listaprestiti.append(nuovoprestito)
        return nuovoprestito

    def termina_prestito(self, id_prestito):
        dacancellare = None
        for prestito in self.listaprestiti:
            if prestito.codiceprestito == id_prestito:
                dacancellare = prestito
        if dacancellare == None:
            raise Exception("Errore: impossibile trovare questo codice prestito.")
        self.listaprestiti.remove(dacancellare)

