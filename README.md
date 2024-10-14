# Mini-Project-2

## Flowchart 
![flowchart mini project 2 drawio](https://github.com/user-attachments/assets/67197d06-051c-4ba5-892b-7d29e8126c1a)

##  baris ke 2-4 informasi tentang nama, judul, dan NIM.
#### 1 print("-------------------------------")
#### 2 print("     Franklyn Galvin Lodo      ")
#### 3 print("        Mini Project 2         ")
#### 4 print("         2409116047            ")
#### 5 print("-------------------------------")

## baris ke 7-9 mendefinisikan list studios yang berisi dictionary untuk setiap studio, dengan data seperti ID, nama, harga, dan kapasitas.
#### 6 studios = [
####  7 {'id': 1, 'nama': 'Studio A',  'harga': 'Rp 65000', 'kapasitas': 4},
####  8 {'id': 2, 'nama': 'Studio B', 'harga': 'Rp 85000', 'kapasitas': 8},
####  9  {'id': 3, 'nama': 'Studio C', 'harga': 'Rp 75000', 'kapasitas': 6},
#### 10 ]

## baris ke 12-13 mendefinisikan dictionary untuk menyimpan username dan password untuk admin dan customer.
## jumlah studio adalah 3 
#### 11 jumlah_studio = 3
## untuk list pertama ada username untuk admin serta passwordnya
#### 12 for_admin = {'admin': 'galpen'}  
## untuk list kedua ada username customer serta passwordnya
##### 13 for_customer = {'customer': 'belidong'}  

##  baris 15-17 meminta input dari pengguna untuk role admin atau customer , username, dan password.
#### 14 def login():
####  15  role = input("Masukkan role (admin/customer): ")
####  16   username = input("Masukkan username: ")
####  17  password = input("Masukkan password: ")

## baris ke 18-21 memeriksa apakah input sesuai jika cocok, mengembalikan role pengguna jika tidak, maka login gagal
## baris 18-19 jika role sama dengan admin lalu username dan password admin benar maka akan lanjut ke tampilan selanjutnya/ke tampilan admin
####   18 if role == 'admin' and username in for_admin and for_admin[username] == password:
####   19     print("Selamat datang admin!")
## baris 20-21 jika role sama dengan customer lalu username dan password customer benar maka akan lanjut ke tampilan selanjutnya/tampilan customer
####   20 elif role == 'customer' and username in for_customer and for_customer[username] == password:
####     21   print("Selamat datang customer!")
## baris 22-23 jika username atau password dari input admin dan customer salah maka login gagal
####  22  else:
####   23    print("Login gagal!")

## baris 25-26 memeriksa apakah jumlah studio sudah mencapai batas maksimal yaitu 20 jika ya, tidak melanjutkan dan mengembalikan jumlah_studio.
#### 24 def tambah_studio(jumlah_studio):
####  25  if jumlah_studio >= 20:
## jika lebih dari 20 maka sistem akan mengingatkan kapasitas studio penuh
####    26    print("Tidak bisa menambah studio, kapasitas studio penuh!")
####    27    return jumlah_studio

## baris 28-30 meminta pengguna untuk memberi nama,harga, dan kapasitas untuk menambah studio baru
####  28  nama = input("Masukkan nama studio baru: ")
####  29  harga = input("Masukkan harga sewa: ")
#### 30   kapasitas = input("Masukkan kapasitas studio: ")

## baris 31-36 menambahkan studio baru ke list studios fungsi append dalam konteks ini digunakan untuk menambahkan elemen baru ke dalam list studios penambahan id jumlah studio akan bertambah satu
####  31  studios.append({
####  32      'id': jumlah_studio + 1,
####  33     'nama': nama,
####  34     'harga': harga,
####  35      'kapasitas': kapasitas
####  36  })    
## baris 37-38 setiap penambahan studio akan bertambah 1
####  37  jumlah_studio += 1  
####  38  print("Studio berhasil ditambahkan!")
####  39  return jumlah_studio  

## baris 41-43 mencetak header untuk tampilan studio dalam format tabel.
#### 40 def tampilkan_studio():
#### 41   print("\n+----+----------------+--------------+-------------+")
####   42 print("| ID | Nama           | Harga        | Kapasitas   |")
####  43  print("+----+----------------+--------------+-------------+")

## baris 44 memakai looping untu mencetak informasi di dalam tabel
####  44  for studio in studios:
####  45      print("| " + str(studio['id']) + " | " + 
## baris 46 len(studio['nama']) menghitung panjang nama studio
####   46           studio['nama'] + " " * (14 - len(studio['nama'])) + "| " + 
## baris 47 len(studio['harga']) menghitung panjang string harga studio
####  47            studio['harga'] + " " * (12 - len(studio['harga'])) + "| " + 
## baris 48 str(studio['kapasitas']) menghitung panjang kapasitas studio.
####  48            str(studio['kapasitas']) + " " * (11 - len(str(studio['kapasitas']))) + "|")
## baris 49 mencetak untuk bawah tabel
####  49  print("+----+----------------+--------------+-------------+")
    
## baris 50-56 meminta input id studio yang ingin diperbarui
#### 50 def update_studio():
## baris 51 id harus integer karna id harus berupa angka agar mempermudah untuk mencari studio
####  51  id = int(input("Masukkan ID studio yang ingin diupdate: "))
## baris 52 menggunakan looping for i in range agar bisa mengakses setiap studio yang ingin diubah, dan juga memperbarui studio
####  52  for i in range(jumlah_studio):
## baris 53 jika id studio ada di data list diatas maka akan otomatis mengakses studio tersebut untuk diperbarui
####    53   if studios[i]['id'] == id:
## baris 54 input nama baru untuk studio yang ingin di perbarui
####    54        studios[i]['nama'] = input("Masukkan nama baru: ")
## baris 55 input harga baru untuk studio yang ingin diperbarui
####    55        studios[i]['harga'] = input("Masukkan harga baru: ")
## baris 56 memasukkan kapasitas baru untuk studio yang ingin diperbarui
####    56        studios[i]['kapasitas'] = input("Masukkan kapasitas baru: ")
## baris 57-58 jika sudah diisi semua maka studio berhasil diupdate
####     57       print("Studio berhasil diupdate!")
####     58       return 
## baris 59 jika id studio tidak ada dalam data maka studio tidak ditemukan
####  59  print("Studio tidak ditemukan!")

## baris 61 meminta id studio yang ingin dihapus, id studio harus integer agar mempermudah mengakses setiap studio
#### 60 def hapus_studio(jumlah_studio):
####  61 id = int(input("Masukkan ID studio yang ingin dihapus: "))

## baris 62-64 looping range jumlah studio memungkinkan untuk mengakses setiap studio di list menggunakan .pop untuk menghapus elemen/studio
####  62 for i in range(jumlah_studio):
## baris 63 id studio harus ada yang di dalam data jika ingin menghapus studio
####   63     if studios[i]['id'] == id:
####   64         studios.pop(i)  
## baris 65 ini jika sudah menghapus studio
####   65         print("Studio berhasil dihapus!")
## baris 66 mengembalikan studio dan berkurang 1
####    66        return jumlah_studio - 1  
## baris 67-68 jika id studio tidak ada di dalam data maka studio tidak ditemukan dan tidak ada yang bisa dihapus
####  67  print("Studio tidak ditemukan!")
####  68  return jumlah_studio

## baris 69-80 menampilkan pilihan menu untuk admin memakai true agar menu muncul saat di run
#### 69 def menu_admin(jumlah_studio):
#### 70  menu = True
#### 71   while menu:
#### 72      print("\n+--------------------+")
####  73      print("|      Menu Admin    |")
####  74      print("+--------------------+")
#### 75       print("| 1. Tambah Studio   |")
####  76      print("| 2. Tampilkan Semua |")
####  77      print("| 3. Update Studio   |")
####  78      print("| 4. Hapus Studio    |")
####  79      print("| 5. Keluar          |")
####  80      print("+--------------------+")
## baris 81 input untuk memilih menu
####  81      opsi = input("Pilih menu: ")

## baris 82-83 opsi 1 maka akan ke tambah studio tampilan untuk menambah studio
####    82   if opsi == '1':
####     83       jumlah_studio = tambah_studio(jumlah_studio)
## baris 84-85 opsi 2 ke tampilkan semua id, nama,harga dan kapasitas studio
####    84    elif opsi == '2':
####     85       tampilkan_studio()
## baris 86-87 opsi ke 3 perbarui studio tampilan untuk memperbarui studio yang ingin diperbarui
####    86    elif opsi == '3':
####    87        update_studio()
## baris 88-89 opsi ke 4 ke hapus studio tampilan untuk menghapus studio yang ingin dihapus
####    88    elif opsi == '4':
####    89        jumlah_studio = hapus_studio(jumlah_studio)
## baris 90-91 opsi ke 5 akan keluar dari program
####    90    elif opsi == '5':
####    91       print("Terima kasih telah login!")
####            menu = False

## baris 92-93 jika pilihan diluar dari opsi maka pilihan tidak ada
####    92    else:
####    93        print("Pilihan anda tidak ada!")

## baris 95 meminta input id studio yang mau disewa
#### 94 def sewa_studio():
####  95  id = int(input("Masukkan ID studio yang ingin disewa: "))
## baris 96 memakai looping for agar bisa mengakses semua studio
#### 96   for studio in studios:
## baris 97 yang didalam kurung adalah id yang ada di dalam data list di lines awal tadi
####   97     if studio['id'] == id:
## baris 98 lalu memakai print studio dengan menambahkan studio['nama'] yang didalam kurung adalah data nama yang ada di list dan sama juga dengan harga
####    98        print("Studio " + studio['nama'] + " berhasil disewa dengan harga " + studio['harga'] + "!")
## baris 99 return untuk mengembalikan list studio yang akan disewa
####     99       return
## baris 100 jika tidak ada data yang di dalam list maka studio tidak ditemukan
####  100  print("Studio tidak ditemukan!")

## baris 102-103 menampilkan menu untuk customer jika login untuk customer maka akan keluar menu untuk customer memakai menu=true agar menu muncul
#### 101 def menu_customer():
#### 102   menu = True
#### 103   while menu:
## baris 104-110 tampilan menunya
#####  104      print("\n+--------------------+")
####   105     print("|    Menu Customer    |")
####   106     print("+--------------------+")
####   107     print("| 1. Tampilkan Semua |")
####   108     print("| 2. Sewa Studio     |")
####   109     print("| 3. Keluar          |")
####  110      print("+--------------------+")
## baris 111 pengguna memilih opsi untuk menunya yang dipilih apa saja
####   111     opsi = input("Pilih menu: ")
## baris 112-113 jika opsi 1 akan menampilkan id studio nama harga dan kapasitas studio yang tersedia
####  112      if opsi == '1':
####   113         tampilkan_studio()
## baris 114-115 jika opsi ke 2 akan menampilkan mekanisme penyewaan studio 
####   114     elif opsi == '2':
####   115         sewa_studio()
## baris 116-117 jika opsi ke 3 maka akan keluar dari program
####  116      elif opsi == '3':
####  117          menu=False
## baris 118-119 jika pilihan lainnya maka pilihan tidak ada
####   118    else:
####    119        print("Pilihan tidak ada!")

## baris 120 untuk mengeksekusi program 
#### 120 role = login()  
## baris 121-122 jika role sama dengan admin dan login benar maka akan langsung ke tampilan menu untuk admin
#### 121 if role == 'admin':
#### 122   menu_admin(jumlah_studio)   
## baris 123-124 jika role sama dengan dan login untuk customer benar maka akan langsung ke tampilan menu untuk customer
#### 123 elif role == 'customer':
#### 124   menu_customer()

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
















