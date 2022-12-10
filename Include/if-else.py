n1=int(input("Bir sayı giriniz: "))

if n1==0:
    print("Sayı sıfıra eşittir")
elif n1>0:
    print("Sayı sıfırdan büyük")
else:
    print("Sayı sıfırdan küçük")


# Bir üniversite öğrencisinin vize final notları alınsın, vizenin ağırlığı %40
# finalin ağırlığı %60, 55 altı kalır, 55-60 şartlı geçer, 60 geçer

v=int(input("Vize notunuzu giriniz: "))
f=int(input("Final notunuzu giriniz: "))

tn = float (v*0.4 + f*0.6)
print("Öğrencinin notu: " , tn)

if tn<55:
    print("Öğrenci kaldı!")
elif tn==55 and tn<60:
    print("Öğrenci şartlı geçti.")
else:
    print("Öğrenci geçti.")

