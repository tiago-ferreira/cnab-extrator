class RegistroA():

    def __init__(self, linha):
        self.__codigo_registro = linha[0:1]
        self.__codigo_remessa = linha[1:2]
        self.__codigo_convenio = linha[2:22]
        self.__nome_destinataria = linha[22:42]
        self.__codigo_depositaria = linha[42:45]
        self.__nome_depositaria = linha[45:65]
        self.__data_geracao = linha[65:73]
        self.__numero_sequencial_arquivo = linha[73:79]
        self.__versao_layout = linha[79:81]
        self.__identificao_servico = linha[81:98]
        self.__reservado_para_futuro = linha[98:150]

    @property
    def codigo_registro(self):
        return self.__codigo_registro

    @codigo_registro.setter
    def codigo_registro(self, codigo_registro):
        self.__codigo_registro = codigo_registro

    @property
    def codigo_remessa(self):
        return self.__codigo_remessa

    @codigo_remessa.setter
    def codigo_remessa(self, codigo_remessa):
        self.__codigo_remessa = codigo_remessa

    @property
    def codigo_convenio(self):
        return self.__codigo_convenio

    @codigo_convenio.setter
    def codigo_convenio(self, codigo_convenio):
        self.__codigo_convenio = codigo_convenio

    @property
    def nome_destinataria(self):
        return self.__nome_destinataria

    @nome_destinataria.setter
    def nome_destinataria(self, nome_destinataria):
        self.__nome_destinataria = nome_destinataria

    @property
    def codigo_depositaria(self):
        return self.__codigo_depositaria

    @codigo_depositaria.setter
    def codigo_depositaria(self, codigo_depositaria):
        self.__codigo_depositaria = codigo_depositaria

    @property
    def nome_depositaria(self):
        return self.__nome_depositaria

    @nome_depositaria.setter
    def nome_depositaria(self, nome_depositaria):
        self.__nome_depositaria = nome_depositaria

    @property
    def data_geracao(self):
        return self.__data_geracao

    @data_geracao.setter
    def data_geracao(self, data_geracao):
        self.__data_geracao = data_geracao

    @property
    def numero_sequencial_arquivo(self):
        return self.__numero_sequencial_arquivo

    @numero_sequencial_arquivo.setter
    def numero_sequencial_arquivo(self, numero_sequencial_arquivo):
        self.__numero_sequencial_arquivo = numero_sequencial_arquivo

    @property
    def versao_layout(self):
        return self.__versao_layout

    @versao_layout.setter
    def versao_layout(self, versao_layout):
        self.__versao_layout = versao_layout

    @property
    def identificacao_servico(self):
        return self.__identificao_servico

    @identificacao_servico.setter
    def identificacao_servico(self, identificacao_servico):
        self.__identificao_servico = identificacao_servico

    @property
    def reservado_para_futuro(self):
        return self.__reservado_para_futuro

    @reservado_para_futuro.setter
    def reservado_para_futuro(self, reservado_para_futuro):
        self.__reservado_para_futuro = reservado_para_futuro

    def __str__(self):
        return f'{self.__codigo_registro} - {self.__codigo_remessa} - ' \
               f'{self.__codigo_convenio} - {self.__nome_destinataria} - ' \
               f'{self.__codigo_depositaria} - {self.__nome_depositaria} - ' \
               f'{self.__data_geracao} - {self.__numero_sequencial_arquivo} - ' \
               f'{self.__versao_layout} - {self.__identificao_servico} - ' \
               f'{self.__reservado_para_futuro}'
