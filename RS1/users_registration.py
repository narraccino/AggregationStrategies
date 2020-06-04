
def registration(number):
    listaNomi= list()

    for i in range(0,number):
        nome= input("Utente: ")
        listaNomi.append(nome)

    print('[%s]' % ', '.join(map(str, listaNomi)))
    return listaNomi