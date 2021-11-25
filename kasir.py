menu = "y" or "Y"
while menu == "y" or "Y":
    print(" ========================================")
    print(" Selamat Datang di Siti Shop")
    print(" List Menu Kebutuhan Pokok")
 
    print(" ========================================")
    print(" 1. Telur Seperemoat : Rp 6000")
    print(" 2. Telur Setengah kilo : Rp 12.000")
    print(" 3. Telur 1 kilo : Rp 21.000")
    print(" 4. Indomie : Rp 3000")
    print(" 5. Minyak Goreng : Rp. 8000")
    print(" ========================================")
    listMenu=str(input(" Masukkan angka sesuai dengan menu yang tersedia = "))
    jumlahPesanan=int(input(" Jumlah dibeli = "))
    if listMenu == "1":
        namaMenu= " Telur Seperemoat"
        harga=(6000*jumlahPesanan)
        pajak= int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga=int(harga+pajak)
        else:
            totalHarga=int(harga+pajak)
    elif listMenu == "2":
        namaMenu= "Telur Setengah kilo"
        harga = (12000*jumlahPesanan)
        pajak = int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga =int(harga+pajak)
        else:
            totalHarga =int(harga+pajak)
    elif listMenu == "3":
        namaMenu= "  Telur 1 kilo"
        harga=int(21000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga=int(harga+pajak)
    elif listMenu == "4":
        namaMenu= " Indomie"
        harga=int(3000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    elif listMenu == "5":
        namaMenu= " Minyak Goreng "
        harga=int(8000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga+pajak)
    else:
        menu=input(" Maaf,Menu yang dipilih tidak tersedia di restoran")
 
    print(" ------------------------------")
    print(" Menu :",namaMenu)
    print(" Jumlah Pesanan :", jumlahPesanan)
    print(" Harga :", harga)
    print(" Pajak :", pajak)
    print(" ------------------------------")
    print(" Total Pembayaran :", totalHarga)
    print(" ------------------------------")
    menu=input(" Mau pesan lagi? pilih Y jika Ya, pilih N jika Tidak (Y/N) = ")