inp_angka = input("Inputkan sebuah angka : ")
inputangka = int(inp_angka)

if inputangka >= 10 :
    print("Inputan angka anda melebihi dari 10 ")
else :
    print("Inputan angka anda kurang dari 10 ")

if inputangka >= 10 and inputangka <= 100:
    print("Inputan angka anda antara 10 sampai 100")
    if inputangka >=10 and inputangka <= 50:
        print("Inputan angka anda antara 10 sampai 50")
    else:
        print("Inputan angka anda antara 50 sampai 100")
elif inputangka >100 and inputangka <=1000:
    print("Inputan angka anda antara 100 sampai 1000")
elif inputangka > 1000 and inputangka <= 10000:
    print("Inputan angka anda antara 1000 sampai 10000")
elif inputangka<0:
    pass
else :
    print("Inputan angka melebihi 10000")