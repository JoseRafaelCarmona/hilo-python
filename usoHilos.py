import threading
import time

def imprimir():
    bandera = 1
    while bandera < 10:
        print(bandera)
        bandera +=1

def salida1():
    print("esto es la funcion del hilo 1")
    imprimir()

def salida2():
    print("esto es la funcion del hilo 2")
    imprimir()

if __name__=='__main__':
    hilo1 = threading.Thread(target=salida1)
    hilo1.start()
    time.sleep(10)
    hilo2 = threading.Thread(target=salida2)
    hilo2.start()