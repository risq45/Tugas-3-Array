arrBerat = []
bMin = 0
bMax = 0
rata = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    bMin = min(arrBerat)
    bMax = max(arrBerat)

def rerata(arrBerat):
    global rata
    rata = sum(arrBerat)/len(arrBerat)

print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    # Inisialisasi Input Data Berat
    # Masukkan Data Berat Ke Array (arrBerat)
    arrBerat.append(float(input()))


# Panggil procedur hitungMinMax(arrBerat)
hitungMinMax(arrBerat)
rerata(arrBerat)
# Print Data Minimum, Maximum, dan Rerata Berat
print("Berat balita minimum :",bMin,"kg")
print("Berat balita maksimum :",bMax,"kg")
print("Rerata berat balita : {:.2f} kg".format(rata))
