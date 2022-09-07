
class SanidadeCheck:

    __instances = None

    def __new__(cls, *args, **kwargs):
        if not SanidadeCheck.__instances:
            SanidadeCheck.__instances = super(SanidadeCheck, cls).__new__(cls,*args, **kwargs)
        return SanidadeCheck.__instances

    def __init__(self):
        self.__servidores = []

    def checar_servidor(self, srv):
        print(f'Checando o {self.__servidores[srv]}')

    def add_servidor(self):
        self.__servidores.append('Servidor 1')
        self.__servidores.append('Servidor 2')
        self.__servidores.append('Servidor 3')
        self.__servidores.append('Servidor 4')
    
    def mudar_servidor(self):
        self.__servidores.pop()
        self.__servidores.append('Servidor 5')


sv1 = SanidadeCheck()
sv2 = SanidadeCheck()

sv1.add_servidor()
print('Coronograma de checagem de sanidade dos servidores A...')

for srv in range(4):
    sv1.checar_servidor(srv)

sv2.mudar_servidor()
print('Coronograma de checagem de sanidade dos servidores B...')

for srv in range(4):
    sv2.checar_servidor(srv)