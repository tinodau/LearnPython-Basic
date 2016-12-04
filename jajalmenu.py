import os
import sys
import math

def basicOperation ():
    print ("Menu Basic Operation")
    print ("1. Penambahan")
    print ("2. Pengurangan")
    print ("3. Perkalian")
    print ("4. Pembagian")
    print ("5. Pemangkatan 2")
    print ("6. Pemangkatan Bebas")
    print ("7. Pengakaran")
    print ("0. EXIT\n")

    pilihan = input("Masukkan menu: ")
    if pilihan == "1" :
        # ======== PENAMBAHAN
        a = int(input ("Bilangan 1 : "))
        b = int(input ("Bilangan 2 : "))
        c = a + b
        print ("Hasilnya penambahan = ", c)

    elif pilihan == "2" :
        # ======== PENGURANGAN
        a = int(input ("Bilangan 1 : "))
        b = int(input ("Bilangan 2 : "))
        c = a - b
        print ("Hasilnya pengurangan = ", c)

    elif pilihan == "3" :
        # ========= PERKALIAN
        a = int(input ("Bilangan 1 : "))
        b = int(input ("Bilangan 2 : "))
        c = a * b
        print ("Hasilnya perkalian = ", c)

    elif pilihan == "4" :
        # ========= PEMBAGIAN
        a = int(input("Bilangan 1 : "))
        b = int(input("Bilangan 2 : "))
        c = a / b
        print ("Hasilnya pembagiannya = ", c)

    elif pilihan == "5" :
        # ========= PEMANGKATAN 2
        a = int(input ("Masukkan Bilangan : "))
        print ("Hasilnya pangkat duanya = ", a**2)

    elif pilihan == "6" :
        # PEMANGKATAN
        a = int(input ("Masukkan Bilangan: "))
        b = int(input ("Masukkan Pangkat: "))
        c = a ** b
        print ("Hasilnya Pemangkatannya = ", c)

    elif pilihan == "7" :
        # ========= PENGAKARAN
        a = int(input ("Masukkan bilangan : "))
        print ("Hasilnya akarnya = ", math.sqrt(a))

    elif pilihan == "0" :
        # ======== EXIT
        print ("Good Bye!")
        sys.exit()

    else :
        print ("Menu salah")

    input()
    os.system("clear")
    return cobamenu()


# POLA POLA BENTUK ===============

