def bulanan():
    import datetime
    from texttable import Texttable
    x = datetime.datetime.now()
    table = Texttable()
    no = 0
    nama = []
    nim = []
    seminar = []
    kelas = []
    bulanan = []
    admin = []
    kas = []
    nama.append(input("Nama : "))
    nim.append(input("Nim : "))
    kelas.append(input("Kelas : "))
    jmlh = (int(input("Jumlah SPP yang ingin Dibayar : ")))
    bulanan = (jmlh*500000)
    tanya = (input("Apakah anda ingin membayar Seminar?: (y/t)"))
    if (tanya == 'y'):
        seminar.append(100000)
    elif (tanya == 't'):
        admin.append(5000)
    else:
        exit()
    tanya =(input("Apakah anda ingin membayar Kas?: (y/t)"))
    if (tanya == 'y'):
        jmlh = (int(input("Jumlah Kas yang ingin dibayar?: ")))
        kas.append(20000*jmlh)
    elif (tanya == 't'):
        exit()
    else:
        exit()
    no += 1
    
        
    

