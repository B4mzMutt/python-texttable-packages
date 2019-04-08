def menu1():
    from texttable import Texttable
    table = Texttable()
    table.add_rows([['NO','PILIHAN PEMBAYARAN'],['1','Bayar UTS'],['2','Bayar UAS']])
    print (table.draw())
        
