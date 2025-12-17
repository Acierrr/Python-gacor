import random

x="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sandi = int(input ("masukkan panjang kata sandi yang di inginkan!"))
password=""
if sandi <=0:
    print ("angka yang anda masukkan tidak valid")
for i in range(sandi):
    y=random.choice(x)
    password+=y

print (password)
