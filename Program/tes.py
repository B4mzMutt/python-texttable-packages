def bayar():
    from Program.menu1 import menu1
    from Program.bayar_uts import bayar_uts
    from Program.bayar_uas import bayar_uas
    import datetime
    from texttable import Texttable
    x = datetime.datetime.now()
    table = Texttable(max_width=700)
    jawab = 'y'
    nim = []
    nama = []
    kelas = []
    bayar_uts = []
    bayar_uas = []
    bulanan = []
    seminar = []
    admin = []
    kas = []
    admin = []
    no = 0
    while(jawab == 'y') :
        nim.append(input("Nim: "))
        nama.append(input("Nama: "))
        kelas.append(input("Kelas: "))
        menu1()
        pilih = input("Masukan Pilihan: ")
        if(pilih == '1'):
            print("Pembayaran UTS")
            uts = 50000
            jmlh = input("Jumlah Mata Kuliah yang dibayar: ")
            bayar_uts.append(int(uts) * int(jmlh))
            tanya = input("Apakah anda ingin melakukan Pembayaran UAS?: (y/t)")
            if (tanya == 'y'):
                print("Pembayaran UAS")
                uas = 50000
                jmlh = input("Jumlah Mata Kuliah yang dibayar: ")
                bayar_uas.append(int(uas) * int(jmlh))
            elif (tanya == 't'):
                bayar_uas.append(0)
            else:
                jawab = input("Please Input (y/t) only!!!: ")
                if(jawab == 'y'):
                    return(pilih)
                else:
                    exit()
        elif(pilih == '2'):
            print("Pembayaran UAS")
            uas = 50000
            jmlh = input("Jumlah Mata Kuliah yang dibayar: ")
            bayar_uas.append(int(uas) * int(jmlh))
            tanya = input("Apakah anda ingin melakukan Pembayaran UTS?: (y/t)")
            if (tanya == 'y'):
                print("Pembayaran UTS")
                uas = 50000
                jmlh = input("Jumlah Mata Kuliah yang dibayar: ")
                bayar_uas.append(int(uts) * int(jmlh))
            elif (tanya == 't'):
                bayar_uts.append(0)
            else:
                jawab = input("Please Input (y/t) only!!!: ")
                if(jawab == 'y'):
                    return(pilih)
                else:
                    exit()
        else:
            print ("Pilihan Anda Tidak Terdaftar")
            no += 1
        jmlh = (int(input("Jumlah SPP yang ingin Dibayar : ")))
        bulanan.append(jmlh*500000)
        tanya = (input("Apakah anda ingin membayar Seminar?: (y/t)"))
        if (tanya == 'y'):
            seminar.append(100000)
        elif (tanya == 't'):
            seminar.append(0)
        else:
            exit()
        tanya =(input("Apakah anda ingin membayar Kas?: (y/t)"))
        if (tanya == 'y'):
            jmlh = (int(input("Jumlah Kas yang ingin dibayar?: ")))
            kas.append(20000*jmlh)
        elif (tanya == 't'):
            kas.append(0)
        else:
            exit()
        print("\tBiaya Administrasi : ")
        admin.append(5000)
        no += 1
        for i in range(no):
            uts = int(bayar_uts[i])
            uas = int(bayar_uas[i])
            spp = int(bulanan[i])
            event = int(seminar[i])
            ks = int(kas[i])
            adm = int(admin[i])
            total = (uts) + (uas) + (spp) + (event) + (ks) + (adm)
            table.set_cols_dtype(['i','i','i','i','i','i','i','i','i','i','i'])
            table.add_rows([['NO','NIM','NAMA','KELAS','UTS','UAS','BULANAN','SEMINAR','KAS','BIAYA ADMIN','TOTAL PEMBAYARAN'],[i+1,nim[i],nama[i],kelas[i],bayar_uts[i],bayar_uas[i],bulanan[i],seminar[i],kas[i],admin[i],total]])
        print(table.draw())
        break


