from Program.login import login
from Program.menu import menu
from Program.tes import bayar
from Program.gaji import gaji
from Program.nilai import nilai
from Program.menu1 import menu1
from Program.calculator import calculator
from Program.choose import choose
def project():
    login()
    pilih = (input("Masukan Pilihan: "))
    if pilih == '1':
        gaji()
        ulang()
    elif pilih == '2':
        nilai()
        ulang()
    elif pilih == '3':
        bayar()
        ulang()
    elif pilih == '4':
        calculator()
        ulang()
    elif pilih == '5':
        exit
        print ("\nMatur Thanks Kawan")
    else:
        print ("\nPlease Input(1, 2, 3, 4, or 5: ")
        ulang()
def ulang():
    tanya = (input("\nBack To Menu (y/t)?: "))
    if tanya == 'y':
        menu()
        choose()
    elif tanya == 't':
        exit
        print ("\nMatur Thanks Kawan")
    else:
        print ("\nPlease input(y/t): ")
        ulang()
project()

