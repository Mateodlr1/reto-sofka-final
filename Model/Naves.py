class Naves:
    def __init__(self, tipo, combustible, medidas): #defino el metodo init y recibo los parametros
        self._tipo = tipo                       #inicializo los atributos
        self._combustible = combustible
        self._medidas = medidas

    @property #uso el decorador property para recuperar el atributo  de _tipo encapsulandolo
    def tipo(self):
        return self._tipo

    @tipo.setter # encapsulo con el setter para poder modificar el valor
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def combustible(self):
        return self._combustible

    @combustible.setter
    def combustible(self, combustible):
        self._combustible = combustible

    @property
    def medidas(self):
        return self._medidas

    @medidas.setter
    def medidas(self, medidas):
         self._medidas = medidas