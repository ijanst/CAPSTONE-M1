# Type Data Dictionary
Data_Karyawan = {
    230100 : ['Naura', 'Perempuan','Manager','SHE', '10/12/2022'],
    230101 : ['Mego', 'Laki-laki','SPV','BisDev', '10/12/2022'],
    230102 : ['Siska', 'Perempuan','Staff','Procurement', '12/10/2016'],
    230103 : ['Ilham', 'Laki-laki','Staff','Engineering', '01/03/2023'],
    230104 : ['Anshari', 'Laki-laki','Staff','Sisfo', '12/12/2022']
}

# View Home Page
def ListDB():
        print("\n\t\t\t           Data Karyawan : \n")
        print("Index\t|  ID   |    Nama   |     Gender     |     Jabatan    |      Unit      |    TMT    ")
        for a,b in enumerate(Data_Karyawan):
            print(f'{a}\t|{b}\t|{Data_Karyawan[b][0].ljust(10)} |{Data_Karyawan[b][1].ljust(15)} |{Data_Karyawan[b][2].ljust(15)} |{Data_Karyawan[b][3].ljust(15)} |{Data_Karyawan[b][4]}')

def view(dict):
        print("\n\t\t\t           Data Karyawan : \n")
        print('ID\t|Nama Karyawan\t|Gender|Jabatan|Unit|TMT')
        for a in dict:
            print(f"{a}\t|{dict[a][0].ljust(10)} |{dict[a][1].ljust(15)} |{dict[a][2].ljust(15)} |{dict[a][3].ljust(15)} |{dict[a][4].ljust(15)} ")
# Sub Menu
def submenu1():     
     print('''
                -=<< CHOOSE MENU >>=-
                \t
                1. Back to Menu Utama
                2. Exit Program
''')
     
     while True:
        User_menu_2 = input("Masukkan pilihan : ")
        if User_menu_2.isdigit() == True and 1 <= int(User_menu_2) <= 2:
            User_menu_2 = int(User_menu_2)
            if User_menu_2 == 1:
             break
            elif User_menu_2 == 2:
             exit()              
        else:
            print("input invalid")


# Menu Menambahkan
def add(a,b):
    ind = []
    for a,b in enumerate(dict):
         if a == int(a):
            ind.append(b)
    return ind[0] 

def addict(a,b,c,d,e,f,dict):
    dict[a] = [b,c,d,e,f]

def menu2inp():
        while True:
            a = int(input("\nMasukkan ID Karyawan : "))
            inp_baru = [i for i in Data_Karyawan]
            if a in inp_baru:
                print(" ")
            else:
                break

        while True:
            try:
                b = input("\nMasukkan Nama Karyawan : ").capitalize()
                inp_baru1 = [i for i in Data_Karyawan]
                if b in inp_baru1:
                    print(" ")
                else:
                    break
            except:
                print(" ")

        while True:
            try:
                c = input("\nMasukkan Jenis Kelamin : ").capitalize()
                inp_baru2 = [i for i in Data_Karyawan]
                if b in inp_baru2:
                     print(" ")
                else:
                    break
            except:
                print(" ")
        while True:
            try:
                d = input("\nMasukkan Jabatan : ").capitalize()
                inp_baru3 = [i for i in Data_Karyawan]
                if b in inp_baru3:
                    print(" ")
                else:
                    break
            except:
                print(" ")
        while True:
            try:
                e = input("\nMasukkan Unit : ").capitalize()
                inp_baru4 = [i for i in Data_Karyawan]
                if b in inp_baru4:
                    print(" ")
                else:
                    break
            except:
                print(" ")
        while True:
            try:
                f = input("\nMasukkan TMT : ")
                inp_baru5 = [i for i in Data_Karyawan]
                if b in inp_baru5:
                    print(" ")
                else:
                    break
            except:
                print(" ")
        
        return a,b,c,d,e,f

# Menu Find Data
def get():
    id = int(input("Masukkan ID karyawan yang ingin dicari : "))
    if id not in Data_Karyawan.keys():
        print("\n ID not define!")
    else:
        print(f"\nID: {id}| Nama: {Data_Karyawan[id][0]}|Gender: {Data_Karyawan[id][1]}|Posisi: {Data_Karyawan[id][2]}|Unit: {Data_Karyawan[id][3]}|TMT: {Data_Karyawan[id][4]}")
     
# Menu Update Data
def update():
    ListDB()
    while True:
        id = int(input("\n Masukkan ID karyawan yang ingin diperbarui : "))
        if id in Data_Karyawan.keys():
            print(f"\nID: {id}, Nama: {Data_Karyawan[id][0]}, Gender: {Data_Karyawan[id][1]}, Posisi: {Data_Karyawan[id][2]}, Unit: {Data_Karyawan[id][3]}, TMT: {Data_Karyawan[id][4]}")
            return id
        else:
            print("\n ID not define!")
        
def updateconfirm(id):
    b_ = input("\nMasukkan Nama Karyawan : ").capitalize()
    c_ = input("\nMasukkan Jenis Kelamin : ").capitalize()
    d_ = input("\nMasukkan Jabatan : ").capitalize()
    e_ = input("\nMasukkan Unit : ").capitalize()
    f_ = input("\nMasukkan TMT (dd/mm/yyyy) : ")

    Data_Karyawan[id] = [b_, c_, d_, e_, f_]  
    print('\nData Berhasil di Perbaharui')

