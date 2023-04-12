def is_palindrome(palabra : str) -> bool:
    palabra = palabra.replace(' ','').lower()
    return palabra == palabra[::-1]

def main():
    print(is_palindrome(1234))

if __name__ == '__main__':
    main()

# mypy .\palindromo_bien_hecho.py --check-untyped-defs