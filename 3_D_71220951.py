masukkankalimat = input("Masukkan sebuah kalimat: ")

def kataterpanjang(masukkankalimat):
    splitkata = masukkankalimat.split()
    kataterpanjang = ""

    for kata in splitkata:
        if (len(kata)>len(kataterpanjang)):
            kataterpanjang = kata
    return kataterpanjang

print("Kata terpanjang dalam kalimat tersebut adalah:", kataterpanjang(masukkankalimat))
