m = int(input("Masukkan jumlah baris: "))#masukkan angka 4
n = int(input("Masukkan jumlah kolom: "))#masukkan angka 5
x = [0]*m
for i in range(m):
    x[i] = [1]*n
print(x)