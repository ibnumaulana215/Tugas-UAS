from texttable import Texttable

def pembayaran () :

    jawab = "y"

    while (jawab == "y"):

        print ("\t------PEMBAYARAN-------")
        table = Texttable (max_width = 700)
        nama = input("input Nama  :")
        nim = input("input Nim   :")
        kelas = input("input Kelas :")
        jawab = "t"
        

        #---Bayar UAS & UTS------------
        
        Bayar_UAS =input("\n\tbayar UAS y/t : ")
        if Bayar_UAS =='y':
            uang_UAS = 500000

        else :
            uang_UAS = 0

        Bayar_UTS =input("\n\tbayar UTS y/t : ")
        if Bayar_UTS =='y':
            uang_UTS = 500000

        else :
            uang_UTS = 0

        #---Bayar Bulanan -----
            
        Bayar_Bulanan =input("\n\tbayar bulanan y/t : ")
        if Bayar_Bulanan =='y':
            Berapa_Bulan =int(input("\tBulanan : berapa Bulan : "))
            uang_Bulanan = 500000*Berapa_Bulan

        else :
            uang_Bulanan = 0

        #---Bayar Seminar---

        Bayar_seminar =input("\n\tbayar Seminar y/t : ")
        if Bayar_seminar =='y':
            Berapa_seminar =int(input("\tBerapa Kali Seminar : "))
            uang_seminar = 100000*Berapa_seminar

        else :
            uang_seminar = 0

        #----Bayar Kas---
            
        Bayar_Kas =input("\n\tbayar kas y/t : ")
        if Bayar_Kas =='y':
            Berapa_Kas =int(input("\tBerapa Bulan KAS : "))
            uang_Kas = 20000*Berapa_Kas
        else :
            uang_Kas = 0

        #---Uang Admin---
        print("\tBayar Admin : ")
        uang_Admin = 5000

        Semua_Total = uang_UAS + uang_UTS + uang_Bulanan + uang_seminar + uang_Kas + uang_Admin
        
        #----------------
        table.set_cols_dtype(['i','i','i','i','i','i','i','i','i','i'])
        table.add_rows([['NAMA','NIM','KELAS','UAS','UTS','BULANAN','SEMINAR','KAS','ADMIN','TOTAL'],
                        [nama,nim,kelas,uang_UAS,uang_UTS,uang_Bulanan,uang_seminar,uang_Kas,uang_Admin,Semua_Total]])

        print(table.draw())

        jawab =input("\n\t Bayar Lain Lagi y/t : ")



    
        


        
            


        
        
        
        
