
class Singleton(object):

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f'Criando o objeto {cls.instance}')
        return cls.instance

# Chamando instâncias da classe:
s1 = Singleton()
s2 = Singleton()

# id -> indentificador do objeto na memória
print(f'Instancia 1: {id(s1)}')
print(f'Instancia 2: {id(s2)}')