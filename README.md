# Mini-Project-2
## informasi tentang nama, judul, dan NIM.
#### print("-------------------------------")
#### print("     Franklyn Galvin Lodo      ")
#### print("        Mini Project 2         ")
#### print("         2409116047            ")
#### print("-------------------------------")

## mendefinisikan list studios yang berisi dictionary untuk setiap studio, dengan data seperti ID, nama, harga, dan kapasitas.
#### studios = [
####    {'id': 1, 'nama': 'Studio A', 'harga': 'Rp 65000', 'kapasitas': 4},
####   {'id': 2, 'nama': 'Studio B', 'harga': 'Rp 85000', 'kapasitas': 8},
####    {'id': 3, 'nama': 'Studio C', 'harga': 'Rp 75000', 'kapasitas': 6},
#### ]

## mendefinisikan dictionary untuk menyimpan username dan password untuk admin dan customer.
#### jumlah_studio = 3
#### for_admin = {'admin': 'galpen'}  
##### for_customer = {'customer': 'belidong'}  

##   meminta input dari pengguna untuk role admin atau customer , username, dan password.
#### def login():
####    role = input("Masukkan role (admin/customer): ")
####    username = input("Masukkan username: ")
####    password = input("Masukkan password: ")

## memeriksa apakah input sesuai jika cocok, mengembalikan role pengguna jika tidak, maka login gagal
####    if role == 'admin' and username in for_admin and for_admin[username] == password:
####        print("Selamat datang admin!")
####    elif role == 'customer' and username in for_customer and for_customer[username] == password:
####        print("Selamat datang customer!")
####    else:
####        print("Login gagal!")

## memeriksa apakah jumlah studio sudah mencapai batas maksimal yaitu 20 jika ya, tidak melanjutkan dan mengembalikan jumlah_studio.
#### def tambah_studio(jumlah_studio):
####    if jumlah_studio >= 20:
####        print("Tidak bisa menambah studio, kapasitas studio penuh!")
####        return jumlah_studio

## meminta pengguna untuk memberi nama,harga, dan kapasitas untuk menambah studio baru
####    nama = input("Masukkan nama studio baru: ")
####    harga = input("Masukkan harga sewa: ")
####    kapasitas = input("Masukkan kapasitas studio: ")

## menambahkan studio baru ke list studios fungsi append dalam konteks ini digunakan untuk menambahkan elemen baru ke dalam list studios.
####    studios.append({
####        'id': jumlah_studio + 1,
####        'nama': nama,
####        'harga': harga,
####        'kapasitas': kapasitas
####    })    
## setiap penambahan studio akan bertambah 1
####    jumlah_studio += 1  
####    print("Studio berhasil ditambahkan!")
####    return jumlah_studio  

## mencetak header untuk tampilan studio dalam format tabel.
#### def tampilkan_studio():
####    print("\n+----+----------------+--------------+-------------+")
####    print("| ID | Nama           | Harga        | Kapasitas   |")
####    print("+----+----------------+--------------+-------------+")

## mencetak informasi di dalam tabel
####    for studio in studios:
####        print("| " + str(studio['id']) + " | " + 
## len(studio['nama']) menghitung panjang nama studio
####              studio['nama'] + " " * (14 - len(studio['nama'])) + "| " + 
## len(studio['harga']) menghitung panjang string harga studio
####              studio['harga'] + " " * (12 - len(studio['harga'])) + "| " + 
## str(studio['kapasitas']) menghitung panjang kapasitas studio.
####              str(studio['kapasitas']) + " " * (11 - len(str(studio['kapasitas']))) + "|")
## print untuk bawah tabel
####    print("+----+----------------+--------------+-------------+")
    
## meminta input id studio yang ingin diperbarui
#### def update_studio():
####    id = int(input("Masukkan ID studio yang ingin diupdate: "))
## menggunakan for i in range agar bisa mengakses setiap studio yang ingin diubah, dan juga memperbarui studio
####    for i in range(jumlah_studio):
####        if studios[i]['id'] == id:
####            studios[i]['nama'] = input("Masukkan nama baru: ")
####            studios[i]['harga'] = input("Masukkan harga baru: ")
####            studios[i]['kapasitas'] = input("Masukkan kapasitas baru: ")
####            print("Studio berhasil diupdate!")
####            return 
####    print("Studio tidak ditemukan!")

## meminta id studio yang ingin dihapus
#### def hapus_studio(jumlah_studio):
####    id = int(input("Masukkan ID studio yang ingin dihapus: "))

## range jumlah studio memungkinkan untuk mengakses setiap studio di list menggunakan .pop untuk menghapus elemen/studio
####    for i in range(jumlah_studio):
####        if studios[i]['id'] == id:
####            studios.pop(i)  
####            print("Studio berhasil dihapus!")
####            return jumlah_studio - 1  
####    print("Studio tidak ditemukan!")
####    return jumlah_studio

## menampilkan pilihan menu untuk admin jika opsi 1 maka akan ke tambah studio, opsi 2 ke tampilkan semua, opsi ke 3 perbarui studio, opsi ke 4
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
            menu = False
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
            menu = False  
        else:
            print("Pilihan tidak ada!")

role = login()  
if role == 'admin':
    menu_admin(jumlah_studio)   
elif role == 'customer':
    menu_customer()
