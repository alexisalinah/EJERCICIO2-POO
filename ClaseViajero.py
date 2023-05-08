class viajero:
    __num_viajero = 00
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 00
    def __init__(self, numeroViaj, dni, nombre, apellido, millas_acum):
        self.__num_viajero = numeroViaj
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum
    def numero(self):
        return self.__num_viajero   
    def nombree(self):
        return self.__nombre
    def numero(self):
        return self.__num_viajero
    def cantidadTotalMillas(self):
        return self.__millas_acum
    def acumularmillas(self, nuevasmillas):
        self.__millas_acum+=nuevasmillas
        return self.__millas_acum
    def canjearMillas (self, millasAcanjear):
        if self.__millas_acum >= millasAcanjear:
            self.__millas_acum -= millasAcanjear
        else:
            print("Error, no tiene suficientes millas")
        return self.__millas_acum