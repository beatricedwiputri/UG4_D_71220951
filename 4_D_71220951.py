masukkanbilangan = input("Masukkan sekumpulan bilangan (pisahkan dengan koma): ")

listbilangan = list(map(int, masukkanbilangan.split(",")))
bilterbesar = max(listbilangan, key=lambda n:n)
bilterkecil = min(listbilangan, key=lambda n:n)

print("Bilangan terbesar dari kumpulan bilangan yang di input adalah", bilterbesar)
print("Bilangan terkecil dari kumpulan bilangan di input adalah", bilterkecil)
