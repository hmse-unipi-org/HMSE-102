nilai = int(input("Masukkan nilai :"))
if(nilai > 80 and nilai < 100):
    print("A")
elif(nilai >= 60):
    print("B")
elif(nilai > 40 and nilai < 59):
    print("C")
elif(nilai >= 20):
    print("D")
else:
    print("E")