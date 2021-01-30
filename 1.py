print("Program sederhana untuk menghitung kredit rumah")

print("\nJenis Rumah")
print("\n1.Rose 120.000.000 \t2.Gold 300.000.000 \t3.Platinum 360.000.000")
rumah = int(input("Masukan jenis rumah yang mau kamu ambil:"))

print("\nLama kredit")
print("\n1.12 Bulan \t2.18 Bulan \t3.24 Bulan")
kredit = int(input("Masukan lama kredit:"))

if rumah == 1:
    tiperumah = "Rose"
    hargarumah = 120000000
    uangmuka = hargarumah * (20/100)
    sisa = hargarumah - uangmuka
elif rumah == 2:
    tiperumah = "Gold"
    hargarumah = 300000000
    uangmuka = hargarumah * (20/100)
    sisa = hargarumah - uangmuka
elif rumah == 3:
    tiperumah = "Platinum"
    hargarumah = 360000000
    uangmuka = hargarumah * (20/100)
    sisa = hargarumah - uangmuka
else:
    print("anda salah memasukan format")
    exit()

if kredit == 1:
    lamakredit = 12
    angsuran = sisa / lamakredit
elif kredit == 2:
    lamakredit = 18
    angsuran = sisa / lamakredit
elif kredit == 3:
    lamakredit = 24
    angsuran = sisa / lamakredit
else:
    print("anda salah memasukan format")
    exit()

print("\nType Rumah\t:{}".format(tiperumah))
print("Harga Rumah\t:{}".format(hargarumah))
print("Uang Muka\t:{}".format(uangmuka))
print("Sisa\t\t:{}".format(sisa))
print("Lama Kredit\t:{}".format(lamakredit))
print("Angsuran\t:{}".format(angsuran))

print("\nTabel angsuran")
print("\n")

for i in range(lamakredit):
    sisa = sisa - angsuran
    print("Bulan ke {}\tangsuran {}\tsisa {}".format(i + 1,angsuran,sisa))
    



