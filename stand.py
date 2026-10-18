class Stand:
    def __init__(self, codice, metri_q, padiglione, prezzo):
        self.__codice = codice
        self.__metri_q = metri_q
        self.__padiglione = padiglione
        self.__prezzo = prezzo
        self.__espositoreAss = None

    def __str__(self):
        return f"{self.__codice}: Standard | {self.__metri_q} mq - Padiglione {self.__padiglione} - Prezzo: {self.__prezzo:.2f} €"
   
    @property 
    def codice(self):
        return self.__codice

    @property
    def metri_q(self):
        return self.__metri_q

    @property
    def padiglione(self):
        return self.__padiglione
    
    @property
    def prezzo(self):
        return self.__prezzo

    @prezzo.setter
    def prezzo(self,prezzo):
        self.__prezzo = prezzo
    
    @property
    def espositoreAss(self):
        return self.__espositoreAss

    @espositoreAss.setter
    def espositore(self,espositoreAss):
        self.__espositoreAss = espositoreAss


class StandPremium(Stand):
    def __init__(self, codice, metri_q, padiglione, prezzo, posizione):
        super().__init__(codice, metri_q, padiglione, prezzo)   
        self.__posizione = posizione

    def __str__(self):
        return f"{self.codice}: : Premium | {self.metri_q} mq - Padiglione {self.padiglione} - Prezzo: {self.prezzo:.2f} € - Posizione: {self.__posizione}"


class StandPreseExtra(Stand):
    def __init__(self, codice, metri_q, padiglione, prezzo, prese_extra):
        super().__init__(codice, metri_q, padiglione, prezzo)   
        self.__prese_extra = prese_extra  

    def __str__(self):
        return f"{self.codice}: Prese Aggiuntive | {self.metri_q} mq - Padiglione {self.padiglione} - Prezzo: {self.prezzo:.2f} € - Prese aggiuntive: {self.__prese_extra}" 