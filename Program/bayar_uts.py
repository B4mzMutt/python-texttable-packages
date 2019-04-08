def bayar_uts():
    from texttable import Texttable
    table = Texttable()
    print("Pembayaran UTS")
    uts = 500000
    jmlh = input("Jumlah Mata Kuliah yang dibayar: ")
    kali = int(uts) * int(jmlh)
    print("Total Pembayaran: ",kali)


