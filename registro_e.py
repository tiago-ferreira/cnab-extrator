class RegistroE():

    def __init__(self, linha):
        self.__codigo_registro = linha[0:1]
        self.__identificacao_cliente_destinataria = linha[1:26]
        self.__agencia = linha[26:30]
        self.__identificacao_cliente_depositaria = linha[30:50]
        self.__data_vencimento = linha[50:58]
        self.__valor_debito = linha[58:73]
        self.__codigo_moeda = linha[73:75]
        self.__uso_instituicao_destinataria = linha[75:129]
        self.__tipo_identificacao = linha[129:130]
        self.__identificacao = linha[130:145]
        self.__tipo_operacao = linha[145:146]
        self.__opcao_cheque_especial = linha[146:147]
        self.__opcao_debito_parcial = linha[147:148]
        self.__reservado_para_futuro = linha[148:149]
        self.__codigo_movimento = linha[149:150]

    @property
    def codigo_registro(self):
        return self.__codigo_registro

    @codigo_registro.setter
    def codigo_registro(self, codigo_registro):
        self.__codigo_registro = codigo_registro

    @property
    def identificacao_cliente_destinataria(self):
        return self.__identificacao_cliente_destinataria

    @identificacao_cliente_destinataria.setter
    def identificacao_cliente_destinataria(self, identificacao_cliente_destinataria):
        self.__identificacao_cliente_destinataria = identificacao_cliente_destinataria

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
    def data_vencimento(self):
        return self.__data_vencimento

    @data_vencimento.setter
    def data_vencimento(self, data_vencimento):
        self.__data_vencimento = data_vencimento

    @property
    def valor_debito(self):
        return self.__valor_debito

    @valor_debito.setter
    def valor_debito(self, valor_debito):
        self.__valor_debito = valor_debito

    @property
    def codigo_moeda(self):
        return self.__codigo_moeda

    @codigo_moeda.setter
    def codigo_moeda(self, codigo_moeda):
        self.__codigo_moeda = codigo_moeda

    @property
    def uso_instituicao_destinataria(self):
        return self.__uso_instituicao_destinataria

    @uso_instituicao_destinataria.setter
    def uso_instituicao_destinataria(self, uso_instituicao_destinataria):
        self.__uso_instituicao_destinataria = uso_instituicao_destinataria

    @property
    def tipo_identificacao(self):
        return self.__tipo_identificacao

    @tipo_identificacao.setter
    def tipo_identificacao(self, tipo_identificacao):
        self.__tipo_identificacao = tipo_identificacao

    @property
    def identificacao (self):
        return self.__identificacao

    @identificacao .setter
    def identificacao (self, identificacao ):
        self.__identificacao  = identificacao

    @property
    def tipo_operacao(self):
        return self.__tipo_operacao

    @tipo_operacao.setter
    def tipo_operacao(self, tipo_operacao):
        self.__tipo_operacao = tipo_operacao

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
        return self.__codigo_registro+self.__identificacao_cliente_destinataria+  \
               self.__agencia+self.__identificacao_cliente_depositaria+ \
               self.__data_vencimento+self.__valor_debito+ \
               self.__codigo_moeda+self.__uso_instituicao_destinataria+ \
               self.__tipo_identificacao+self.__identificacao+ \
               self.__tipo_operacao+self.__opcao_cheque_especial+ \
               self.__opcao_debito_parcial+self.__reservado_para_futuro+ \
               self.__codigo_movimento

    def __repr__(self):
        return f'codigo_registro= {self.__codigo_registro}, identificacao_cliente_destinataria= {self.__identificacao_cliente_destinataria}, ' \
               f'agencia= {self.__agencia}, identificacao_cliente_depositaria= {self.__identificacao_cliente_depositaria}, ' \
               f'data_vencimento= {self.__data_vencimento}, valor_debito= {self.__valor_debito}, ' \
               f'codigo_moeda= {self.__codigo_moeda}, uso_instituicao_destinataria= {self.__uso_instituicao_destinataria}, ' \
               f'tipo_identificacao= {self.__tipo_identificacao}, identificacao, {self.__identificacao}, ' \
               f'tipo_operacao= {self.__tipo_operacao}, opcao_cheque_especial= {self.__opcao_cheque_especial}, ' \
               f'opcao_debito_parcial= {self.__opcao_debito_parcial}, reservado_para_futuro, {self.__reservado_para_futuro}, ' \
               f'codigo_movimento= {self.__codigo_movimento}'