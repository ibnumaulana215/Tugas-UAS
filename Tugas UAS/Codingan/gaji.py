def Gajih():
    from texttable import Texttable
    table = Texttable ()
    jawab = "y"
    no = 0
    nama = []
    jabatan = []
    gaji = []
    while (jawab == "y"):
        nama.append(input("\n Masukan Nama :"))
        jab = input("jabatan :")
        jabatan.append(jab)                                                                                 

        if (jab == 'programer'):
            gaji.append('Rp.500000')
            jawab = input("\n Tambahan data(y/t) :")
            no +=1

        elif(jab == 'operator'):
            gaji.append('Rp.400000')
            jawab = input("\n Tambahan Data(y/t) :")
            no +=1
            

        else :
            print ("\nTidak ada")
            from Menu import Login
             
            
    for i in range (no) :
        table.add_rows([['No' ,'Nama','Jabatan','Gaji'],
                        [i+1, nama[i],jabatan[i],gaji[i]]])

    print(table.draw())




