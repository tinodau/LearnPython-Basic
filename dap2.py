def kalitambah():
    def kali (a, b) :
        total = a * b
        return total

    def jumlah (a, b) :
        total = a + b
        return total

    a = int(input("Masukkan nilai A = "))
    b = int(input("Masukkan nilai B = "))

    hasilkali = kali(a,b)
    hasiljumlah = jumlah(a,b)

    print (hasilkali)
    print (hasiljumlah)


def pola1() : #GAGAL
    panjang = int(input("masukkan panjang : "))
    i, j = 1, 1
    while i <= panjang :
        while j <= panjang :
            if i==1 or j==1 :
                print("*")
            j = j + 1
        i = i + 1

def main ():
    print("1. Kali tambah")
    menu = int(input("Pilih menu : "))
    if menu == 1 :
        kalitambah()
    elif menu == 2 :
        pola1()

main()
