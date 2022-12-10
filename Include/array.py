# Diziler

ar = [0,1,2,3,4,5]

ar[0] = 5 #Dizinin 0.elemanını 5 olarak değiştirdi.
print(ar)
print(ar[0]) #Dizinin istediğimiz elemanını çağırırken [] kullanırız.

print(ar[0:3]) #0.elemandan 3.elemana kadar yazdırır.
print(ar[:3])

print(ar[3:]) #3.elemandan sonucnu elemana kadar yazdırır.
print(ar[-1]) #Dizinin sonuncu elemanını getirir.

# dizi uzunluğu
print("Dizi uzunluğu", len(ar))

# String diziler

sar = ["elma","armut","çilek","muz"]
print(sar[2])

sar.append("nar") #diziye yeni bir değer eklememize yarar.
print(sar)

del sar[1] #1.indisteki eleman silinir.
print(sar)
sar.remove("elma") #değer üzerinden silme.
print(sar)

sar.pop(0)
print(sar)

sar += ["elma", "armut", "çilek"]
print(sar)

sar *=2 #her dizi elemanını 2.kez ekler
print(sar)

nar = [12,22,63,57,72,34,15]
nar.sort() #Büyükten küçüğe doğru sıraladı.
print(nar)

nar.reverse() #diziyi tersten saydırarak büyükten küçüğe saydırır.
print(nar)

print(nar.count(15)) #15 elemanı kaç kere tekrar etmiştir.

nar.clear() #hepsini siler.
print(nar)

nar.insert(0,15) #0.elemana 15 i ekler
nar.index(1,35)
print()