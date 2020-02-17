import random

class Objeto:
    def __init__(self):
        pass

    def getString(self):
        pass

class ObjetoReal(Objeto):

    def getString(self):
        return "Imprimiendo una cadena"

class Proxy(Objeto):
    def __init__(self):
        self.__obj = ObjetoReal()

    def getString(self):
        return self.__obj.getString()

class OtroObjeto:
    def __init__(self):
        pass

    def doSomething(self):
        return "Imprimiendo una cadena"

class Adapter(Objeto):
    def __init__(self):
        self.__obj = OtroObjeto()

    def getString(self):
        return self.__obj.doSomething()

def main():
    proxy = Proxy()
    adtar = Adapter()
    obto = Objeto()
    if random.randint(0,3) <= 1:
        obto = proxy
    else:
        obto = adtar
    print(obj.getString(), "desde", type(obto))
    pass

if __name__ == '__main__':
    main()
