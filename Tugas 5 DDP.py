Kendaraan=["Mobil","Sport","Lamborghini",6.498]
Kendaraan.append("abu")
print(Kendaraan)
Kendaraan.append(4)
print(Kendaraan)
Kendaraan.append("30.000.000")
print(Kendaraan)
Kendaraan.remove("Sport")
print(Kendaraan)

pilihan = input("Pilih Opsi:")
match pilihan:
    case"1":
        s = int(input("masukan sisi:"))
        persegi = s*s
        print("luas persegi", persegi)
    case"2":
        phi=3.14
        r=int(input("masukan jari jari:"))
        lingkaran=phi*r*r
        print("luas lingkaran",lingkaran)
    case"3":
        l=1/2
        a=int(input("masukan alas:"))
        t=int(input("masukan tinggi:"))
        segitiga=l*a*t
        print("luas segitiga",segitiga)
    case _:
        print("Pilihan tidak tersedia")