# Mini-Project-2

## Flowchart 
![flowchart mini project 2 drawio](https://github.com/user-attachments/assets/67197d06-051c-4ba5-892b-7d29e8126c1a)

##  baris ke 8-10 informasi tentang nama, judul, dan NIM.
#### print("-------------------------------")
#### print("     Franklyn Galvin Lodo      ")
#### print("        Mini Project 2         ")
#### print("         2409116047            ")
#### print("-------------------------------")

## baris ke 15-17 mendefinisikan list studios yang berisi dictionary untuk setiap studio, dengan data seperti ID, nama, harga, dan kapasitas.
#### studios = [
####    {'id': 1, 'nama': 'Studio A', 'harga': 'Rp 65000', 'kapasitas': 4},
####   {'id': 2, 'nama': 'Studio B', 'harga': 'Rp 85000', 'kapasitas': 8},
####    {'id': 3, 'nama': 'Studio C', 'harga': 'Rp 75000', 'kapasitas': 6},
#### ]

## baris 24 dan 26 mendefinisikan dictionary untuk menyimpan username dan password untuk admin dan customer.
## jumlah studio adalah 3 
#### jumlah_studio = 3
## untuk list pertama ada username untuk admin serta passwordnya
#### for_admin = {'admin': 'galpen'}  
## untuk list kedua ada username customer serta passwordnya
##### for_customer = {'customer': 'belidong'}  

##  baris 30-32 meminta input dari pengguna untuk role admin atau customer , username, dan password.
#### def login():
####    role = input("Masukkan role (admin/customer): ")
####    username = input("Masukkan username: ")
####    password = input("Masukkan password: ")

## memeriksa apakah input sesuai jika cocok, mengembalikan role pengguna jika tidak, maka login gagal
## jika role sama dengan admin lalu username dan password admin benar maka akan lanjut ke tampilan selanjutnya/ke tampilan admin
####    if role == 'admin' and username in for_admin and for_admin[username] == password:
####        print("Selamat datang admin!")
## jika role sama dengan customer lalu username dan password customer benar maka akan lanjut ke tampilan selanjutnya/tampilan customer
####    elif role == 'customer' and username in for_customer and for_customer[username] == password:
####        print("Selamat datang customer!")
## jika username atau password dari input admin dan customer salah maka login gagal
####    else:
####        print("Login gagal!")

## memeriksa apakah jumlah studio sudah mencapai batas maksimal yaitu 20 jika ya, tidak melanjutkan dan mengembalikan jumlah_studio.
#### def tambah_studio(jumlah_studio):
####    if jumlah_studio >= 20:
## jika lebih dari 20 maka sistem akan mengingatkan kapasitas studio penuh
####        print("Tidak bisa menambah studio, kapasitas studio penuh!")
####        return jumlah_studio

## meminta pengguna untuk memberi nama,harga, dan kapasitas untuk menambah studio baru
####    nama = input("Masukkan nama studio baru: ")
####    harga = input("Masukkan harga sewa: ")
####    kapasitas = input("Masukkan kapasitas studio: ")

## menambahkan studio baru ke list studios fungsi append dalam konteks ini digunakan untuk menambahkan elemen baru ke dalam list studios penambahan id jumlah studio akan bertambah satu
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

## memakai looping untu mencetak informasi di dalam tabel
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
## id harus integer karna id harus berupa angka agar mempermudah untuk mencari studio
####    id = int(input("Masukkan ID studio yang ingin diupdate: "))
## menggunakan looping for i in range agar bisa mengakses setiap studio yang ingin diubah, dan juga memperbarui studio
####    for i in range(jumlah_studio):
## jika id studio ada di data list diatas maka akan otomatis mengakses studio tersebut untuk diperbarui
####        if studios[i]['id'] == id:
## input nama baru untuk studio yang ingin di perbarui
####            studios[i]['nama'] = input("Masukkan nama baru: ")
## input harga baru untuk studio yang ingin diperbarui
####            studios[i]['harga'] = input("Masukkan harga baru: ")
## masukkan kapasitas baru untuk studio yang ingin diperbarui
####            studios[i]['kapasitas'] = input("Masukkan kapasitas baru: ")
## jika sudah diisi semua maka studio berhasil diupdate
####            print("Studio berhasil diupdate!")
####            return 
## jika id studio tidak ada dalam data maka studio tidak ditemukan
####    print("Studio tidak ditemukan!")

## meminta id studio yang ingin dihapus, id studio harus integer agar mempermudah mengakses setiap studio
#### def hapus_studio(jumlah_studio):
####    id = int(input("Masukkan ID studio yang ingin dihapus: "))

## looping range jumlah studio memungkinkan untuk mengakses setiap studio di list menggunakan .pop untuk menghapus elemen/studio
####    for i in range(jumlah_studio):
## id studio harus ada yang di dalam data jika ingin menghapus studio
####        if studios[i]['id'] == id:
####            studios.pop(i)  
## ini jika sudah menghapus studio
####            print("Studio berhasil dihapus!")
## menegembalikan studio dan berkurang 1
####            return jumlah_studio - 1  
## jika id studio tidak ada di dalam data maka studio tidak ditemukan dan tidak ada yang bisa dihapus
####    print("Studio tidak ditemukan!")
####    return jumlah_studio

## menampilkan pilihan menu untuk admin memakai true agar menu muncul saat di run
#### def menu_admin(jumlah_studio):
####    menu = True
####    while menu:
####        print("\n+--------------------+")
####        print("|      Menu Admin    |")
####        print("+--------------------+")
####        print("| 1. Tambah Studio   |")
####        print("| 2. Tampilkan Semua |")
####        print("| 3. Update Studio   |")
####        print("| 4. Hapus Studio    |")
####        print("| 5. Keluar          |")
####        print("+--------------------+")
####        opsi = input("Pilih menu: ")

## opsi 1 maka akan ke tambah studio tampilan untuk menambah studio
####        if opsi == '1':
####            jumlah_studio = tambah_studio(jumlah_studio)
## opsi 2 ke tampilkan semua id, nama,harga dan kapasitas studio
####        elif opsi == '2':
####            tampilkan_studio()
## opsi ke 3 perbarui studio tampilan untuk memperbarui studio yang ingin diperbarui
####        elif opsi == '3':
####            update_studio()
## opsi ke 4 ke hapus studio tampilan untuk menghapus studio yang ingin dihapus
####        elif opsi == '4':
####            jumlah_studio = hapus_studio(jumlah_studio)
## opsi ke 5 akan keluar dari program
####        elif opsi == '5':
####            print("Terima kasih telah login!")
####            menu = False

## jika pilihan diluar dari opsi maka pilihan tidak ada
####        else:
####            print("Pilihan anda tidak ada!")

## meminta input id studio yang mau disewa
#### def sewa_studio():
####    id = int(input("Masukkan ID studio yang ingin disewa: "))
## memakai looping for agar bisa mengakses semua studio
####    for studio in studios:
## yang didalam kurung adalah id yang ada di dalam data list di lines awal tadi
####        if studio['id'] == id:
## lalu memakai print studio dengan menambahkan studio['nama'] yang didalam kurung adalah data nama yang ada di list dan sama juga dengan harga
####            print("Studio " + studio['nama'] + " berhasil disewa dengan harga " + studio['harga'] + "!")
## return untuk mengembalikan list studio yang akan disewa
####            return
## jika tidak ada data yang di dalam list maka studio tidak ditemukan
####    print("Studio tidak ditemukan!")

## menampilkan menu untuk customer jika login untuk customer maka akan keluar menu untuk customer memakai menu=true agar menu muncul
#### def menu_customer():
####    menu = True
####    while menu:
## tampilan menunya
#####        print("\n+--------------------+")
####        print("|    Menu Customer    |")
####        print("+--------------------+")
####        print("| 1. Tampilkan Semua |")
####        print("| 2. Sewa Studio     |")
####        print("| 3. Keluar          |")
####        print("+--------------------+")
## pengguna memilih opsi untuk menunya yang dipilih apa saja
####        opsi = input("Pilih menu: ")
## jika opsi 1 akan menampilkan id studio nama harga dan kapasitas studio yang tersedia
####        if opsi == '1':
####            tampilkan_studio()
## jika opsi ke 2 akan menampilkan mekanisme penyewaan studio 
####        elif opsi == '2':
####            sewa_studio()
## jika opsi ke 3 maka akan keluar dari program
####        elif opsi == '3':
####            menu=False
## jika pilihan lainnya maka pilihan tidak ada
####        else:
####            print("Pilihan tidak ada!")

## untuk mengeksekusi program 
#### role = login()  
## jika role sama dengan admin dan login benar maka akan langsung ke tampilan menu untuk admin
#### if role == 'admin':
####    menu_admin(jumlah_studio)   
## jika role sama dengan dan login untuk customer benar maka akan langsung ke tampilan menu untuk customer
#### elif role == 'customer':
####    menu_customer()

## tampilan login admin berhasil dan tampilan menu admin
![Screenshot 2024-10-14 101227](https://github.com/user-attachments/assets/517855f9-357e-4439-8c71-f1aaa4fbe017)

## tampilan studio yang tersedia
![Screenshot 2024-10-14 101312](https://github.com/user-attachments/assets/404e9791-303b-4fec-a2a3-c42584345065)

## tampilan untuk penambahan studio dan tampilan jika studio ditambah
![Screenshot 2024-10-14 101428](https://github.com/user-attachments/assets/3c30afd4-1d44-4c5f-8750-e563e5d98c95)

## tampilan jika ingin memperbarui studio dan tampilan jika studio telah diperbarui
![Screenshot 2024-10-14 101602](https://github.com/user-attachments/assets/5c5c8415-a197-4348-9062-4f235cdd1b4d)

## tampilan jika ingin menghapus studio dan tampilan studio yang telah dihapus
![Screenshot 2024-10-14 101644](https://github.com/user-attachments/assets/72a6b7af-f954-4a62-8157-6ea187338678)

## tampilan jika opsi keluar dari program
![Screenshot 2024-10-14 101715](https://github.com/user-attachments/assets/5924d414-6462-4d9a-b763-19d4bca6cce1)

## output jika login gagal
![Screenshot 2024-10-14 101808](https://github.com/user-attachments/assets/310f9c42-c01a-461e-b145-1bf06593c8c1)

## tampilan login customer berhasil dan tampilan menu customer dan tampilan studio yang tersedia untuk disewa
![Screenshot 2024-10-14 101855](https://github.com/user-attachments/assets/7f25e7e4-5b4a-459e-9720-624c31e8a987)

## tampilan jika ingin menyewa studio dan pemilihan studio yang ingin disewa dan studio yang disewa berhasil
![Screenshot 2024-10-14 101930](https://github.com/user-attachments/assets/9294ee49-5176-4e0b-add1-ba354eee463b)

## output jika ingin keluar dari program
![Screenshot 2024-10-14 101951](https://github.com/user-attachments/assets/e6235140-c0aa-4664-b31f-55cae4a4ae1b)

## output jika login customer salah
![Screenshot 2024-10-14 110720](https://github.com/user-attachments/assets/22813382-fcc0-4303-b10e-1518f02360fa)

## tampilan jika studio yang ingin di update tidak ada di data 
![Screenshot 2024-10-14 110820](https://github.com/user-attachments/assets/a064ea91-8831-42ef-8a37-9402554ae16e)

## tampilan jika studio yang ingin dihapus tidak ada di data
![Screenshot 2024-10-14 110846](https://github.com/user-attachments/assets/5ea146dc-4ce8-4d5b-a1cb-398e7a41618b)

## tampilan jika studio yang ingin disewa tidak ada di data
![Screenshot 2024-10-14 111004](https://github.com/user-attachments/assets/cc6b3add-c73c-4ed0-8e93-89f0746ee6f3)
