def polapola():
    chara = ("*")
    spasi = (" ")
    jarak = ("\n")
    print ("Menu Pola - Pola")
    print ("1. Segitiga Siku Bawah Kiri")
    print ("2. Segitiga Siku Bawah Kanan")
    print ("3. Segitiga Siku Atas Kiri")
    print ("4. Segitiga Siku Atas Kanan")
    print ("5. Persegi")
    print ("6. Persegi Panjang")
    print ("7. Segitiga Sama Sisi")
    print ("8. Belah Ketupat")
    print ("9. Lambang Plus")
    print ("10. Segitiga Kebawah")
    print ("11. Segitiga Kekanan")
    print ("12. Segitiga Kekiri")
    print ("13. Lambang Nazi")
    print ("0. EXIT\n")

    pilihan = input("Masukkan menu : ")
    if pilihan == "1":
        print (" Segitiga siku bawah kiri")
        sisi = int(input ("Masukkan tinggi segitiga : "))
        tinggi, alas = 1, 1
        while (tinggi <= sisi) :
            while (alas <= tinggi) :
                print (chara * alas)
                alas = alas + 1
            tinggi = tinggi + 1

    elif pilihan == "2" :
        print ("Segitiga siku bawah kanan")
        sisi  = int (input ("Masukkan tinggi segitiga : "))
        tinggibin, alasbin = 1, 1
        tinggispa = sisi
        while (tinggibin <= sisi) :
            while (alasbin <= tinggibin) :
                tinggispa = tinggispa - 1
                print(spasi * tinggispa, chara * alasbin)
                alasbin = alasbin + 1
            tinggibin = tinggibin + 1

    elif pilihan == "3" :
        print ("Segitiga siku atas kiri")
        sisi = int(input("Masukkan tinggi segitiga : "))
        tinggi, alas = sisi, sisi
        while (tinggi != 0) :
            while (alas != 0) :
                print (chara * alas)
                alas = alas - 1
            tinggi = tinggi - 1

    elif pilihan == "4" :
        print ("Segitiga siku atas kanan")
        sisi = int(input("Masukkan tinggi segitiga : "))
        tinggibin, alasbin = sisi, sisi
        tinggispa = 0
        while (tinggibin != 0):
            while (alasbin != 0):
                print(tinggispa * spasi, alasbin * chara)
                alasbin = alasbin - 1
                tinggispa = tinggispa + 1
            tinggibin = tinggibin - 1

    elif pilihan == "5" :
        print ("Persegi")
        sisi = int(input("Masukkan panjang sisi : "))
        tinggi = 1
        while (tinggi <= sisi) :
            print (chara * sisi)
            tinggi = tinggi + 1

    elif pilihan == "6" :
        print ("Persegi panjang")
        panjang = int(input("Masukkan panjang sisi  : "))
        lebar   = int(input("Masukkan lebar sisi    : "))
        tinggi = 1
        while (tinggi <= lebar) :
            print ( chara * panjang)
            tinggi = tinggi + 1

    elif pilihan == "7" :
        print ("segitiga sama sisi")
        tinggibin, alasbin, bintang = 1, 1, 1
        sisi = int(input("Masukkan tinggi segitiga : "))
        tinggispa = sisi
        while (tinggibin <= sisi):
            while (alasbin <= tinggibin):
                print(tinggispa * spasi, bintang * chara)
                tinggispa = tinggispa - 1
                bintang = bintang + 2
                alasbin = alasbin + 1
            tinggibin = tinggibin + 1

    elif pilihan == "8" :
        print ("belah ketupat")
        tinggibin, alasbin, bintang = 1, 1, 1
        sisi = int(input("Masukkan tinggi jari - jari : "))
        tinggispa = sisi
        while (tinggibin <= (sisi)):
            while (alasbin <= tinggibin):
                print(tinggispa * spasi, bintang * chara)
                tinggispa = tinggispa - 1
                bintang = bintang + 2
                alasbin = alasbin + 1
            tinggibin = tinggibin + 1
        while (tinggibin != 0) :
            while (alasbin != 0):
                print (tinggispa * spasi, bintang * chara)
                tinggispa = tinggispa + 1
                bintang = bintang - 2
                alasbin = alasbin - 1
            tinggibin = tinggibin - 1

    elif pilihan == "9" :
        print ("Tanda Plus")
        panjang = 1
        sisi = int(input("Masukkan panjang sisi : "))
        while (panjang <= sisi) :
            print (spasi * (sisi-1), chara)
            panjang = panjang + 1
        print(chara * ((sisi*2)+1))
        while (panjang != 0) :
            print (spasi * (sisi-1), chara)
            panjang = panjang - 1

    elif pilihan == "10":
        print ("Segitiga kebawah")
        sisi = int(input("masukkan tinggi segitiga : "))
        tinggi = sisi
        spasinya = 0
        while (tinggi != 0) :
            print (spasinya * spasi, chara * ((tinggi*2)-1))
            spasinya = spasinya + 1
            tinggi = tinggi - 1

    elif pilihan == "11" :
        print ("Segitiga Kekanan")
        sisi = int(input("Masukkan tinggi segitiga : "))
        tinggi = 1
        while (tinggi <= sisi):
            print(chara * tinggi)
            tinggi = tinggi + 1
        tinggi = tinggi - 2
        while(tinggi != 0 ) :
            print (chara * tinggi)
            tinggi = tinggi - 1

    elif pilihan == "12" :
        print ("Segitiga Kekiri")
        sisi = int(input("Masukkan tinggi segitiga : "))
        tinggi = 1
        spasinya = sisi
        while (tinggi <= sisi) :
            print (spasi * spasinya, chara * tinggi)
            spasinya = spasinya - 1
            tinggi   = tinggi + 1
        tinggi = tinggi - 2
        spasinya = spasinya + 2
        while (tinggi != 0) :
            print (spasi * spasinya, chara * tinggi)
            spasinya = spasinya + 1
            tinggi   = tinggi - 1

    elif pilihan == "13" :
        os.system("clear")
        print ("\nLambang Nazi\n")
        sisi = int(input ("Masukkan panjang sisi (minimal 2) : \n"))
        if (sisi < 2 ):
            print ("Harus lebih besar dari 2 !!")
        else :
            sisi1, sisi2, sisi3, sisi4 = 1, 1, 1, 1
            intervalchara = sisi - 1
            intervalsisi  = sisi - 2
            intervalspasi = sisi - 4
            while (sisi1 != sisi) :
                sisi1 = sisi
                print ((chara*sisi),(spasi*intervalspasi), chara)
                while (sisi2 != intervalchara) :
                    print ((spasi * intervalsisi), chara, (spasi * intervalspasi), chara)
                    sisi2 = sisi2 + 1

            print (chara*(sisi+intervalchara))

            while (sisi3 != sisi) :
                sisi3 = sisi
                while (sisi4 != intervalchara):
                    print (chara, (spasi*intervalspasi), chara)
                    sisi4 = sisi4 + 1
                print (chara, (spasi*intervalspasi), (chara * sisi))

    elif pilihan == "0" :
        sys.exit()

    else :
        print ("Menu salah")

    input ()
    os.system("clear")
    return polapola()

polapola()
