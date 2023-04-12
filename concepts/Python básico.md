### Afirmaciones

```python
def primera_letra(lista_de_palabras):
primeras_letras = []

for palabra in lista_de_palabras:
    assert type(palabra) == str, f'{palabra} no es str'
    assert len(palabra) > 0, 'no se permiten srt vacios'
    
    primeras_letras.append(palabra[0].capitalize())
        
return primeras_letras
```

 

### Filter y Map

````python
#Filter recibe una funcion anonima y un iterable
options = list(filter(lambda x : x not in words_list, words_list))
options = [x for x in words_list if x not in new_list]
#Map
opc = list(map(lambda x : x*2, words_list))

#Reduce
import functools
# initializing list
lis = [1, 3, 5, 6, 2, ]
#lis = sorted(lis) Ordenamiento
#lis = lis.sort() Ordenamiento
# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b,lis))
 
#Django
filter(program__in=queryset)
filter(program__contains=queryset)
filter(program__icontains=queryset)
filter(program__gte=queryset)
````

### Raise

````python
def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se pueden ingresar cadenas vacías")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False
````



### Setters, Getters y Encapsulación

````python
class CasillaVotacion:
    def __init__(self, indentificador,pais):
        self._identificador = indentificador
        self._pais = pais
        self._region = None
    @property
    def region(self):
        return self._region
    @region.setter
    def region(self,reg):
        if reg in self._pais:
            self._region = reg
        else:
            raise ValueError(f'La region {reg} no es valida en {self._pais}')

casilla = CasillaVotacion(123,['Bogota','Medellin'])
print(casilla.region)
casilla.region = 'Bogota'
print(casilla.region)
````



### Polimorfismo

```python
class Terrestre:
    def desplazar(self):
        print('El animal anda')


class Acuatico:
    def desplazar(self):
        print('El animal nada')

class Cocodrilo(Terrestre, Acuatico):
    """Abstracción de cocodrilo. Herencia multiple.
    Como Terrestre se encuentra más a la izquierda,
    sería la definición de desplazar de esta clase la
    que prevalecería.
    """
    pass
```



### Matemáticas

*Representación de gráficas*

Un loop => crecimiento lineal.
Un loop dentro de otro => crecimiento cuadrático
Llamadas recursivas => crecimiento exponencial.

O(1) Constante
O(n) Lineal
O(log n) logaritmica
O(n log n) log lineal
O(n\*\*2) Polinomial
O2(2\*\*n) Exponencial

- [ ] Buscar programación dinámica



### Abrir archivo



|        | *Modos de Apertura*                                          |
| ------ | ------------------------------------------------------------ |
| **r**  | Solo lectura                                                 |
| **r**  | Lectura y escritura                                          |
| **w**  | Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe |
| **w+** | Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe |
| **a**  | Añadido (agregar contenido). Crea el archivo si éste no existe |
| **a+** | Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe. |

Existen varias extensiones de archivos con los que podemos interactuar con python (*js,csv,py,css,json,xml*)
Para abrir un archivo seguimos las siguiente estructura

``with open(ruta, modo_apertura) as nombre``

``with`` impide que se rompa


```python
def read():
    names = []
    with open("./archivos/name.txt", "r", encoding="utf-8") as f:
        for line in f: 
            if len(line.strip()) > 0:
                names.append(line.strip())
    if len(names)> 0:
        print(names)
    else:
        print("Archivo vacio")

def write():
    names = []
    with open("./archivos/name.txt", "w" , encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')

def agregar_nombre(nombre):
    with open("./archivos/name.txt", "a" , encoding="utf-8") as f:
        f.write(nombre)
        f.write("\n")

def borrar_nombre(nombre):
    names = []
    with open("./archivos/name.txt", "r", encoding="utf-8") as f:
        for line in f: 
            if len(line.strip()) > 0 and line.strip()!= nombre:
                names.append(line.strip())
    with open("./archivos/name.txt", "w" , encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')


def run():
    sw = True
    while sw:
        try:

            print("""  
----------------------------------------------------------------------

            Seleccione un numero:
            1. Crear un nuevo archivo 
            2. Agregar nombre
            3. Listar nombre
            4. Borrar nombre
            5. Salir del programa

----------------------------------------------------------------------

            """)
            n = int(input("Ingrese una opcion :   "))
            if n == 1:
                write()
            elif n == 2:
                nombre = input("Ingrese el nombre a agregar: ")
                agregar_nombre(nombre)
            elif n == 3:
                read()
            elif n == 4:
                nombre = input("Ingrese el nombre a borrar : ")
                borrar_nombre(nombre)
            elif n ==5:
                sw = False
                print("Programa Terminado!")
        except ValueError :
                print("Error seleccione una opcion correcta")
    # write()

if __name__ == '__main__':
    run()
```