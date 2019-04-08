def calculator() :
    def tambah() :
        print ('1.Penjumlahan')
        jumlah = float(a) + float(b)
        print (a,'+',b ,'=',jumlah)
        tanya()
    def kurang() :
        print ('2.Pengurangan')
        kurang = float(a) - float(b)
        print (a,'–',b,'=',kurang)
        tanya()
    def kali() :
        print ('3.Perkalian')
        kali = float(a) * float(b)
        print (a,'*',b ,'=',kali)
        tanya()
    def bagi() :
        print ('4.Pembagian')
        bagi = float(a) / float(b)
        print (a,'/',b ,'=',bagi)
        tanya()
    def tanya() :
        choose = input ('Ulangi lagi (Y/T)? ')
        if (choose == 'Y' or choose == 'y'):
            calculator()
        elif (choose == 'T' or choose == 't'):
            print ('Terima kasih sudah menggunakan program ini')
        else :
            print ('Maaf, input yang Anda masukkan salah')
            print ('Silahkan masukkan Y atau T')
            tanya()
    def menu():
        from texttable import Texttable
        table = Texttable ()
        table.add_rows([['NO','MENU'],['1','PENJUMLAHAN'],['2','PENGURANGAN'],['3','PERKALIAN'],['4','PEMBAGIAN'],['5','EXIT']])
        print (table.draw())
    menu()
    pil = input ('Masukkan pilihan : ')
    if (pil == '1'):
        a = input ('Masukkan nilai x = ')
        b = input ('Masukkan nilai y = ')
        tambah()
    elif (pil == '2'):
        a = input ('Masukkan nilai x = ')
        b = input ('Masukkan nilai y = ')
        kurang()
    elif (pil == '3'):
        a = input ('Masukkan nilai x = ')
        b = input ('Masukkan nilai y = ')
        kali()
    elif (pil == '4'):
        a = input ('Masukkan nilai x = ')
        b = input ('Masukkan nilai y = ')
        bagi()
    elif (pil == '5'):
        exit()
    else :
        print ('Maaf, input yang Anda masukkan salah')
        print ('coba ulangi lagi')
        tanya()
        calculator()


