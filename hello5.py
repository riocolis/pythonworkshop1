larik = [5,6,7,11,20,"86","tulisan lain",8.7]
print("Jumlah data = {}".format(len(larik)))
print(larik[5]) #orint dari depan
print(larik[-1]) #print dari belakang
print(larik[-5]) #print dari belakang

for idx, data in enumerate(larik):
    print("data ke {} dan isinya {} ".format(idx,data))
# for data in larik:
#    print(data)
# ctrl + /

menu = {'makanan' :"geprek" , 'harga' : 10000 , 'bonus' : "es Teh Segar +  nasi banyak"}
print("\n\n")
# for deklarasi in menu :
#     print(deklarasi)

# for isivalue in menu.values():
#     print(isivalue)

# for iterasi, jumlah in menu.items():
#     print("{} : {}".format(iterasi,jumlah))

for jajal in range(len(larik)-1,0,-1):
    print(larik[jajal])
