def menu():
    from texttable import Texttable
    table = Texttable ()
    table.add_rows([['NO','PILIHAN PROGRAM'],['1','Penilaian'],['2','Penggajian'],['3','Pembayaran'],['4','Calculator'],['5','Exit']])
    print (table.draw())
   
