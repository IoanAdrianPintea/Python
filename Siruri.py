def inlocuire():
    sir = input()
    sirnou = ""
    for caracter in sir:
        if caracter in 'aeiou':
            sirnou += caracter.upper() #sirnou = sirnou + caracter.upper()
            print(caracter.upper())
        else:
            sirnou += caracter # sirnou = sirnou + caracter
            print(caracter)
    print(sirnou)


if __name__== "__main__":
    inlocuire()

