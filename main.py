from registro_a import RegistroA
from registro_d import RegistroD


if(__name__ == "__main__"):
    linha = 'AB2222222222222222222211111111111111111111333nome na depositaria 2020010100000188DEBITO AUTOMATICO                                                   1'
    registro = RegistroD(linha)

    print(repr(registro))
    print(linha)
    print(registro)