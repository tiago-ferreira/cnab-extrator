class RegistroZ():

    def __init__(self, linha):
        self.__codigo_registro = linha[0:1]
        self.__total_registros_arquivo = linha[1:7]
        self.__valor_total_registros = linha[7:24]
        self.__reservado_para_futuro = linha[24:150]

    @property
    def codigo_registro(self):
        return self.__codigo_registro

    @codigo_registro.setter
    def codigo_registro(self, codigo_registro):
        self.__codigo_registro = codigo_registro

    @property
    def total_registros_arquivo (self):
        return self.__total_registros_arquivo 

    @total_registros_arquivo .setter
    def total_registros_arquivo (self, total_registros_arquivo ):
        self.__total_registros_arquivo  = total_registros_arquivo 

    @property
    def valor_total_registros (self):
        return self.__valor_total_registros 

    @valor_total_registros .setter
    def valor_total_registros (self, valor_total_registros ):
        self.__valor_total_registros  = valor_total_registros 

    @property
    def reservado_para_futuro(self):
        return self.__reservado_para_futuro

    @reservado_para_futuro.setter
    def reservado_para_futuro(self, reservado_para_futuro):
        self.__reservado_para_futuro = reservado_para_futuro


    def __str__(self):
        return self.__codigo_registro+self.__total_registros_arquivo + \
               self.__valor_total_registros +self.__reservado_para_futuro

    def __repr__(self):
        return f'codigo_registro= {self.__codigo_registro},  total_registros_arquivo = {self.__total_registros_arquivo }, ' \
               f'valor_total_registros = {self.__valor_total_registros }, reservado_para_futuro, {self.__reservado_para_futuro}, '