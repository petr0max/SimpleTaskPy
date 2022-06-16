def funcGenapGanjil():
    message = '''Halo, lagi cari bilangan genap dan ganjil ?
    \nyuk coba input disini: '''

    bilangan = int(input(message))

    while True:
        if (bilangan == 0):
            break
        elif (bilangan % 2 == 0):
            print(f"{bilangan} adalah bilangan genap.")
            break
        else:
            print(f"{bilangan} adalah bilangan ganjil.")
            break


funcGenapGanjil()
