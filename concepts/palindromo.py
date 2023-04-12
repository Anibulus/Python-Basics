def palindromo(palabra):
    palabra = palabra.replace(' ','').lower()
    return palabra == palabra[::-1]

def main():
    pass       
#punto de entrada en un programa de python
if __name__ == '__main__':
    main()