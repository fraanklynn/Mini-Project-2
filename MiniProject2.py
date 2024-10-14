print("-------------------------------")
print("     Franklyn Galvin Lodo      ")
print("        Mini Project 2         ")
print("         2409116047            ")
print("-------------------------------")

studios = [
    {'id': 1, 'nama': 'Studio A', 'harga': 'Rp 65000', 'kapasitas': 4},
    {'id': 2, 'nama': 'Studio B', 'harga': 'Rp 85000', 'kapasitas': 8},
    {'id': 3, 'nama': 'Studio C', 'harga': 'Rp 75000', 'kapasitas': 6},
]

jumlah_studio = 3
for_admin = {'admin': 'galpen'}  
for_customer = {'customer': 'belidong'}  

def login():
    role = input("Masukkan role (admin/customer): ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if role == 'admin' and username in for_admin and for_admin[username] == password:
        print("Selamat datang admin!")
        return 'admin'
    elif role == 'customer' and username in for_customer and for_customer[username] == password:
        print("Selamat datang customer!")
        return 'customer'
    else:
        print("Login gagal!")
        return None

def tambah_studio(jumlah_studio):
    if jumlah_studio >= 20:
        print("Tidak bisa menambah studio, kapasitas studio penuh!")
        return jumlah_studio

    nama = input("Masukkan nama studio baru: ")
    harga = input("Masukkan harga sewa: ")
    kapasitas = input("Masukkan kapasitas studio: ")

    studios.append({
        'id': jumlah_studio + 1,
        'nama': nama,
        'harga': harga,
        'kapasitas': kapasitas
    })
    
    jumlah_studio += 1  
    print("Studio berhasil ditambahkan!")
    return jumlah_studio  
def tampilkan_studio():
    print("\n+----+----------------+--------------+-------------+")
    print("| ID | Nama           | Harga        | Kapasitas   |")
    print("+----+----------------+--------------+-------------+")
    for studio in studios:
        print("| " + str(studio['id']) + " | " + 
              studio['nama'] + " " * (14 - len(studio['nama'])) + "| " + 
              studio['harga'] + " " * (12 - len(studio['harga'])) + "| " + 
              str(studio['kapasitas']) + " " * (11 - len(str(studio['kapasitas']))) + "|")
    print("+----+----------------+--------------+-------------+")

def update_studio():
    id = int(input("Masukkan ID studio yang ingin diupdate: "))
    for i in range(jumlah_studio):
        if studios[i]['id'] == id:
            studios[i]['nama'] = input("Masukkan nama baru: ")
            studios[i]['harga'] = input("Masukkan harga baru: ")
            studios[i]['kapasitas'] = input("Masukkan kapasitas baru: ")
            print("Studio berhasil diupdate!")
            return 
    print("Studio tidak ditemukan!")

def hapus_studio(jumlah_studio):
    id = int(input("Masukkan ID studio yang ingin dihapus: "))
    for i in range(jumlah_studio):
        if studios[i]['id'] == id:
            studios.pop(i) 
            print("Studio berhasil dihapus!")
            return jumlah_studio - 1  
    print("Studio tidak ditemukan!")
    return jumlah_studio

def menu_admin(jumlah_studio):
    menu = True
    while menu:
        print("\n+--------------------+")
        print("|      Menu Admin    |")
        print("+--------------------+")
        print("| 1. Tambah Studio   |")
        print("| 2. Tampilkan Semua |")
        print("| 3. Update Studio   |")
        print("| 4. Hapus Studio    |")
        print("| 5. Keluar          |")
        print("+--------------------+")
        opsi = input("Pilih menu: ")

        if opsi == '1':
            jumlah_studio = tambah_studio(jumlah_studio)
        elif opsi == '2':
            tampilkan_studio()
        elif opsi == '3':
            update_studio()
        elif opsi == '4':
            jumlah_studio = hapus_studio(jumlah_studio)
        elif opsi == '5':
            print("Terimakasih telah login!")
            menu=False
        else:
            print("Pilihan anda tidak ada!")

def sewa_studio():
    id = int(input("Masukkan ID studio yang ingin disewa: "))
    for studio in studios:
        if studio['id'] == id:
            print("Studio " + studio['nama'] + " berhasil disewa dengan harga " + studio['harga'] + "!")
            return
    print("Studio tidak ditemukan!")

def menu_customer():
    menu = True
    while menu:
        print("\n+--------------------+")
        print("|    Menu Customer    |")
        print("+--------------------+")
        print("| 1. Tampilkan Semua |")
        print("| 2. Sewa Studio     |")
        print("| 3. Keluar          |")
        print("+--------------------+")
        opsi = input("Pilih menu: ")

        if opsi == '1':
            tampilkan_studio()
        elif opsi == '2':
            sewa_studio()
        elif opsi == '3':
            print("Terimakasih telah login!")
            menu=False
        else:
            print("Pilihan tidak ada!")

role = login()  
if role == 'admin':
    menu_admin(jumlah_studio)   
elif role == 'customer':
    menu_customer()
