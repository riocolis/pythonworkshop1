def cetak_awalan():
    print("ini awalannya")

def cetak_nama(nama=None):
    if nama is None :
        print("Anda tidak punya nama ")
    else :
        print("nama anda adalah : "+nama)

def luas(panjang, lebar):
    return panjang * lebar

def bingung():
    pass

cetak_awalan()
cetak_nama("Sebastien")
cetak_nama()
bingung()
print("Luas Persegi Panjang {} x {} = {}".format(10,12,luas(10,12)))