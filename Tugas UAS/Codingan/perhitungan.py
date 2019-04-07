from texttable import Texttable

def kalkulator():
    jawab = "y"

    while (jawab == "y"):

        print ("\n\t\nkalkulator")
        print ("1. Penjumlahan")
        print ("2. perkalian")
        print ("3. pengurangan")
        print ("4. pembagian")

        pilihan =input("\npilih perhitungan : ")

        if pilihan == '1':
            print("\n( penjumlahan ) ")
            jumlah1 =int(input("angka pertama : "))
            jumlah2 =int(input("angka kedua   : "))
            hitung = jumlah1 + jumlah2
            print ("\n" ,jumlah1,"+",jumlah2,"=",hitung,"\n")

        elif pilihan == '2':
            print("\n( perkalian ) ")
            jumlah1 =int(input("angka pertama : "))
            jumlah2 =int(input("angka kedua   : "))
            hitung = jumlah1 * jumlah2
            print ("\n" ,jumlah1,"x",jumlah2,"=",hitung,"\n")

        elif pilihan == '3':
            print("\n( pengurangan) ")
            jumlah1 =int(input("angka pertama : "))
            jumlah2 =int(input("angka kedua   : "))
            hitung = jumlah1 - jumlah2
            print ("\n" ,jumlah1,"-",jumlah2,"=",hitung,"\n")

        elif pilihan == '4':
            print("\n( pembagian ) ")
            jumlah1 =int(input("angka pertama : "))
            jumlah2 =int(input("angka kedua   : "))
            hitung = jumlah1 / jumlah2
            print ("\n" ,jumlah1,":",jumlah2,"=",hitung,"\n")

        else :
            print ("tidak ada perhitungan ")


        jawab =input("kembali ke perhitungan y/t : ")
            
        


        
        

        

        
                
                

    
