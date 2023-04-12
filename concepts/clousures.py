def make_repeaer_on(n):
    def repeater(string):
        assert type(string) == str , 'Solo puedes insertar cadenas'
        return string * n
    return repeater

@make_repeaer_on
def hola():
    print('\nHola')


def mayuscula(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayuscula
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

"""Es equivaente a:

def sauludo(nombre):
    return f'{nombre}, recibiste un mensaje'
saludo = decorador(saludo)

saludo()
"""

def run():
    repeat_5 = make_repeaer_on(5)
    print(type(repeat_5))
    print(repeat_5('Hola'))
   # hola()

    print(mensaje('cesar'))

if __name__ == '__main__':
    run()