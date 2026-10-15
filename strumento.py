class Strumento:
    """Rappresenta uno strumento musicale del deposito"""

    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        return (f"{self.codice}: {self.tipo} {self.marca} (acquistato nel {self.anno_acquisto}) "
                f"- valore {self.valore} euro")

    def __repr__(self):
        return (f"{self.codice}: {self.tipo} {self.marca} (acquistato nel {self.anno_acquisto}) "
                f"- valore {self.valore} euro")