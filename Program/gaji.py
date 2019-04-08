def gaji():
    from texttable import Texttable
    table = Texttable()
    jawab = 'y'
    nama = []
    jabatan = []
    gaji = []
    no = 0
    while(jawab == 'y') :
        nama.append(input("Masukan Nama: "))
        jab = input ("Jabatan: ")
        jabatan.append(jab)
        if(jab == 'Direktur'):
            jabatan = ['Direktur']
            gaji.append('Rp.50.000.000')
            jawab = input("Tambah lagi (y/t)?: ")
            no += 1
        elif(jab == 'Manager'):
            jabatan = ['Manager']
            gaji.append('Rp.35.000.000')
            jawab = input("Tambah lagi (y/t)?: ")
            no += 1
        elif(jab == 'Programmer'):
            jabatan = ['Programmer']
            gaji.append('Rp.40.000.000')
            jawab = input("Tambah lagi (y/t)?: ")
            no += 1
        elif(jab == 'Koordinator'):
            jabatan = ['Koordinator']
            gaji.append('Rp.10.000.000')
            jawab = input("Tambah lagi (y/t)?: ")
            no += 1
        elif(jab == 'Sales'):
            jabatan = ['Sales']
            gaji.append('Rp.4.500.000')
            jawab = input("Tambah lagi (y/t)?: ")
            no += 1
        else:
            print ("Jabatan yang Anda Masukan tidak terdaftar")
            continue
            no += 1
    for i in range(no):
        table.add_rows([['NO','NAMA','JABATAN','GAJI'],[i+1,nama[i],jabatan[i],gaji[i]]])
        print(table.draw())


