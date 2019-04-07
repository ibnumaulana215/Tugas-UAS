from Codingan.gaji import Gajih
from Codingan.nilai import Nilai
from Codingan.PEMBAYARAN import pembayaran
from Codingan.perhitungan import kalkulator
import getpass


def Login ():
    print ("\n\tLogin Akun ")
    user = input("Username: ")
    Password = getpass.getpass ("Password: ")
    if user == 'ibnu' and Password == '12345':
         pilihan ()
    else:
         print ("\n Password yang anda masukan Salah")
         Login ()

def pilihan () :
    print("----PILIH MENU----")
    print("\n\t----pilihan----\n\t1. Gajih\n\t2. Nilai\n\t3. Pembayaran\n\t4. kalkulator")

    pilih = input("\n\tsilahkan pilih : ")
    if pilih == "1" :
        Gajih ()
        lagi ()
    elif pilih == "2" :
        Nilai ()
        lagi ()
    elif pilih == "3" :
        pembayaran ()
        lagi ()
    elif pilih == "4" :
        kalkulator ()
        lagi ()
    else :
        exit
        print ("\n\t-----terima kasih----")

def lagi ():
    tanya = input("\nkembali ke menu pilihan (y/t)? ")
    if tanya == "y":
        pilihan ()
    else :
        print ("\n\t-----terima kasih----")
        input("")
        exit

        
Login()
     

