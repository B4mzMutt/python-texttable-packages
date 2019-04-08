def login():
    from Program.menu import menu
    import getpass
    print ("-"*40)
    print (""*6,"Welcome to My Program Texttable Python",""*6)
    print ("-"*40)
    print ("-"*7)
    print (""*6,"LOGIN",""*6)
    print ("-"*7)
    USERNAME = input("Username : ")
    PASSWORD = getpass.getpass("Password : ")
    if USERNAME == 'B4mz' and PASSWORD == '1234':
        print ("Successfully Login!")
        menu()
    else:
        print ("LOGIN GAGAL")
        exit()

