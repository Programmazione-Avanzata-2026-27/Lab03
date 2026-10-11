#Due librerie (aggiunte) sono state importate nel main

class Strumenti:
    def __init__(self,codice, tipo, marca, anno, prezzo):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno = int(anno)
        self.prezzo = float(prezzo)


class DepositoStrumenti:
    #Variabile di classe per l'incremento dei codici prestito
    numero_prestito = 0

    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile
        #Così con self è accessibile a tutte la altre funzioni definite nella classe
        self.lista_strumenti = []
        #Dentro questo dizionario verranno associati i prestiti all'id dello strumento
        self.diz_prestiti = {}



    def carica_file_strumenti(self, file_path):
       try:
           with open(file_path, "r", encoding= "utf-8") as file:
               riga = csv.reader(file)

               for r in riga:
                   strumento = Strumenti(r[0], r[1], r[2], r[3], r[4])
                   self.lista_strumenti.append(strumento)


       except FileNotFoundError:
           raise FileNotFoundError("Errore: Il file degli strumenti non è stato trovato.")




    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        n = (len(self.lista_strumenti)) + 1
        codice = f"S{n}"

        strumento = Strumenti(codice,tipo, marca, anno_acquisto, valore)
        self.lista_strumenti.append(strumento)
        return strumento


    def strumenti_ordinati_per_marca(self):
        lista_strumenti_ordinata = sorted(self.lista_strumenti, key=attrgetter("marca"))
        return lista_strumenti_ordinata

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        if id_strumento in self.diz_prestiti:
            raise Exception(f"Lo strumento associato all'id {id_strumento} attualmente è già in prestito.")
        else:
            #Utilizzo controllo ed il suo valore 0/1 per verificare se lo strumento è registrato nel deposito
            controllo = 0
            for r in self.lista_strumenti:
                if r.codice == id_strumento:
                    controllo = 1

            if controllo == 0:
                raise Exception(f"Lo strumento richiesto non è registrato nel deposito.")

            #Incremento la variabile utilizzata per il codice progressivo del prestito prima di crearlo
            self.numero_prestito = self.numero_prestito + 1
            self.diz_prestiti[id_strumento] = [f"P{self.numero_prestito}",data,cognome_allievo]
            return self.diz_prestiti[id_strumento]

    def termina_prestito(self, id_prestito):
        chiave = None

        for r in self.diz_prestiti:
            if self.diz_prestiti[r][0] == id_prestito:
                #Salvo la chiave associata al prestito da eliminare. Non lo elimino immediatamente perchè interferirebbe con il ciclo for
                chiave = r

        if chiave == None:
            raise Exception("Nessun prestito associato al codice.")
        else:
            del self.diz_prestiti[chiave]

