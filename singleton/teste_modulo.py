import modulo_singleton

print(f'O nome é {modulo_singleton.NOME}')
modulo_singleton.funcao1()


import modulo_singleton as meu_modulo
print(f'O nome é {meu_modulo.NOME}')
meu_modulo.funcao2()