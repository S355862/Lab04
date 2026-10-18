class Espositore: 
    def __init__(self,codiceE,nome,cognome):
        self.__codiceE = codiceE
        self.__nome = nome
        self.__cognome = cognome
        self.__standAssociato = None

    @property
    def codiceE(self):
        return self.__codiceE

    @property
    def standAssociato(self):
        return self.__standAssociato

    @standAssociato.setter
    def standAssociato(self,valore): 
        self.__standAssociato = valore
    
    def __str__(self):
        if self.__standAssociato is None:
            return f"{self.__codiceE} - Nome : {self.__nome} Cognome : {self.__cognome} Stand: Nessuno stand associato"
        else:
            return f"{self.__codiceE} - Nome : {self.__nome} Cognome : {self.__cognome} Stand: {self.__standAssociato.codiceE}"