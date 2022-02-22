from registro_a import RegistroA
from registro_d import RegistroD
from registro_e import RegistroE
from registro_z import RegistroZ


if(__name__ == "__main__"):
    linha = 'AB2222222222222222222211111111111111111111333nome na depositaria 2020010100000188DEBITO AUTOMATICO                                                   1'
    registro = RegistroZ(linha)

    print(repr(registro))
    print(linha)
    print(registro)