def subupdate(id):
    print("1. Nama")
    print("2. Gender")
    print("3. Jabatan")
    print("4. Unit")
    print("5. TMT")
    print("6. selesai")


    while True:
        choice = int(input("Masukkan Data yang ingin diperbaharui : "))
        if choice == 1:
            Data_Karyawan[id][0] = input("Masukkan Nama Karyawan: ")       
            break
        elif choice == 2:
            Data_Karyawan[id][1] = input("Masukkan Gender Karyawan: ")
            break
        elif choice == 3:
            Data_Karyawan[id][2] = input("Masukkan Jabatan Karyawan: ")
            break
        elif choice == 4:
            Data_Karyawan[id][3] = input("Masukkan Unit Karyawan: ")
            break
        elif choice == 5:
            Data_Karyawan[id][4] = input("Masukkan TMT Karyawan: ")
            break
        elif choice == 6:
            break
            
    print('Data Berhasil di Perbaharui')
   
def submenu2():   
    while True:
        print('''
                -=<< CHOOSE MENU >>=-
                \t
                1. Perbaharui Data Karyawan tertentu
                2. Perbaharui Salah Satu Data
                3. Back to Menu Utama
                4. Exit Program
        ''')
        User_menu_3 = int(input("Masukkan pilihan : "))
        if User_menu_3 == 1:
            while True:
                indexupdate = update()
                updkey = []
                for i,j in enumerate(Data_Karyawan):
                    if j == indexupdate:
                        updkey.append(i)
                updkey = updkey[0]
                print(f"{updkey}\t|{Data_Karyawan[indexupdate][0].ljust(10)}\t|{Data_Karyawan[indexupdate][1].ljust(15)}|{Data_Karyawan[indexupdate][2].ljust(15)}|{Data_Karyawan[indexupdate][3].ljust(15)}|{Data_Karyawan[indexupdate][4].ljust(15)} ")
            
                inputL = input('\n Apakah ingin memperbaharui data? (y/n): ')
                if inputL == 'y':
                    updateconfirm(indexupdate)
                    ListDB()
                    submenu2()
                    break
                else:
                    break
        elif User_menu_3 == 2:
            indexupdate = update()
            subupdate(indexupdate)
            ListDB()
            print('\n')
            break
        elif User_menu_3 == 3:
            break
        elif User_menu_3 == 4:
            exit()              
        else:
            print("input invalid")
            

# Menu Delete Data  
def delete(): 
    ListDB()
    while True:
        x = input("\nMasukkan ID yang ingin dihapus : ") 
        if int(x) not in Data_Karyawan.keys():
            print("\n Index not define!")   
        else:
            return x
    
def deleteConfirm(id):
    Data_Karyawan.pop(id)

def submenu3():     
     print('''
                -=<< CHOOSE MENU >>=-
                \t
                1. Back to Menu Utama
                2. Exit Program
''')
     
     while True:
        User_menu_3 = input("Masukkan pilihan : ")
        if User_menu_3.isdigit() == True and 1 <= int(User_menu_3) <= 3:
            User_menu_3 = int(User_menu_3)
            if User_menu_3 == 1:
             break
            elif User_menu_3 == 2:
             exit()               
        else:
            print("input invalid")

        

def menu():
    print('''
            Selamat Datang di Database Karyawan 
                -=== PT Sian Mulana Pe ===-

                        Opsi MENU :
                __________________________
                \t
                1. Tampilkan Data Karyawan
                2. Tambah Data Karyawan
                3. Cari Data Karyawan
                4. Perbarui Data Karyawan
                5. Hapus Data Karyawan
                6. Exit Program
    ''')
    


Gif = 1
while Gif == 1:
    menu()
    print()
 
    while True:
          User_menu = input("Masukkan pilihan MENU : ")
          if User_menu.isdigit() == True and 1 <= int(User_menu) <= 6:
            User_menu = int(User_menu)
            break
          
    if User_menu == 1:
         ListDB()
         submenu1()

    elif User_menu == 2:
         a,b,c,d,e,f = menu2inp()
         addict(a,b,c,d,e,f,Data_Karyawan)
         ListDB()
         submenu1()

    elif User_menu == 3:
         while True:
            get()
            inputlanjut = input("\n Apakah ingin memasukkan ID? (ya/tidak): ")
            if inputlanjut == 'ya':
                continue
            else: 
                break
  
         submenu1()

    elif User_menu == 4:
         submenu2()

    elif User_menu == 5:
          while True:
            indexdelete = delete()
            indexdelete = int(indexdelete)
            print(f'\nID\t|{"Nama Karyawan".ljust(10)}\t|{"Gender".ljust(15)}|{"Jabatan".ljust(15)}|{"Unit".ljust(15)}|TMT')
            print(f"{indexdelete}\t|{Data_Karyawan[indexdelete][0].ljust(10)}\t|{Data_Karyawan[indexdelete][1].ljust(15)}|{Data_Karyawan[indexdelete][2].ljust(15)}|{Data_Karyawan[indexdelete][3].ljust(15)}|{Data_Karyawan[indexdelete][4].ljust(15)} ")
            inputL = input('\n Apakah anda yakin untuk menghapus data ini ? (y/n): ')
            if inputL == 'y':
                deleteConfirm(indexdelete)
                print('\n Data Deleted')
                ListDB()
                submenu3()
                break
            else:
                break 

    elif User_menu == 6:
        inp = input('\n Apakah anda yakin untuk keluar dari program ini ? (y/n): ')
        if inp == 'n':
            continue
        elif inp != 'n':
            break
    else:
        print("Pilihan tidak valid.")
