import operator
from stand import Stand,StandPremium, StandPreseExtra
from espositore import Espositore
 
class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.elenco_stand = []
        self.elenco_espositori = []

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    
    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        try:
            with open(file_path,'r',encoding='utf-8') as f:
                for riga in f:
                    campi = riga.strip().split(',')
                    codice = campi[0]
                    if codice[0] == "S":
                        codice_stand = campi[0]
                        padiglione = int(campi[2])
                        metri_q = int(campi[1])
                        prezzo = int(campi[3])
                        if len(campi) == 4:
                            self.elenco_stand.append(Stand(codice_stand,metri_q,padiglione,prezzo))
                        elif len(campi) == 5:
                            if campi[4].isdigit():
                                prese_extra = int(campi[4])
                                prezzoPrese = prezzo * (1+0.07*prese_extra)
                                self.elenco_stand.append(StandPreseExtra(codice_stand,metri_q,padiglione,prezzoPrese,prese_extra))
                            else:
                                posizione = campi[4]
                                prezzoPremium = prezzo* 1.30
                                self.elenco_stand.append(StandPremium(codice_stand,metri_q,padiglione,prezzoPremium,posizione))

                    else:
                        codice_espositore = campi[0]
                        nome = campi[1]
                        cognome = campi[2]
                        self.elenco_espositori.append(Espositore(codice_espositore,nome,cognome))
        except FileNotFoundError:
            raise FileNotFoundError(f"file {file_path} non trovato")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        trovato_stand = None
        trovato_espositore = None
        for s in self.elenco_stand:
            if s.codice == codice_stand:
                trovato_stand = s
                break

        for e in self.elenco_espositori:
            if e.codice == codice_espositore:
                trovato_espositore = e
                break
        
        if trovato_stand is None:
            raise ValueError("Lo stand non esiste")
        if trovato_espositore is None:
            raise ValueError("L'espositore non esiste")

        if trovato_stand.espositoreAss is not None:
            raise ValueError("Lo stand è stato già assegnato")
        if trovato_espositore.standAssociato:
            raise ValueError("L'espositore è stato già assegnato")

        
    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositori in self.elenco_espositori:
            print(espositori)

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        lista_ordinata = sorted(self.elenco_stand, key = operator.attrgetter("prezzo"))
        return lista_ordinata
