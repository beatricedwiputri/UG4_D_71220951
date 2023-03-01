print("=================== BARIS ARITMATIKA ===================")
u1 = int(input("Masukkan bilangan awal : "))
b = int(input("Masukkan selisih bilangan : "))
n = int(input("Masukkan banyaknya suku : "))

def aritmatika (u1, b, n):
    rumusaritmatika = (n/2)*(2*u1 + (n-1)*b)
    return rumusaritmatika

totalderetarit = aritmatika(u1, b, n)

print("Total dari deret aritmatika tersebut adalah :", totalderetarit)
