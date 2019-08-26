print('Selamat datang di Parseltongue..')

coba = 1 + 2 + 3 + \
    4 + 5 + 6 

coba2 = (1 + 2 + 3
    + 4 + 5 + 6)

print(coba)
print(coba2)

nama = "Nurcholis"
umur = 21
gelar = "SMA"

"""
Komentar Yang dari bari sampai ke baris, Doc String untuk membuat anotasi pada catatan kelas,fungsi atau program.
"""
#komentar line
greeting = "3.Selamat Datang {}, umur {}, gelar {}".\
    format(nama,umur,gelar)

greeting1 = "4.Selamat Datang "+nama+", umur "+str(umur)+", gelar "+gelar

print("1.Selamat datang {}, umur {}, gelar {}".format(nama,umur,gelar))
print("2.Selamat datang "+nama+", umur",umur,", gelar "+gelar)
print(greeting)
print(greeting1)

#Variabel tipe data dynamis
#type() = untuk mengetahui jenis variabel
#tipe data harus diajarkan.
type(nama)
