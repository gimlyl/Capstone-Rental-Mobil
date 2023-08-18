# CAPSTONE PROJECT MODULE 1
# By Vinson Leo Veronal Jong
# Membuat Aplikasi CRUD
# Rental Mobil 

# Import Library For The Table
from tabulate import tabulate

# The Code
ListMobil  = {
     1 :{
        'NamaMobil' : 'Family Size',
        'CarSize' : '6 - 8 Orang',
        'Harga' : 500000,
        'Status' : "Available"
        },
    2 :{
        'NamaMobil' : 'Large',
        'CarSize' : '4 - 6 Orang',
        'Harga' : 400000,
        'Status' : "Not Available"
        },
    3 :{
        'NamaMobil' : 'Regular',
        'CarSize' : '2 - 4 Orang',
        'Harga' : 300000,
        'Status' : "Available"
        },
    4 :{
        'NamaMobil' : 'Small',
        'CarSize' : '2 Orang',
        'Harga' : 200000,
        'Status' : "Available"
        }
    }

cart = []

# Function For Showing Messages
def showMessages(type) :
    if type == 0 :
        print("Terima Kasih Sudah Melakukan Rental Mobil Di Kim Rent Car")
    elif type == 1 :
         print("Inputan Hanya Berupa Angka!")
    elif type == 2 :
        print("Data Tidak Ditemukan!")
    elif type == 3 :
        print("Pembayaran Tidak Mencukupi. Mohon Untuk Melakukan Pembayaran Sesuai Dengan Invoice.")
    elif type == 4:
        print("Menu Pilihan Tidak Ditemukan!")
        
# Function For Show Car Tables
def carTables(data):
    table_headers = ["Index", "Nama Mobil", "Car Size", "Rent Price/Day", "Status"]
    table_data = [(i, item["NamaMobil"], item["CarSize"], item["Harga"], item["Status"]) for i, item in data.items()]
    print(tabulate(table_data, headers=table_headers, tablefmt="outline"))

# Function For Add Car List
def addCars(data):
    namaMobil = input('Masukkan Nama Mobil: ')
    carSize = input('Masukkan Luas/Ukuran Mobil: ')
    hargaSewa = int(input('Masukkan Harga Sewa (Per Hari): '))
    status = "Available" 
    new_index = max(data.keys()) + 1
    data[new_index] = {
        'NamaMobil': namaMobil,
        'CarSize': carSize,
        'Harga': hargaSewa,
        'Status': status
    }
    carTables(data)
    
# Function For Delete Data Inside The Table
def deleteCars(data):
    carTables(data)
    indexItem = int(input('Masukkan index Mobil yang ingin dihapus: '))
    if indexItem in data:
        del data[indexItem]
        carTables(data)
    else:
        showMessages(2)

# Function For Updating The Data Inside The Table
def updateCar(data):
    carTables(data)
    indexItem = int(input('Masukkan index Mobil yang ingin diupdate: '))
    if indexItem in data:
        newNamaMobil = input('Masukkan Nama Mobil Baru: ')
        newCarSize = input('Masukkan Ukuran Mobil Baru: ')
        newHargaSewa = int(input('Masukkan Harga Sewa Baru (Per Hari): '))
        newStatus = input("Masukan Status Mobil (Available / Not Available): ")
        data[indexItem]['NamaMobil'] = newNamaMobil
        data[indexItem]['CarSize'] = newCarSize
        data[indexItem]['Harga'] = newHargaSewa
        data[indexItem]['Status'] = newStatus
        carTables(data)
    else:
        showMessages(2)

# Function For Renting Car
def rentCars(data):
    while True:
        try:
            carTables(data)
            indexItem = int(input('Masukkan No Index Mobil yang Ingin Disewa: '))
            if indexItem in data:
                if data[indexItem]['Status'] == "Not Available":
                    print(f"Mobil {data[indexItem]['NamaMobil']} tidak tersedia. Silakan pilih mobil lain.")
                else:
                    try:
                        rentItem = int(input('Masukkan Jumlah Hari Sewa: '))
                        totalRentPrice = data[indexItem]['Harga'] * rentItem
                        print(f"Total Harga Sewa: {totalRentPrice}")
                        while True:
                            jmlUang = int(input('Masukkan jumlah uang : '))
                            if jmlUang < totalRentPrice:
                                showMessages(3)
                                print(f"Total Pembayaran: {totalRentPrice}")
                            elif jmlUang > totalRentPrice:
                                kembali = jmlUang - totalRentPrice
                                print(f"Terima kasih! Uang kembali anda: {kembali}")
                                cart.append({
                                    'NamaMobil': data[indexItem]['NamaMobil'],
                                    'JumlahHari': rentItem,
                                    'HargaSewa': data[indexItem]['Harga'],
                                    'Index': indexItem,
                                    'TotalBayar': totalRentPrice
                                })
                                break 
                            else:
                                showMessages(0)
                                cart.append({
                                    'NamaMobil': data[indexItem]['NamaMobil'],
                                    'JumlahHari': rentItem,
                                    'HargaSewa': data[indexItem]['Harga'],
                                    'Index': indexItem,
                                    'TotalBayar': totalRentPrice
                                })
                            break  
                    except:
                        showMessages(1)
                checker = input('Lanjut menyewa mobil? (ya/tidak) = ')
                if checker == 'tidak':
                    break
            else:
                showMessages(2)
        except :
            showMessages(1)
# List Menu to Choose
while True:
    chooseMenu = input('''
    Selamat Datang Di Kim Shopping Center

    List Menu:
    1. Menampilkan Daftar Mobil
    2. Menambah Mobil
    3. Menghapus Mobil
    4. Update Mobil
    5. Menyewa Mobil
    6. Exit Program

    Masukkan Angka Menu yang Ingin Dijalankan: 
    ''')

    if chooseMenu == '1':
        carTables(ListMobil)
    elif chooseMenu == '2':
        addCars(ListMobil)
    elif chooseMenu == '3':
        deleteCars(ListMobil)
    elif chooseMenu == '4':
        updateCar(ListMobil)
    elif chooseMenu == '5':
        rentCars(ListMobil)
    elif chooseMenu == '6':
        break
    else :
        showMessages(4)