class RegistroD():

    def __init__(self, linha):
        self.__codigo_registro = linha[0:1]
        self.__identificacao_cliente_destinataria_atual = linha[1:26]
        self.__agencia = linha[26:30]
        self.__identificacao_cliente_depositaria = linha[30:50]
        self.__identificacao_cliente_destinataria_nova = linha[50:75]
        self.__ocorrencia = linha[75:130]
        self.__nova_data_vencimento = linha[130:138]
        self.__opcao_cheque_especial = linha[138:139]
        self.__opcao_debito_parcial = linha[139:140]
        self.__reservado_para_futuro = linha[140:149]
        self.__codigo_movimento = linha[149:150]

    @property
    def codigo_registro(self):
        return self.__codigo_registro

    @codigo_registro.setter
    def codigo_registro(self, codigo_registro):
        self.__codigo_registro = codigo_registro

    @property
    def identificacao_cliente_destinataria_atual(self):
        return self.__identificacao_cliente_destinataria_atual

    @identificacao_cliente_destinataria_atual.setter
    def identificacao_cliente_destinataria_atual(self, identificacao_cliente_destinataria_atual):
        self.__identificacao_cliente_destinataria_atual = identificacao_cliente_destinataria_atual

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def identificacao_cliente_depositaria(self):
        return self.__identificacao_cliente_depositaria

    @identificacao_cliente_depositaria.setter
    def identificacao_cliente_depositaria(self, identificacao_cliente_depositaria):
        self.__identificacao_cliente_depositaria = identificacao_cliente_depositaria

    @property
    def identificacao_cliente_destinataria_nova(self):
        return self.__identificacao_cliente_destinataria_nova

    @identificacao_cliente_destinataria_nova.setter
    def identificacao_cliente_destinataria_nova(self, identificacao_cliente_destinataria_nova):
        self.__identificacao_cliente_destinataria_nova = identificacao_cliente_destinataria_nova

    @property
    def ocorrencia(self):
        return self.__ocorrencia

    @ocorrencia.setter
    def ocorrencia(self, ocorrencia):
        self.__ocorrencia = ocorrencia

    @property
    def nova_data_vencimento(self):
        return self.__nova_data_vencimento

    @nova_data_vencimento.setter
    def nova_data_vencimento(self, nova_data_vencimento):
        self.__nova_data_vencimento = nova_data_vencimento

    @property
    def opcao_cheque_especial(self):
        return self.__opcao_cheque_especial

    @opcao_cheque_especial.setter
    def opcao_cheque_especial(self, opcao_cheque_especial):
        self.__opcao_cheque_especial = opcao_cheque_especial

    @property
    def opcao_debito_parcial(self):
        return self.__opcao_debito_parcial

    @opcao_debito_parcial.setter
    def opcao_debito_parcial(self, opcao_debito_parcial):
        self.__opcao_debito_parcial = opcao_debito_parcial

    @property
    def reservado_para_futuro(self):
        return self.__reservado_para_futuro

    @reservado_para_futuro.setter
    def reservado_para_futuro(self, reservado_para_futuro):
        self.__reservado_para_futuro = reservado_para_futuro

    @property
    def codigo_movimento(self):
        return self.__codigo_movimento

    @codigo_movimento.setter
    def codigo_movimento(self, codigo_movimento):
        self.__codigo_movimento = codigo_movimento

    def __str__(self):
        return self.__codigo_registro+self.__identificacao_cliente_destinataria_atual+  \
               self.__agencia+self.__identificacao_cliente_depositaria+ \
               self.__identificacao_cliente_destinataria_nova+self.__ocorrencia+ \
               self.__nova_data_vencimento+self.__opcao_cheque_especial+ \
               self.__opcao_debito_parcial+self.__reservado_para_futuro+ \
               self.__codigo_movimento

    def __repr__(self):
        return f'codigo_registro= {self.__codigo_registro}, identificacao_cliente_destinataria_atual= {self.__identificacao_cliente_destinataria_atual}, ' \
               f'agencia= {self.__agencia}, identificacao_cliente_depositaria= {self.__identificacao_cliente_depositaria}, ' \
               f'identificacao_cliente_destinataria_nova= {self.__identificacao_cliente_destinataria_nova}, ocorrencia= {self.__ocorrencia}, ' \
               f'nova_data_vencimento= {self.__nova_data_vencimento}, opcao_cheque_especial= {self.__opcao_cheque_especial}, ' \
               f'opcao_debito_parcial= {self.__opcao_debito_parcial}, reservado_para_futuro, {self.__reservado_para_futuro}, ' \
               f'codigo_movimento= {self.__codigo_movimento}'