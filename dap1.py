import sys
import os

def soal1 ():
    while True:
        try:
            beli = int(input("Masukkan pembayaran : "))
        except ValueError:
            print ("Maaf input salah")

        else :
            if (beli > 100000) :
                print ("Anda mendapat diskon 10%")
            else :
                print ("Total belanja anda = ", beli)
            break
    input()
    return main()

def soal2 ():
    barang = int(input("Masukkan barang : "))
    if (barang < 100):
        barang = barang * 10000
    elif (barang >= 100 and barang < 150) :
        barang = barang * 9500
    else :
        barang = barang * 9000

    print ("total harga = ", barang)
    input()
    return main()


def soal3 ():
    bil = int(input("Masukkan bilangan : "))
    if (bil < 0 ) :
        print ("Negatif")
    else :
        print ("Positif")

    print ("Finish")
    input()
    return main()

def soal4 ():
    bil1 = int(input("Masukkan barang 1 : "))
    bil2 = int(input("Masukkan barang 2 : "))
    bil3 = int(input("Masukkan barang 3 : "))
    bil4 = int(input("Masukkan barang 4 : "))

    if(bil1 > bil2) : besar1 = bil1
    elif (bil1 < bil2) : besar1 = bil2
    else :
        besar1 = bil1

    if(bil3 > bil4) : besar2 = bil3
    elif (bil3 < bil4) : besar2 = bil4
    else :
        besar2 = bil3

    if (besar1 > besar2) :
        print ("%d adalah yang terbesar" % (besar1))
    elif (besar1 < besar2) :
        print ("%d adalah yang terbesar" % (besar2))
    else :
        print ("Semua bilangan sama besar")
    input()
    return main()

def soal5() :
    print ("KALKULATOR CIECIE\n")
    print ("Pilih Operasi Bilangan : ")
    print ("1. Pertambahan ")
    print ("2. Pengurangan ")
    print ("3. Perkalian ")
    print ("4. Pembagian \n")

    pilihan = int(input("Masukkan Menu (1 - 4) : "))

    if pilihan == 1 :
        print("PENAMBAHAN")
        bil1 = int(input("Masukkan bilangan 1 : "))
        bil2 = int(input("Masukkan bilangan 2 : "))

        hasil = bil1 + bil2
        print ("Hasil %d + %d adalah = %d" % (bil1, bil2, hasil))

    elif pilihan == 2 :
        print("PENGURANGAN")
        bil1 = int(input("Masukkan bilangan 1 : "))
        bil2 = int(input("Masukkan bilangan 2 : "))

        hasil = bil1 - bil2
        print ("Hasil %d - %d adalah = %d" % (bil1, bil2, hasil))

    elif pilihan == 3 :
        print("PERKALIAN")
        bil1 = int(input("Masukkan bilangan 1 : "))
        bil2 = int(input("Masukkan bilangan 2 : "))

        hasil = bil1 * bil2
        print ("Hasil %d x %d adalah = %d" % (bil1, bil2, hasil))

    elif pilihan == 4 :
        print("PEMBAGIAN")
        bil1 = int(input("Masukkan bilangan 1 : "))
        bil2 = int(input("Masukkan bilangan 2 : "))

        hasil = bil1 / bil2
        print ("Hasil %d : %d adalah = %d" % (bil1, bil2, hasil))

    elif pilihan == 0 :
        sys.exit()

    else :
        print ("Maaf input salah")

    input()
    os.system("clear")
    return main()

def soal6 () :
    print ("Program Bulan")
    bulan = int(input("Masukkan angka bulan : "))

    if bulan == 1 : print ("Bulan ke %d = Januari" % (bulan))
    elif bulan == 2 : print ("Bulan ke %d = Februari" % (bulan))
    elif bulan == 3 : print ("Bulan ke %d = Maret" % (bulan))
    elif bulan == 4 : print ("Bulan ke %d = April" % (bulan))
    elif bulan == 5 : print ("Bulan ke %d = Mei" % (bulan))
    elif bulan == 6 : print ("Bulan ke %d = Juni" % (bulan))
    elif bulan == 7 : print ("Bulan ke %d = Juli" % (bulan))
    elif bulan == 8 : print ("Bulan ke %d = Agustus" % (bulan))
    elif bulan == 9 : print ("Bulan ke %d = September" % (bulan))
    elif bulan == 10 : print ("Bulan ke %d = Oktober" % (bulan))
    elif bulan == 11 : print ("Bulan ke %d = November" % (bulan))
    elif bulan == 12 : print ("Bulan ke %d = Desember" % (bulan))
    else : print ("Bulan ke %d Tidak ada " % (bulan))
    input()
    return main()

def main() :
    os.system("clear")
    print ("Menu")
    print ("1. Diskon")
    print ("2. Total Harga")
    print ("3. Positif negatif")
    print ("4. Bilangan Terbesar")
    print ("5. kalkulator sederhana")
    print ("6. Bulan Angka\n")
    print ("0. EXIT\n")

    soal = int(input("Masukkan menu : "))
    if soal == 1 : soal1()
    elif soal == 2 : soal2()
    elif soal == 3 : soal3()
    elif soal == 4 : soal4()
    elif soal == 5 : soal5()
    elif soal == 0 : sys.exit()
    else : soal6()
    return

main()
