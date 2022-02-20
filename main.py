from registro_a import RegistroA


if(__name__ == "__main__"):
    linha = 'AB2222222222222222222211111111111111111111333nome na depositaria 2020010100000188DEBITO AUTOMATICO                                                    '
    registro = RegistroA(linha)
    print(len(registro.reservado_para_futuro))
    print(registro)