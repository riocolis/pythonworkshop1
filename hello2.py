print("tulisan yang ingin ditampilkan pertama",end=' dan ')
print("tulisan yang ingin ditampilkan kedua",end="\n")
print("tulisan yang ingin ditampilkan ketiga",end="\n")

nama1 = 'Alpha'
nama2 = 'Beta'
nama3 = 'Chalice'
nama4 = 'Dexter'
nilai1 = 100
nilai2 = 80
nilai3 = 70
nilai4 = 95

print(nama1, nama2, nama3 ,nama4,end="\n")
print(nama1, nama2, nama3 ,nama4,sep="\n")
print(nama1, nama2, nama3 ,nama4,sep="-")

mencoba = "nama : {} nilai kamu : {}".format(nama2,nilai2)
mencoba2 = "nama : %s nilai kamu adalah : %.2f " % (nama3,nilai3)
mencoba3 = "nama : "+nama4+" nilai kamu  = "+str(nilai4)
print("nama : {} nilainya {}".format(nama1,nilai1))
print(mencoba)
print(mencoba2)
print(mencoba3)

umur = input("masukkan umur anda: ")
print("umur anda adalah :"+umur)
print("umur anda menikah adalah : {}".format(int(umur)+10))
print("umur anda tua adalah : {}".format(int(umur)+40))