
class Singleton:

    __instance = None

    def __init__(self) -> None:
        if not Singleton.__instance:
            print('Metodo __init__ foi chamado...')
        else:
            print(f'A instancia já foi criada: {self.get_instance()}')

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


# Chamando instâncias da classe:

s1 = Singleton() # A classe é inicializada, mas o objeto não é criado
print(f'Objeto criado agora: {Singleton.get_instance()}')
s2 = Singleton() # Instância já criada...